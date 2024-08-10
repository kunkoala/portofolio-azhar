export function Footer() {
  return (
    <footer className="bg-background text-sm text-foreground py-4">
      <div className="container mx-auto flex items-center justify-between">
        <p>&copy; {new Date().getFullYear()} Azhar Rahadian</p>
      </div>
    </footer>
  );
}
