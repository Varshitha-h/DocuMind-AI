import Card from "../common/Card";

function WelcomeCard() {
  return (
    <section className="welcome-section">

      <h1>👋 Welcome to DocuMind AI</h1>

      <h2>Talk to your documents using AI</h2>

      <p>
        Upload a PDF to start a conversation powered by
        semantic search and a local Llama 3.2 model.
      </p>

      <div className="feature-grid">

        <Card
          icon="⚡"
          title="Fast Local AI"
          description="Powered by Ollama running completely on your computer."
        />

        <Card
          icon="🧠"
          title="Semantic Search"
          description="Finds the most relevant information using FAISS embeddings."
        />

        <Card
          icon="🔒"
          title="Private"
          description="Your documents remain on your local machine."
        />

      </div>

    </section>
  );
}

export default WelcomeCard;