export function Footer() {
  return (
    <footer className="bg-foreground text-sm text-background py-4 min-h-32">
      <div className="container mx-auto flex items-center justify-between">
        <p>&copy; {new Date().getFullYear()} Azhar Rahadian</p>
      </div>
    </footer>
  );
}
