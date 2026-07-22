import { User } from "lucide-react";
import type { Message } from "../../types/chat";
import "../../styles/message.css";

interface UserMessageProps {
  message: Message;
}

function UserMessage({ message }: UserMessageProps) {
  return (
    <div className="message-row user-row">

      <div className="message user-message">

        <div className="message-header">

          <User size={16} />

          <span>You</span>

        </div>

        <div className="message-content">
          {message.content}
        </div>

      </div>

    </div>
  );
}

export default UserMessage;