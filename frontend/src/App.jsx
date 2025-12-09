import React, { useState } from "react";
import axios from "axios";
import UploadBox from "./components/UploadBox";
import ResultCard from "./components/ResultCard";

export default function App() {
  const [imagePreview, setImagePreview] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async (file) => {
    setImagePreview(URL.createObjectURL(file));

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post(" paste link here/predict", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    setResult(res.data);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center pt-20 px-4">
      <h1 className="text-4xl font-bold text-gray-900 mb-6">
        Fruit Intelligence System
      </h1>

      <UploadBox onSelect={handleUpload} />

      {imagePreview && (
        <img
          src={imagePreview}
          alt="preview"
          className="w-64 h-64 object-cover rounded-2xl mt-6 shadow-md"
        />
      )}

      <ResultCard result={result} />
    </div>
  );
}
