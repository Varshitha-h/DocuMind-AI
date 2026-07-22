import { Brain, Circle } from "lucide-react";
import "../../styles/header.css";

function Header() {
  return (
    <header className="header">

      <div className="header-left">

        <div className="header-icon">
          <Brain size={20} />
        </div>

        <div>
          <h1>DocuMind AI</h1>
          <p>AI-Powered Document Assistant</p>
        </div>

      </div>

      <div className="header-status">

        <Circle
          size={10}
          fill="#22c55e"
          stroke="#22c55e"
        />

        <div>

          <span>Local AI</span>

          <small>Llama 3.2 Ready</small>

        </div>

      </div>

    </header>
  );
}

export default Header;