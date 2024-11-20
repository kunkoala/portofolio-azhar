import { Navbar } from "@/components/Navbar/navbar";
import { Footer } from "@/components/Navbar/footer";
import { ThemeProvider } from "@/components/theme-provider";
import { lora } from "@/lib/fonts";

export default function GuestbookLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <section className={lora.className}>
      <Navbar showMenu={false} />
      {children}
      <Footer />
    </section>
  );
}
