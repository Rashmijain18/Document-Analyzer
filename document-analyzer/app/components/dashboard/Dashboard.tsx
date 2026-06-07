// components/dashboard/Dashboard.tsx

import KeyPointsCard from "./KeyPointCard";
import StatsCard from "./StatsCard";
import SummaryCard from "./SummaryCard";

export default function Dashboard() {
  return (
    <main className="flex-1 p-6 overflow-auto">
      <div className="grid grid-cols-3 gap-4">
        <StatsCard title="Chunks Indexed" value="1,842" />

        <StatsCard title="Questions Asked" value="12" />

        <StatsCard title="AI Cost" value="$0.04" />
      </div>

      <SummaryCard />

      <KeyPointsCard />
    </main>
  );
}
