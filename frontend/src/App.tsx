import { BrowserRouter, Navigate, Routes, Route } from "react-router-dom";
import useSession from "./auth/useSession";
import Login from "./components/Login";
import CreateLinkForm from "./components/CreateLinkForm";
import ViewLinks from "./components/ViewLinks";
import type { Session } from "@supabase/supabase-js";

function ProtectedRoute({
  session,
  children,
}: {
  session: Session | null;
  children: React.ReactNode;
}) {
  if (!session) {
    return <Navigate to="/login" replace />;
  }
  return children;
}

export default function App() {
  const session = useSession();

  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/login"
          element={session ? <Navigate to="/" replace /> : <Login />}
        />
        <Route
          path="/"
          element={
            <ProtectedRoute session={session}>
              <CreateLinkForm session={session!} />
              <ViewLinks session={session!} />
            </ProtectedRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}
