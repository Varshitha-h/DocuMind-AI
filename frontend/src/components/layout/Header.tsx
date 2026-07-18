import "../../styles/header.css";

function Header() {
  return (
    <header className="header">

      <div className="header-left">

        <h1>DocuMind AI</h1>

      </div>

      <div className="header-right">

        <span className="status">

          <span className="status-dot"></span>

          Local • Llama 3.2

        </span>

      </div>

    </header>
  );
}

export default Header;