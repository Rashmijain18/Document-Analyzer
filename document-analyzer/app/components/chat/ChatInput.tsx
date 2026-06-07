export default function ChatInput() {
  return (
    <div className="p-4 border-t">
      <div className="flex gap-2">
        <input
          placeholder="Ask anything about this document..."
          className="flex-1 border rounded-lg px-4 py-2"
        />

        <button className="bg-green-600 text-white px-4 rounded-lg">
          Send
        </button>
      </div>
    </div>
  );
}
