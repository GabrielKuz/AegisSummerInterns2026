import {
  BrowserRouter,
  Navigate,
  Route,
  Routes,
} from "react-router-dom";
import { LoginPage } from "./features/auth/LoginPage";
import { RequireDevUser } from "./features/auth/RequireDevUser";
import { SupportHomePage } from "./features/support/pages/SupportHomePage";
import { SupportTicketsPage } from "./features/support/pages/SupportTicketsPage";
import { CreateSupportTicketPage } from "./features/support/pages/CreateSupportTicketPage";
import { SupportLayout } from "./layouts/SupportLayout";
import { CustomerUpload } from "./features/uploader/CustomerUpload";
import { UploadDetails } from "./features/uploader/UploadDetails";
export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route
          path="/upload"
          element={
            <RequireDevUser>
              <CustomerUpload />
            </RequireDevUser>
          }
        >
          <Route
            index
            element={
              <div className="upload-content">
                <p className="note">
                  <b>Note:</b> This link is temporary and will cease working after
                  (insert time here). Please ensure that you upload your files by the
                  given time remaining.
                </p>

                <div className="upload-box">
                  <p>Choose file(s) or drag and drop here</p>
                  <button className="browse-button">
                    Browse Files
                  </button>
                </div>
              </div>
            }
          />          
          
        </Route>
        <Route path="/upload/details" element={<UploadDetails />} />
        <Route
          path="/support"
          element={
            <RequireDevUser>
              <SupportLayout />
            </RequireDevUser>
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
 