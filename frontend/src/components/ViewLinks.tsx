import { useState } from "react";
import type { Session } from "@supabase/supabase-js";

type LinkResponse = {
  original_url: string;
  slug: string;
  owner_id: string;
  created_at: string;
};

export default function ViewLinks({ session }: { session: Session | null }) {
  const [links, setLinks] = useState<LinkResponse[] | null>(null);

  const token = session?.access_token;
  const apiUrl = import.meta.env.VITE_API_URL;

  async function fetchLinks() {
    const response = await fetch(`${apiUrl}/links`, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (response.ok) {
      const data = await response.json();
      setLinks(data);
    } else {
      const error = await response.json();
      console.log(error);
    }
  }

  return (
    <>
      <button onClick={fetchLinks}>Fetch Links</button>
      <ul>
        {links ? links.map((link) => (
          <li key={link.slug}>
            <p>
              {link.slug} -&gt; {link.original_url}
            </p>
          </li>
        )) :
          <p>
            Links not found.
          </p>
        }
      </ul>
    </>
  );
}
