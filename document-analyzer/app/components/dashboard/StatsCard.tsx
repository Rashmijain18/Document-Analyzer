type Props = {
  title: string;
  value: string;
};

export default function StatsCard({ title, value }: Props) {
  return (
    <div className="bg-white border rounded-xl p-6">
      <h2 className="text-3xl font-bold">{value}</h2>

      <p className="text-gray-500">{title}</p>
    </div>
  );
}
