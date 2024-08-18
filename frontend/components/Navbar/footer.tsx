export function Footer() {
  return (
    <footer className="dark:bg-gray-950 text-sm py-4 min-h-32">
      <div className="container mx-auto flex items-center justify-between">
        <p>&copy; {new Date().getFullYear()} Azhar Rahadian</p>
      </div>
    </footer>
  );
}
