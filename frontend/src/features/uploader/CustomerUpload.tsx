import "./CustomerUpload.css";
import "../../styles/SupportTheme.css";
import { ThemeToggle } from "../../theme/ThemeToggle";
import {NavLink, Outlet} from "react-router-dom";

export function CustomerUpload() {
    

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
                            Customer Upload
                        </span>

                        <span className="support-section-name">
                            Provide files for support
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

            /*
            <main className="support-main">
                <div className="upload-content">
                    <p className="note">
                        <b>Note:</b> This link is temporary and will cease
                        working after (insert time here). Please ensure that
                        you upload your files by the given time remaining.
                    </p>

                    <div className="upload-box">
                        <p>Choose file(s) or drag and drop here</p>
                        <button className="browse-button">
                            Browse Files
                        </button>
                    </div>
                </div>
            </main>
            */
            <main className = "support-main">
                <Outlet />
            </main>
        </div>
    );

}