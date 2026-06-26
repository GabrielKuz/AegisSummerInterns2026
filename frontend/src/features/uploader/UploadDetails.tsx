import "./UploadDetails.css";
import {NavLink} from "react-router-dom";
import { useState } from "react";
import "../../styles/SupportTheme.css";
import { ThemeToggle } from "../../theme/ThemeToggle";

export function UploadDetails() {
    const[mode, setMode] = useState<"USA" | "EU">("USA");
    return (
        <div className="support-layout">
            <header className="support-header">
                <div className="support-brand">
                    <img
                        src="/images/aegis-logo.svg"
                        alt="Aegis Software"
                        className="support-logo"
                    />
                    <div className="support-header-divider" />
                    <div className="support-title">
                        <span className="support-product-name">
                            Link Details
                        </span>

                        <span className="support-section-name">
                            View link information
                        </span>
                    </div>
                </div>
                <div className="support-header-actions">
                    <ThemeToggle />
                </div>
            </header>

            <aside className="support-sidebar">
                <nav>
                    <NavLink
                        to="/upload"
                        end
                        className={({ isActive }) =>
                            isActive
                                ? "support-nav-link support-nav-link-active"
                                : "support-nav-link"
                        }
                    >
                        Upload Files
                    </NavLink>
                    
                    <NavLink
                        to="/upload/details"
                        className={({ isActive }) =>
                            isActive
                                ? "support-nav-link support-nav-link-active"
                                : "support-nav-link"
                        }
                    > 
                        Upload Details
                    </NavLink>
                </nav>
            </aside>


            <main className="support-main">
               
                <div className="details-panel">

       
                    <div className="details-row">
                        <div className="details-label">Ticket ID</div>
                        <div className="details-value">AES12345</div>
                    </div>
                    <div className="details-row">
                        <div className="details-label">Is ITAR?</div>
                        <div className="details-value">No</div>
                    </div>

                   
                    <div className="details-row">
                        <div className="details-label">Days Until Expiration Date</div>
                        <div className="details-value">30</div>
                    </div>

                    <div className="details-row">
                            <div className="details-label">Server Location</div>

                            <div className="details-toggle">
                                <button
                                    className={mode === "USA" ? "toggle-btn active" : "toggle-btn"}
                                    onClick={() => setMode("USA")}
                                >
                                    USA
                                </button>

                                <button
                                    className={mode === "EU" ? "toggle-btn active" : "toggle-btn"}
                                    onClick={() => setMode("EU")}
                                >
                                    EU
                            </button>
                         </div>
                    </div>
                </div>
            </main>
        </div>
    );

}