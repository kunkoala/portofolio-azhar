"use client";
import Image from "next/image";
import React from "react";
import { Carousel, Card } from "@/components/ui/apple-cards-carousel";

// images
import sampleStock from "@/assets/stock-images/sample-stock.jpg";
import sensusStock from "@/assets/stock-images/sensus-stock.jpg";
import iconicWeb from "@/assets/stock-images/iconic-web.png";

import { DummyContent, SensusContent } from "@/app/(landing)/(projects)/carousel-contents";


export function AppleCardsCarouselDemo() {
  const cards = data.map((card, index) => (
    <Card key={card.title} card={card} index={index} layout={true} />
  ));

  return (
    <div className="w-full h-full">
      <Carousel items={cards} />
    </div>
  );
}



const data = [
  {
    category: "Full-stack Web Development",
    title: "Sensus PPI Jerman",
    src: sensusStock,
    content: <SensusContent />,
  },
  {
    category: "Front-end Web Development",
    title: "Website ICONIC 2024",
    src: iconicWeb,
    content: <DummyContent />,
  },
  {
    category: "Full-stack Web Development",
    title: "Personal Portofolio",
    src: sensusStock,
    content: <DummyContent />,
  },

  {
    category: "AI",
    title: "Voicebot St.Gallen",
    src: sensusStock,
    content: <DummyContent />,
  },
];
