import { SiTypescript, SiPython, SiReact, SiGit } from "react-icons/si";
import { RiNextjsFill } from "react-icons/ri";

export function AboutSection() {
  const skillsLogo = [
    {
      name: "React.js",
      icon: SiReact,
    },
    {
      name: "TypeScript",
      icon: SiTypescript,
    },
    {
      name: "Next.js",
      icon: RiNextjsFill,
    },
    {
      name: "Python",
      icon: SiPython,
    },
    {
      name: "Git",
      icon: SiGit,
    },
  ];
  return (
    <section
      className="flex flex-col items-center justify-center py-12 md:py-16"
      id="about-section"
    >
      <div className="container px-4 md:px-6">
        <div className="grid md:grid-cols-2 gap-8">
          <div className="flex flex-col gap-4 justify-center">
            <p className="text-muted-foreground">
              I like creating stuff from scratch, learning the fundamentals, and
              creating a system.
            </p>
            <p className="text-muted-foreground">
              I specialize in building modern, responsive web applications using
              the latest technologies and frameworks. I also compose music for
              games and films in my free time.
            </p>
          </div>
          <div className="flex flex-col gap-4">
            <h2 className="text-3xl font-bold tracking-tight">
              I specialize in
            </h2>
            <ul className="grid grid-cols-3 gap-y-4 gap-x-2">
              {skillsLogo.map((skill) => (
                <li key={skill.name} className="flex items-center gap-2">
                  <skill.icon className="h-6 w-6" />
                  <span>{skill.name}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
}
