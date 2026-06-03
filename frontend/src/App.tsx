import { useEffect, useState } from "react";
import { supabase } from "./lib/supabase";
import CreateLinkForm from "./components/CreateLinkForm";
import Login from "./components/Login";
import type { Session } from "@supabase/supabase-js";

export default function App() {
  const [session, setSession] = useState<Session | null>(null);

  useEffect(() => {
    supabase.auth.getSession().then(({ data }) => {
      setSession(data.session);
    });

    const { data } = supabase.auth.onAuthStateChange((_, session) => {
      setSession(session);
    });

    return () => {
      data.subscription.unsubscribe();
    };
  }, []);

  if (!session) return <Login />;

  return <CreateLinkForm session={session} />;
}
