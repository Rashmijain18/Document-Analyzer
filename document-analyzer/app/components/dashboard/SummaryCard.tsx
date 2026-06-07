// components/dashboard/SummaryCard.tsx

export default function SummaryCard() {
  return (
    <div className="mt-6 bg-white border rounded-xl p-6">
      <h2 className="text-sm font-semibold text-gray-500 uppercase mb-4">
        AI Summary
      </h2>

      <p className="text-gray-700 leading-7">
        Revenue grew 18% YoY to $4.2M in Q3, driven by enterprise subscription
        expansion. Operating costs increased 9%, resulting in an improved EBITDA
        margin of 23% versus 17% last year. The report flags increased R&D
        investment ahead of a Q4 product launch.
      </p>
    </div>
  );
}
