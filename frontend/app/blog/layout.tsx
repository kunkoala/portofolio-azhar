import { Navbar } from "@/components/Navbar/navbar";
import { Footer } from "@/components/Navbar/footer";
import { ThemeProvider } from "@/components/theme-provider";

export default function BlogLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <Navbar showMenu={false} />
        {children}
        <Footer />
      </body>
    </html>
  );
}
