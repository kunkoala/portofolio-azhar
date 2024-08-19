export function ExperienceSection() {
  return (
    <section
      className="min-h-screen flex flex-col items-center  bg-inherit dark:bg-inherit py-12 md:py-16"
      id="experience-section"
    >
      <div className="container px-4 md:px-6 flex flex-col items-center">
        <h1 className="text-5xl tracking-tight font-bold text-center">
          Experience
        </h1>
        <div className="flex flex-col py-12 max-w-5xl">
          {experience.map((exp) => (
            <ExperienceTable {...exp} />
          ))}
        </div>
      </div>
    </section>
  );
}

type Experience = {
  title: string;
  company: string;
  location: string;
  date: string;
  description: string;
};

const experience = [
  {
    title: "Hackathon Participant",
    company: "START Hack 2024",
    location: "St. Gallen",
    date: "March 2024",
    description:
      "Collaborated with a team of engineers, leveraging Python, GPT-4, RAG, Microsoft Azure, and Twilio to create a functional voice bot prototype for Canton of St. Gallen, enabling phone call-based citizen support for basic inquiries.",
  },
  {
    title: "Head of IT",
    company: "PPI Jerman",
    location: "Germany",
    date: "October 2023 - Present",
    description:
      "Lead a team of nine dedicated IT team members, managing and enhancing the organization’s digital structure with strategic planning, team leadership, and technical acumen, ensuring effective collaboration with various departments as well as overseeing diverse technology initiatives.",
  },
  {
    title: "Student",
    company: "TU Braunschweig",
    location: "Braunschweig",
    date: "2021 - Present",
    description:
      "Strong points in full-stack development, software engineering, and data science.",
  },
];

function ExperienceTable(experience: Experience) {
  return (
    <div className="flex flex-col gap-1 py-4">
      <h2 className="text-xl font-bold">
        {experience.title} @ {experience.company}
      </h2>
      <p className="text-muted-foreground">
        {experience.location} | {experience.date}
      </p>
      <p className="text-muted-foreground">{experience.description}</p>
    </div>
  );
}
