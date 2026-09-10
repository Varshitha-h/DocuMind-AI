import Header from "./Header";
import Sidebar from "./Sidebar";

import "../../styles/layout.css";

type AppShellProps = {
  children: React.ReactNode;
};

function AppShell({ children }: AppShellProps) {
  return (
    <div className="app-shell">

      <Sidebar />

      <div className="main-section">

        <Header />

        <main className="content">
          {children}
        </main>

        <footer className="app-footer">
          © 2026 Varshitha H. All rights reserved.
        </footer>

      </div>

    </div>
  );
}

export default AppShell;