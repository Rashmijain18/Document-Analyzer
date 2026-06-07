export default function AboutLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  console.log("About layout");
  return (
    <div>
      <h1>About Layout</h1>
      {children}
    </div>
  );
}
