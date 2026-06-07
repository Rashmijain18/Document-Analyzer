import ChatInput from "./ChatInput";
import ChatMessage from "./ChatMessage";

export default function ChatPanel() {
  return (
    <section className="w-[500px] border-l bg-white flex flex-col">
      <div className="p-4 border-b">
        <h2 className="font-semibold">Ask The Document</h2>
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        <ChatMessage
          role="user"
          message="What was the main reason for revenue growth?"
        />

        <ChatMessage
          role="assistant"
          message="Enterprise subscription expansion drove most of the growth."
        />
      </div>

      <ChatInput />
    </section>
  );
}
