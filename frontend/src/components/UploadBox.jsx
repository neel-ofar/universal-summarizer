import React from "react";

export default function UploadBox({ onSelect }) {
  return (
    <div className="border border-gray-300 rounded-2xl p-10 text-center bg-white shadow-sm">
      <input
        type="file"
        accept="image/*"
        onChange={(e) => onSelect(e.target.files[0])}
        className="hidden"
        id="upload"
      />

      <label
        htmlFor="upload"
        className="cursor-pointer text-gray-700 text-lg font-medium"
      >
        Click to Upload Fruit Image
      </label>
    </div>
  );
}
