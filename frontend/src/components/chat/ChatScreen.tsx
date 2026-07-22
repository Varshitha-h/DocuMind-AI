import { useEffect, useRef, useState } from "react";
import { Brain, FileText, Sparkles } from "lucide-react";

import ChatInput from "./ChatInput";
import UserMessage from "./UserMessage";
import AIMessage from "./AIMessage";
import TypingIndicator from "./TypingIndicator";

import type { Message } from "../../types/chat";
import { askQuestion } from "../../services/documentService";

import "../../styles/chatScreen.css";

function ChatScreen() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  const handleSend = async () => {
    if (!question.trim() || loading) return;

    const currentQuestion = question;

    const userMessage: Message = {
      id: crypto.randomUUID(),
      role: "user",
      content: currentQuestion,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);

    setQuestion("");
    setLoading(true);

    try {
      const response = await askQuestion(currentQuestion);

      const aiMessage: Message = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: response.answer,
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          id: crypto.randomUUID(),
          role: "assistant",
          content: "Something went wrong while generating the answer.",
          timestamp: new Date(),
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-screen">

      <div className="conversation">

        {messages.length === 0 && (

          <div className="empty-state">

            <div className="empty-logo">
              <Brain size={34} />
            </div>

            <h1>Welcome to DocuMind AI</h1>

            <p>
              Ask questions about your uploaded PDF using local AI.
            </p>

            <div className="suggestions">

              <div>
                <Sparkles size={18} />
                Summarize this document
              </div>

              <div>
                <FileText size={18} />
                Extract key skills
              </div>

              <div>
                <Brain size={18} />
                Explain this document
              </div>

            </div>

          </div>

        )}

        {messages.map((message) =>
          message.role === "user" ? (
            <UserMessage key={message.id} message={message} />
          ) : (
            <AIMessage key={message.id} message={message} />
          )
        )}

        {loading && <TypingIndicator />}

        <div ref={bottomRef} />

      </div>

      <div className="chat-footer">

        <ChatInput
          value={question}
          onChange={setQuestion}
          onSend={handleSend}
          disabled={loading}
        />

      </div>

    </div>
  );
}

export default ChatScreen;