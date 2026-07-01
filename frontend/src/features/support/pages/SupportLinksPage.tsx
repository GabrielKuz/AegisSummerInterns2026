import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
//import { mockLinks } from "../data/mockLinks";
import "../../../styles/SupportTheme.css";
import "./SupportLinksPage.css";
import { getDevToken } from "../../auth/devAuth";

/**
 * Converts a display status into a CSS-friendly modifier.
 *
 * Example:
 * "In Progress" becomes "in-progress".
 */
/*function getStatusClassName(status: string): string {
  return status
    .trim()
    .toLowerCase()
    .replace(/\s+/g, "-");
}*/
type SupportLink = {
    uuid: string;
    caseId: string;
    itarStatus: boolean;
    link: string;
    creator: string;
    usersWithAccess: string[];
    createdTimestamp: string;
    expired: boolean;
};

/**
 * Displays previously created support links in a responsive table.
 */
export function SupportLinksPage() {
  const [links, setLinks] = useState<SupportLink[]>([]);

  async function loadLinks() {
    const response = await fetch("/api/links", {headers: { Authorization: `Bearer ${getDevToken()}` }});
    if(!response.ok) {
      console.error("Failed to load support links.");
      return;
    }
    const data: SupportLink[] = await response.json();
    setLinks(data);
  }
  useEffect(() => {
    loadLinks();
  }, []);
  return (
    <section
      className="links-page"
      aria-labelledby="links-page-heading"
    >
      <header className="links-page-header">
        <div className="links-page-heading">
          <p className="links-page-eyebrow">
            Customer support
          </p>

          <h1 id="links-page-heading">
            Created links
          </h1>

          <p className="links-page-description">
            Review previous requests and their current status.
          </p>
        </div>

        <Link
          to="/support/links/new"
          className="new-link-link"
        >
          Create link
        </Link>
      </header>

      <div className="links-table-wrapper">
        <table className="links-table">

          <thead>
            <tr>
              {/*<th scope="col">Link</th>
              <th scope="col">Subject</th>
              <th scope="col">Category</th>
              <th scope="col">Status</th>
              <th scope="col">Last updated</th>
              */}
              <th scope="col">UUID</th>
              <th scope="col">Case ID</th>
              <th scope="col">ITAR</th>
              <th scope="col">Creator</th>
              <th scope="col">Created At</th>
            </tr>
          </thead>

          <tbody>
            {/*{links.map((supportLink) => {
              const statusClassName = getStatusClassName(
                supportLink.status,
              );

              return (
                <tr key={supportLink.id}>
                  <td>{supportLink.id}</td>
                  <td>{supportLink.subject}</td>
                  <td>{supportLink.category}</td>
                  <td>
                    <span
                      className={
                        `link - status` +
                        `link - status - ${statusClassName} `
                      }
                    >
                      {supportLink.status}
                    </span>
                  </td>
                  <td>{supportLink.updatedAt}</td>
                </tr>
                
              );
            })}*/}
            {links.map((supportLink) => (
              <tr key={supportLink.uuid}>
                  <td>{supportLink.uuid}</td>
                  <td>{supportLink.caseId}</td>
                  <td>{supportLink.itarStatus ? "Yes" : "No"}</td>
                  <td>{supportLink.creator}</td>
                  <td>{new Date(supportLink.createdTimestamp).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
