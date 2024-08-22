import { Navbar } from "@/components/Navbar/navbar";
import { Footer } from "@/components/Navbar/footer";
import { lora } from "@/app/layout";

export default function BlogLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <section className={lora.className}>
      <Navbar />
      {children}
      <Footer />
    </section>
  );
}
