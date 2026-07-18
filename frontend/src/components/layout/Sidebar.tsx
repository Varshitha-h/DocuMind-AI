import "../../styles/sidebar.css";

function Sidebar() {
  return (
    <aside className="sidebar">

      <h2>📄 Documents</h2>

      <button className="new-document">

        + New Document

      </button>

      <div className="sidebar-divider"></div>

      <h3>Recent Files</h3>

      <ul className="document-list">

        <li>No documents uploaded</li>

      </ul>

    </aside>
  );
}

export default Sidebar;