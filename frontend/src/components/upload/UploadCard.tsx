import { useRef } from "react";
import { UploadCloud } from "lucide-react";

import Button from "../common/Button";
import { uploadDocument } from "../../services/documentService";

import "../../styles/uploadCard.css";

function UploadCard() {
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleBrowseClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = async (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const file = event.target.files?.[0];

    if (!file) return;

    try {
      const result = await uploadDocument(file);

      console.log(result);

      alert("PDF uploaded successfully!");
    } 
    catch (error) {
  console.error("Upload Error:", error);

  if (error instanceof Error) {
    alert(error.message);
  } else {
    alert("Upload failed.");
  }
}
  };

  return (
    <section className="upload-card">
      <div className="upload-icon">
        <UploadCloud strokeWidth={1.7} />
      </div>

      <h2>Drop your PDF here</h2>

      <p>
        Drag & drop your file or browse from your computer.
      </p>

      <Button onClick={handleBrowseClick}>
        Browse Files
      </Button>

      <input
        ref={fileInputRef}
        type="file"
        accept=".pdf"
        hidden
        onChange={handleFileChange}
      />

      <span className="upload-note">
        PDF • Maximum size 10 MB
      </span>
    </section>
  );
}

export default UploadCard;