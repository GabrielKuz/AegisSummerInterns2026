import { Link } from "react-router-dom";
import "./SupportHomePage.css";

export function SupportHomePage() {
  return (
    <section className="support-home">
      <header className="support-page-heading">
        <p>Customer support</p>
        <h1>How can we help?</h1>
        <span>
          Review an existing support request or create a new ticket.
        </span>
      </header>

      <div className="support-home-actions">
        <Link
          to="/support/tickets"
          className="support-home-card"
        >
          <span className="support-home-card-number">01</span>

          <div>
            <h2>Access created tickets</h2>
            <p>
              Review ticket status, previous requests, and recent
              support activity.
            </p>
          </div>

          <span className="support-home-card-link">
            View tickets →
          </span>
        </Link>

        <Link
          to="/support/tickets/new"
          className="support-home-card"
        >
          <span className="support-home-card-number">02</span>

          <div>
            <h2>Create a new ticket</h2>
            <p>
              Submit a new issue with a category, description, and
              supporting information.
            </p>
          </div>

          <span className="support-home-card-link">
            Create ticket →
          </span>
        </Link>
      </div>
    </section>
  );
}