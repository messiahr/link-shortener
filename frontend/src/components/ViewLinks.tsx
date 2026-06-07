import type { Session } from "@supabase/supabase-js";

export default function ViewLinks({ session }: { session: Session | null }) {
  const token = session?.access_token;

  const apiUrl = import.meta.env.VITE_API_URL;

  async function fetchLinks() {
    const response = await fetch(`${apiUrl}/links`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    const data = await response.json();
    console.log(data);
  }

  return (
    <div>
      <button onClick={fetchLinks}>Fetch Links</button>
    </div>
  );
}
