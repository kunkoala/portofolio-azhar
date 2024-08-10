import { getByQuery } from "@/lib/api";

export default async function Home() {
  const data = await getByQuery("/project_settings/hello");

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1>This is a message</h1>
      <p>The message: {JSON.stringify(data)}</p>
    </main>
  );
}