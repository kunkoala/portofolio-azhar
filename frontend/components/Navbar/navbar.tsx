import Link from "next/link";
import { Sheet, SheetTrigger, SheetContent } from "@/components/ui/sheet";
import { Button } from "@/components/ui/button";
import { GithubIcon } from "lucide-react";
import { ThemeToggle } from "@/components/Navbar/theme-toggle";
import { EXTERNAL_LINKS, PATHS } from "@/lib/constants";

const menuItems = [
  { href: "#hero-section", label: "About" },
  { href: "#projects-section", label: "Projects" },
  { href: "#experience-section", label: "Experience" },
];

export function Navbar({ showMenu = true }: { showMenu?: boolean }) {
  return (
    <header className="top-0 z-50 w-full bg-background shadow-sm">
      <div className="container mx-auto flex h-16 items-center justify-between px-4 md:px-6">
        <div className="flex gap-4 items-center">
          <Link
            href={PATHS.HOME}
            className="flex items-center gap-2"
            prefetch={false}
          >
            <MountainIcon className="h-6 w-6" />
            <span className="text-lg font-semibold">Azhar</span>
          </Link>
        </div>
        {showMenu && (
          <nav className="hidden gap-4 sm:flex">
            {menuItems.map((item) => (
              <Link
                key={item.label}
                href={item.href}
                className="text-md font-medium hover:text-pink-500 transition-colors"
                prefetch={false}
              >
                {item.label}
              </Link>
            ))}
          </nav>
        )}
        <div className="hidden sm:flex">
          <LinksAndToggle />
        </div>
        <Sheet>
          <SheetTrigger asChild>
            <Button variant="outline" size="icon" className="sm:hidden">
              <MenuIcon className="h-6 w-6" />
              <span className="sr-only">Toggle navigation menu</span>
            </Button>
          </SheetTrigger>
          <SheetContent side="right" className="w-64 bg-background p-4">
            <div className="flex flex-col justify-between gap-4 h-full">
              {showMenu && (
                <nav className="grid gap-4">
                  {menuItems.map((item) => (
                    <Link
                      key={item.label}
                      href={item.href}
                      className="text-sm font-medium text-foreground hover:text-primary transition-colors"
                      prefetch={false}
                    >
                      {item.label}
                    </Link>
                  ))}
                </nav>
              )}

              <div className="flex flex-col gap-2">
                <LinksAndToggle />
                <p className="text-sm text-foreground">
                  &copy; {new Date().getFullYear()} Azhar Rahadian
                </p>
              </div>
            </div>
          </SheetContent>
        </Sheet>
      </div>
    </header>
  );
}

function LinksAndToggle() {
  return (
    <div className="flex items-center gap-4">
      <Link href={PATHS.BLOG} className="text-sm md:text-md">
        Blog
      </Link>
      <Link
        className="text-sm md:text-md font-semibold bg-pink-100/40 p-2 rounded-md hover:bg-gray-100 transition"
        href={PATHS.GUESTBOOK}
      >
        Guestbook
      </Link>
      <Link
        href={EXTERNAL_LINKS.GITHUB_PROFILE}
        target="_blank"
        className="hover:text-primary transition-colors"
        prefetch={false}
      >
        <GithubIcon className="h-6 w-6" />
      </Link>
      <ThemeToggle />
    </div>
  );
}

function MenuIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <line x1="4" x2="20" y1="12" y2="12" />
      <line x1="4" x2="20" y1="6" y2="6" />
      <line x1="4" x2="20" y1="18" y2="18" />
    </svg>
  );
}

function MountainIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m8 3 4 8 5-5 5 15H2L8 3z" />
    </svg>
  );
}
