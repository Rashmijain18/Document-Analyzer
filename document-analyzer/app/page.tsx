// app/page.tsx

import ChatPanel from "./components/chat/ChatPanel";
import Dashboard from "./components/dashboard/Dashboard";
import Sidebar from "./components/layout/Sidebar";

export default function Home() {
  return (
    <div className="h-screen flex bg-gray-50">
      <Sidebar />
      <Dashboard />
      <ChatPanel />
    </div>
  );
}
