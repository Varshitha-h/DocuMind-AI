import {
  createContext,
  useContext,
  useState,
  type ReactNode,
} from "react";

interface DocumentContextType {
  uploadedFile: string | null;
  setUploadedFile: (file: string | null) => void;

  isDocumentUploaded: boolean;
  setIsDocumentUploaded: (value: boolean) => void;
}

const DocumentContext = createContext<DocumentContextType | undefined>(
  undefined
);

export function DocumentProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [uploadedFile, setUploadedFile] = useState<string | null>(null);

  const [isDocumentUploaded, setIsDocumentUploaded] =
    useState(false);

  return (
    <DocumentContext.Provider
      value={{
        uploadedFile,
        setUploadedFile,

        isDocumentUploaded,
        setIsDocumentUploaded,
      }}
    >
      {children}
    </DocumentContext.Provider>
  );
}

export function useDocument() {
  const context = useContext(DocumentContext);

  if (!context) {
    throw new Error(
      "useDocument must be used within DocumentProvider"
    );
  }

  return context;
}