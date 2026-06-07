type Props = {
  name: string;
  pages: number;
  size: string;
  active?: boolean;
};

export default function DocumentItem({ name, pages, size, active }: Props) {
  return (
    <div
      className={`mx-2 p-3 rounded-xl cursor-pointer ${
        active ? "bg-green-50 border border-green-300" : "hover:bg-gray-100"
      }`}
    >
      <h3 className="font-medium">{name}</h3>

      <p className="text-xs text-gray-500">
        {size} · {pages} pages
      </p>
    </div>
  );
}
