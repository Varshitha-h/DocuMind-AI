import { Brain, FileText, Plus, Circle } from "lucide-react";
import { useDocument } from "../../context/DocumentContext";
import "../../styles/sidebar.css";

function Sidebar() {
  const { uploadedFile } = useDocument();

  return (
    <aside className="sidebar">

      {/* Logo */}

      <div className="sidebar-logo">

        <div className="logo-box">
          <Brain size={22} />
        </div>

        <div>
          <h2>DocuMind AI</h2>
          <p>AI Document Assistant</p>
        </div>

      </div>

      {/* New Chat */}

      <button className="new-document">
        <Plus size={18} />
        <span>New Chat</span>
      </button>

      <div className="sidebar-divider"></div>

      {/* Recent Files */}

      <div className="sidebar-section">

        <h3>Recent Documents</h3>

        <ul className="document-list">

          {uploadedFile ? (

            <li className="active">

              <FileText size={18} />

              <span>{uploadedFile}</span>

            </li>

          ) : (

            <li className="empty">

              No documents uploaded

            </li>

          )}

        </ul>

      </div>

      {/* Bottom Status */}

      <div className="sidebar-status">

        <div className="status-header">

          <Circle
            size={10}
            fill="#22c55e"
            stroke="#22c55e"
          />

          <span>Local AI</span>

        </div>

        <p>Llama 3.2 Ready</p>

      </div>

    </aside>
  );
}

export default Sidebar;