import { Brain } from "lucide-react";
import "../../styles/typingIndicator.css";

function TypingIndicator() {
  return (
    <div className="message-row ai-row">
      <div className="message ai-message">

        <div className="message-header">
          <Brain size={16} />
          <span>DocuMind AI</span>
        </div>

        <div className="typing-dots">
          <span></span>
          <span></span>
          <span></span>
        </div>

      </div>
    </div>
  );
}

export default TypingIndicator;