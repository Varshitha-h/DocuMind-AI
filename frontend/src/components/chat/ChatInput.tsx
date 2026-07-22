import { useEffect, useRef } from "react";
import { SendHorizontal } from "lucide-react";
import "../../styles/chatInput.css";

interface ChatInputProps {
  value: string;
  onChange: (value: string) => void;
  onSend: () => void;
  disabled?: boolean;
}

function ChatInput({
  value,
  onChange,
  onSend,
  disabled = false,
}: ChatInputProps) {
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    if (!textareaRef.current) return;

    textareaRef.current.style.height = "0px";
    textareaRef.current.style.height =
      `${textareaRef.current.scrollHeight}px`;
  }, [value]);

  const handleKeyDown = (
    e: React.KeyboardEvent<HTMLTextAreaElement>
  ) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();

      if (value.trim() && !disabled) {
        onSend();
      }
    }
  };

  return (
    <div className="chat-input-wrapper">

      <textarea
        ref={textareaRef}
        rows={1}
        className="chat-input"
        placeholder="Ask anything about your document..."
        value={value}
        disabled={disabled}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={handleKeyDown}
      />

      <button
        className="send-button"
        disabled={!value.trim() || disabled}
        onClick={onSend}
      >
        <SendHorizontal size={18} />
      </button>

    </div>
  );
}

export default ChatInput;