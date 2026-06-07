// components/layout/Sidebar.tsx

import DocumentItem from "../documents/documentItem";

// data/documents.ts

export const documents = [
  {
    id: 1,
    name: "Q3 Financial Report.pdf",
    type: "PDF",
    size: "2.4 MB",
    pages: 48,
    active: true,
  },
  {
    id: 2,
    name: "Product Roadmap 2025.docx",
    type: "DOC",
    size: "840 KB",
    pages: 12,
  },
  {
    id: 3,
    name: "Legal Contract Draft.pdf",
    type: "PDF",
    size: "1.8 MB",
    pages: 35,
  },
  {
    id: 4,
    name: "Research Paper - NLP.pdf",
    type: "PDF",
    size: "3.8 MB",
    pages: 62,
  },
  {
    id: 5,
    name: "Team OKRs Q4.docx",
    type: "DOC",
    size: "210 KB",
    pages: 6,
  },
];

export default function Sidebar() {
  return (
    <aside className="w-72 border-r bg-white flex flex-col">
      <div className="flex flex-row p-4 gap-12 align-center">
        <h3 className="justify-center align-center text-green-600">
          Documents
        </h3>
        <button className="w-full bg-green-600 text-white py-2 rounded-lg">
          Upload
        </button>
      </div>

      <div className="flex-1 overflow-y-auto">
        {documents.map((doc) => (
          <DocumentItem key={doc.id} {...doc} />
        ))}
      </div>
    </aside>
  );
}
