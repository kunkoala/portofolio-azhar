import { Navbar } from "@/components/Navbar/navbar";
import { Footer } from "@/components/Navbar/footer";

export default function BlogLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        {children}
        <Footer />
      </body>
    </html>
  );
}
