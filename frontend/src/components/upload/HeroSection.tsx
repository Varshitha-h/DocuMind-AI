import { Brain, Shield, Upload, Zap } from "lucide-react";

import Button from "../common/Button";
import Card from "../common/Card";
import UploadCard from "./UploadCard";

import "../../styles/hero.css";

function HeroSection() {
  return (
    <section className="hero">
      {/* Hero Badge */}
      <div className="hero-badge">
        Local AI • Powered by Llama 3.2
      </div>

      {/* Heading */}
      <h1>
        Chat with your <span>Documents</span>
      </h1>

      {/* Description */}
      <p className="hero-description">
        Upload PDFs, ask natural language questions, and receive accurate
        answers powered by semantic search and your local Llama 3.2 model.
      </p>

      {/* Upload Button */}
      {/* <Button>
        <Upload size={18} />
        Upload PDF
      </Button> */}

      {/* Upload Card */}
      <UploadCard />

      {/* Feature Cards */}
      <div className="feature-grid">
        <Card
          icon={<Zap size={30} />}
          title="Fast Local AI"
          description="Runs completely on your machine using Ollama."
        />

        <Card
          icon={<Brain size={30} />}
          title="Semantic Search"
          description="Uses FAISS vector search to find the most relevant document content."
        />

        <Card
          icon={<Shield size={30} />}
          title="Private & Secure"
          description="Your documents remain on your computer. Nothing is uploaded to the cloud."
        />
      </div>
    </section>
  );
}

export default HeroSection;