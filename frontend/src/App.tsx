import { BrowserRouter, Routes, Route } from "react-router-dom";
import useSession from "./auth/useSession";
import Login from "./components/Login";
import CreateLinkForm from "./components/CreateLinkForm";
import type { Session } from "@supabase/supabase-js";

function ProtectedRoute({
  session,
  children,
}: {
  session: Session;
  children: React.ReactNode;
}) {
  if (!session) {
    return <Login />;
  }
  return children;
}

export default function App() {
  const session = useSession();

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/"
          element={
            <ProtectedRoute session={session}>
              <CreateLinkForm session={session} />
            </ProtectedRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}
