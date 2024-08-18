export function HeroSection() {
  return (
    <section
      className="h-[50vh] flex flex-col items-center justify-center bg-gray-100 dark:bg-gray-800"
      id="hero-section"
    >
      <main className="w-full">
        <div className="flex flex-col items-center justify-center px-4 md:px-6">
          <h1 className="text-4xl md:text-6xl font-bold tracking-tight">
            Azhar Rahadian
          </h1>
          <p className="text-lg md:text-xl mt-2 max-w-[600px] text-center">
            Full-Stack Developer | Composer{" "}
          </p>
        </div>
      </main>
    </section>
  );
}
