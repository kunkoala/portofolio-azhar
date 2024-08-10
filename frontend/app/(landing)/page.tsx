import { HeroSection } from "./hero-section";
import { ExperienceSection } from "./experience-section";
import { AboutSection } from "./about-section";
import { ProjectsSection } from "./projects-section";

export default async function Home() {
  return (
    <main className="min-h-screen">
      <div className="container py-12 sm:py-16 md:py-20">
        <div className="flex flex-col justify-center items-center">
          <HeroSection />
          <AboutSection />
          <ProjectsSection />
          <ExperienceSection />
        </div>
      </div>
    </main>
  );
}
