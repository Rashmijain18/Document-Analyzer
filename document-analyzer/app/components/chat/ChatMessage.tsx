type Props = {
  role: "user" | "assistant";
  message: string;
};

export default function ChatMessage({ role, message }: Props) {
  const isUser = role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-md p-3 rounded-2xl ${
          isUser ? "bg-green-600 text-white" : "bg-gray-100"
        }`}
      >
        {message}
      </div>
    </div>
  );
}
