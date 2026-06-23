import { Link } from "react-router-dom";
import { mockTickets } from "../data/mockTickets";
import "./SupportTicketsPage.css";

export function SupportTicketsPage() {
  return (
    <section className="tickets-page">
      <header className="tickets-page-header">
        <div>
          <p>Customer support</p>
          <h1>Created tickets</h1>
          <span>
            Review previous requests and their current status.
          </span>
        </div>

        <Link
          to="/support/tickets/new"
          className="new-ticket-link"
        >
          Create ticket
        </Link>
      </header>

      <div className="tickets-table-wrapper">
        <table className="tickets-table">
          <thead>
            <tr>
              <th>Ticket</th>
              <th>Subject</th>
              <th>Category</th>
              <th>Status</th>
              <th>Last updated</th>
            </tr>
          </thead>

          <tbody>
            {mockTickets.map((ticket) => (
              <tr key={ticket.id}>
                <td>{ticket.id}</td>
                <td>{ticket.subject}</td>
                <td>{ticket.category}</td>
                <td>
                  <span
                    className={`ticket-status ticket-status-${ticket.status
                      .toLowerCase()
                      .replace(" ", "-")}`}
                  >
                    {ticket.status}
                  </span>
                </td>
                <td>{ticket.updatedAt}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}