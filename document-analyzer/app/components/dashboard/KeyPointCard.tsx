// components/dashboard/KeyPointsCard.tsx

const highlights = [
  "Enterprise ARR reached $3.1M, up from $2.2M in Q2",
  "Customer churn dropped to 1.8%, lowest since founding",
  "R&D spend increased 32% ahead of Q4 product launch",
  "Cash runway extended to 18 months post Series A close",
  "Headcount grew from 41 to 58, primarily in engineering",
];

export default function KeyPointsCard() {
  return (
    <div className="mt-6 bg-white border rounded-xl overflow-hidden">
      <div className="px-6 py-4 border-b bg-green-50">
        <h2 className="font-semibold">Extracted Highlights</h2>
      </div>

      <ul>
        {highlights.map((item) => (
          <li
            key={item}
            className="flex items-start gap-3 px-6 py-4 border-b last:border-b-0"
          >
            <div className="w-2 h-2 rounded-full bg-green-500 mt-2" />

            <span className="text-gray-700">{item}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
