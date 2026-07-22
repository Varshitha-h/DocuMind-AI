import AppShell from "./components/layout/AppShell";
import HeroSection from "./components/upload/HeroSection";
import ChatScreen from "./components/chat/ChatScreen";

import { useDocument } from "./context/DocumentContext";

function App() {
  const { isDocumentUploaded } = useDocument();

  return (
    <AppShell>
      {isDocumentUploaded ? (
        <ChatScreen />
      ) : (
        <HeroSection />
      )}
    </AppShell>
  );
}

export default App;