import { useState } from "react";
import type { Session } from "@supabase/supabase-js";

export default function CreateLinkForm({ session }: { session: Session }) {
  const token = session?.access_token;
  const [url, setUrl] = useState("");
  const [slug, setSlug] = useState("");

  async function createLink() {
    const response = await fetch("http://localhost:8000/links", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        original_url: url,
        slug: slug,
      }),
    });

    if (response.ok) {
      const data = await response.json();
      alert(`Link created: ${data.slug}`);
    } else {
      const error = await response.json();
      console.log(error);
    }
  }

  return (
    <>
      <h1>Link Shortener</h1>

      <input
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter URL"
      />

      <input
        value={slug}
        onChange={(e) => setSlug(e.target.value)}
        placeholder="Enter slug"
      />

      <button onClick={createLink}>Shorten</button>
    </>
  );
}
