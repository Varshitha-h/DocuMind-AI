import { Brain } from "lucide-react";
import type { Message } from "../../types/chat";
import "../../styles/message.css";

interface AIMessageProps {
  message: Message;
}

function AIMessage({ message }: AIMessageProps) {
  return (
    <div className="message-row ai-row">

      <div className="message ai-message">

        <div className="message-header">

          <Brain size={16} />

          <span>DocuMind AI</span>

        </div>

        <div className="message-content">
          {message.content}
        </div>

      </div>

    </div>
  );
}

export default AIMessage;