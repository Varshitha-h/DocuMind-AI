import { UploadCloud, CheckCircle2 } from "lucide-react";
import { useRef, useState } from "react";
import toast from "react-hot-toast";

import { uploadDocument } from "../../services/documentService";
import { useDocument } from "../../context/DocumentContext";

import "../../styles/uploadCard.css";

function UploadCard() {
  const inputRef = useRef<HTMLInputElement>(null);

  const [loading, setLoading] = useState(false);

  const { uploadedFile, setUploadedFile, setIsDocumentUploaded } = useDocument();

  const handleUpload = async (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    const file = e.target.files?.[0];

    if (!file) return;

    if (file.type !== "application/pdf") {
      toast.error("Please upload a PDF file.");
      return;
    }

    try {
      setLoading(true);

      await uploadDocument(file);

      setUploadedFile(file.name);

      setIsDocumentUploaded(true);

      toast.success("Document uploaded successfully!");
    } catch {
      toast.error("Upload failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-card">

      <div className="upload-icon">
        <UploadCloud size={28} />
      </div>

      <h2>Upload your PDF</h2>

      <p>
        Drag & drop your document or browse your files to begin chatting.
      </p>

      <input
        hidden
        ref={inputRef}
        type="file"
        accept=".pdf"
        onChange={handleUpload}
      />

      <button
        className="upload-btn"
        disabled={loading}
        onClick={() => inputRef.current?.click()}
      >
        {loading ? "Uploading..." : "Choose PDF"}
      </button>

      {uploadedFile && (
        <div className="uploaded-file">
          <CheckCircle2 size={18} />
          <span>{uploadedFile}</span>
        </div>
      )}

    </div>
  );
}

export default UploadCard;