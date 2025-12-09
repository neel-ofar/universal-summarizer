import React from "react";

export default function ResultCard({ result }) {
  if (!result) return null;

  return (
    <div className="mt-8 p-6 bg-white rounded-2xl shadow-md border border-gray-200">
      <h2 className="text-2xl font-semibold text-gray-900">
        🍎 Predicted Fruit: {result.fruit}
      </h2>

      <h3 className="mt-4 text-xl font-medium">📌 Nutrition Info</h3>
      <pre className="text-gray-700">{JSON.stringify(result.info, null, 2)}</pre>

      <h3 className="mt-4 text-xl font-medium">🤖 AI Explanation</h3>
      <p className="text-gray-700 mt-2">{result.explanation}</p>
    </div>
  );
}
