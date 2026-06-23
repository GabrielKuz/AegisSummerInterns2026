import {
  BrowserRouter,
  Navigate,
  Route,
  Routes,
} from "react-router-dom";
import { LoginPage } from "./features/auth/LoginPage";
import { RequireSupportUser } from "./features/auth/RequireSupportUser";
import { SupportHomePage } from "./features/support/pages/SupportHomePage";
import { SupportTicketsPage } from "./features/support/pages/SupportTicketsPage";
import { CreateSupportTicketPage } from "./features/support/pages/CreateSupportTicketPage";
import { SupportLayout } from "./layouts/SupportLayout";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LoginPage />} />

        <Route
          path="/support"
          element={
            <RequireSupportUser>
              <SupportLayout />
            </RequireSupportUser>
          }
        >
          <Route index element={<SupportHomePage />} />

          <Route
            path="tickets"
            element={<SupportTicketsPage />}
          />

          <Route
            path="tickets/new"
            element={<CreateSupportTicketPage />}
          />
        </Route>

        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}