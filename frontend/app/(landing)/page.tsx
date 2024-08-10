import { HeroSection } from "./hero-section";
import { ExperienceSection } from "./experience-section";
import { AboutSection } from "./about-section";
import { ProjectsSection } from "./projects-section";

export default async function Home() {
  return (
    <main className="min-h-screen">
      <HeroSection />
      <AboutSection />
      <ProjectsSection />
      <ExperienceSection />
    </main>
  );
}
