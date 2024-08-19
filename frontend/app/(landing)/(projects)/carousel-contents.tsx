import Image from "next/image";

import sampleStock from "@/assets/stock-images/sample-stock.jpg";
import { ArrowRight } from "lucide-react";

export function DummyContent() {
  return (
    <>
      {[...new Array(3).fill(1)].map((_, index) => {
        return (
          <div
            key={"dummy-content" + index}
            className="bg-[#F5F5F7] p-8 md:p-14 rounded-3xl mb-4"
          >
            <p className="text-neutral-600 text-base md:text-2xl font-sans max-w-3xl mx-auto">
              <span className="font-bold text-neutral-700">
                The first rule of Apple club is that you boast about Apple club.
              </span>{" "}
              Keep a journal, quickly jot down a grocery list, and take amazing
              class notes. Want to convert those notes to text? No problem.
              Langotiya jeetu ka mara hua yaar is ready to capture every
              thought.
            </p>
            <Image
              src={sampleStock}
              alt="Macbook mockup from Aceternity UI"
              height="500"
              width="500"
              className="md:w-1/2 md:h-1/2 h-full w-full mx-auto object-contain"
            />
          </div>
        );
      })}
    </>
  );
}

export function SensusContent() {
  return (
    <div className="bg-[#F5F5F7] p-8 md:p-14 rounded-3xl mb-4 flex flex-col gap-4">
      <p className="text-neutral-600 text-base md:text-2xl max-w-3xl mx-auto">
        <span className="font-bold text-neutral-700">
          Full-Stack census web application using React, TypeScript, Next,js,
          Prisma, tRPC, TailwindCSS, PostgreSQL.
        </span>{" "}
        to manage and visualize the data of the Indonesian population in Germany
        in real-time.
      </p>
      <p className="text-neutral-600 text-base md:text-2xl font-sans max-w-3xl mx-auto">
        Implemented a CI/CD pipeline using GitHub Actions and Vercel for the
        Census web Application with automatic tests.
      </p>
      <a
        href="https://sensus.ppijerman.org"
        target="_blank"
        rel="noopener noreferrer"
        className=""
      >
        <div className="hover:text-blue-500 flex items-center gap-2 max-w-3xl mx-auto transition group">
          <p className="font-bold text-neutral-800 group-hover:text-blue-500 transition text-2xl">
            Access the project
          </p>
          <ArrowRight className="h-6 w-6" />
        </div>
      </a>
    </div>
  );
}
