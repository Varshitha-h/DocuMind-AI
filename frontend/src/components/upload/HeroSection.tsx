import { Brain, ShieldCheck, Zap } from "lucide-react";
import UploadCard from "./UploadCard";
import "../../styles/hero.css";

function HeroSection() {
  return (
    <section className="hero">

      {/* Badge */}

      <div className="hero-badge">
        🧠 Local AI • Powered by Llama 3.2
      </div>

      {/* Heading */}

      <h1>
        Chat with your <span>Documents</span>
      </h1>

      {/* Subtitle */}

      <p className="hero-description">
        Upload PDF documents and ask questions in natural language.
        Powered by semantic search, FAISS, and your local Llama model.
      </p>

      {/* Upload */}

      <UploadCard />

      {/* Feature Pills */}

      <div className="feature-strip">

        <div className="feature-pill">
          <Zap size={18} />
          <span>Fast Local AI</span>
        </div>

        <div className="feature-pill">
          <Brain size={18} />
          <span>Semantic Search</span>
        </div>

        <div className="feature-pill">
          <ShieldCheck size={18} />
          <span>Private & Secure</span>
        </div>

      </div>

    </section>
  );
}

export default HeroSection;