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

      </div>

    </div>
  );
}

export default AppShell;