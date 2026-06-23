import { useState } from "react";
import type { FormEvent } from "react";
import { useNavigate } from "react-router-dom";
import "./CreateSupportTicketPage.css";

type TicketForm = {
  subject: string;
  category: string;
  description: string;
  urgency: string;
};

const initialForm: TicketForm = {
  subject: "",
  category: "",
  description: "",
  urgency: "Normal",
};

export function CreateSupportTicketPage() {
  const navigate = useNavigate();
  const [form, setForm] = useState<TicketForm>(initialForm);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    if (
      !form.subject.trim() ||
      !form.category ||
      !form.description.trim()
    ) {
      setError(
        "Subject, category, and description are required.",
      );
      return;
    }

    setError(null);

    // Temporary frontend-only behavior.
    console.log("Ticket submitted:", form);

    navigate("/support/tickets");
  };

  return (
    <section className="create-ticket-page">
      <header>
        <p>Customer support</p>
        <h1>Create a new ticket</h1>
        <span>
          Tell the support team what happened and what assistance
          you need.
        </span>
      </header>

      <form className="ticket-form" onSubmit={handleSubmit}>
        {error && (
          <div className="ticket-form-error" role="alert">
            {error}
          </div>
        )}

        <label>
          <span>Subject</span>
          <input
            type="text"
            value={form.subject}
            onChange={(event) =>
              setForm({
                ...form,
                subject: event.target.value,
              })
            }
          />
        </label>

        <label>
          <span>Category</span>
          <select
            value={form.category}
            onChange={(event) =>
              setForm({
                ...form,
                category: event.target.value,
              })
            }
          >
            <option value="">Select a category</option>
            <option value="Access">Access</option>
            <option value="File upload">File upload</option>
            <option value="Expiration">Expiration</option>
            <option value="Account">Account</option>
            <option value="Other">Other</option>
          </select>
        </label>

        <label>
          <span>Urgency</span>
          <select
            value={form.urgency}
            onChange={(event) =>
              setForm({
                ...form,
                urgency: event.target.value,
              })
            }
          >
            <option value="Low">Low</option>
            <option value="Normal">Normal</option>
            <option value="High">High</option>
          </select>
        </label>

        <label className="ticket-description-field">
          <span>Description</span>
          <textarea
            rows={8}
            value={form.description}
            onChange={(event) =>
              setForm({
                ...form,
                description: event.target.value,
              })
            }
          />
        </label>

        <div className="ticket-form-actions">
          <button
            type="button"
            className="ticket-cancel-button"
            onClick={() => navigate("/support")}
          >
            Cancel
          </button>

          <button type="submit" className="ticket-submit-button">
            Submit ticket
          </button>
        </div>
      </form>
    </section>
  );
}