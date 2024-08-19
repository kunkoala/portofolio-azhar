import { AppleCardsCarouselDemo } from "./(projects)/projects-carousel";

export function ProjectsSection() {
  return (
    <section
      className="min-h-screen flex flex-col items-center  bg-inherit dark:bg-inherit py-12 md:py-16"
      id="projects-section"
    >
      <div className="container px-4 md:px-6">
        <h1 className="text-5xl tracking-tight font-bold text-center">Projects</h1>
        <AppleCardsCarouselDemo />
      </div>
    </section>
  );
}
