from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.pdf_service import save_pdf
from app.services.pdf_reader import extract_text_from_pdf
from app.rag.chunker import chunk_text
from app.rag.embeddings import generate_embeddings
from app.rag.vector_store import VectorStore

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF, extract text, generate embeddings,
    and store them in a FAISS vector store.
    """

    # Validate uploaded file
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Save PDF
    result = save_pdf(file)

    # Build path to saved PDF
    file_path = Path("uploads") / result["stored_filename"]

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    print("\n========== EXTRACTED TEXT ==========\n")
    print(extracted_text[:500])
    print("\n====================================\n")

    # Split text into chunks
    chunks = chunk_text(extracted_text)

    print("\n========== CHUNK INFORMATION ==========\n")
    print(f"Total Chunks Created: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):
        print(f"\n----------- Chunk {index} -----------")
        print(chunk[:300])

    print("\n=======================================\n")

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    print("\n========== EMBEDDINGS ==========\n")
    print(f"Total Embeddings: {len(embeddings)}")

    if embeddings:
        print(f"Embedding Dimension: {len(embeddings[0])}")

    print("\n================================\n")

    # Create FAISS Vector Store
    vector_store = VectorStore(len(embeddings[0]))

    # Store embeddings with their corresponding text chunks
    vector_store.add_embeddings(
        embeddings=embeddings,
        chunks=chunks
    )

    print("\n========== VECTOR STORE ==========\n")
    print(f"Vectors Stored: {vector_store.index.ntotal}")
    print(f"Embedding Dimension: {len(embeddings[0])}")
    print("\n==================================\n")

    # ----------------------------
    # Test Semantic Search
    # ----------------------------
    test_query = "Do you provide AMC services?"

    query_embedding = generate_embeddings([test_query])[0]

    results = vector_store.search(
        query_embedding=query_embedding,
        top_k=1
    )

    print("\n========== SEARCH RESULT ==========\n")

    if results:
        print(results[0])
    else:
        print("No matching chunks found.")

    print("\n===================================\n")

    return {
        "message": "PDF processed successfully.",
        "original_filename": result["original_filename"],
        "stored_filename": result["stored_filename"],
        "total_chunks": len(chunks),
        "embedding_dimension": len(embeddings[0]) if embeddings else 0,
        "vectors_stored": vector_store.index.ntotal,
        "search_query": test_query,
        "top_result": results[0] if results else None,
        "first_chunk": chunks[0] if chunks else ""
    }