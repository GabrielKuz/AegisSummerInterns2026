import "./CustomerUpload.css";

export function CustomerUpload() {
    /*return(
        <div className = "support-layout">
            <header className = "support-header">
                <div className = "support-brand">
                    <img src = "/images/aegis-logo.svg" alt = "Aegis Software" className="support-logo" />
                <div className="divide"></div>

                    <span className = "support-product-name"> 
                        Customer Upload
                    </span>
                    <span className="support-section-name">
                        Provide files for support
                    </span>
                </div>
            </header>

        
        <div className = "central-container">
            {/*The sidebar*//*}
            <aside className = "support-sidebar">
                <div className = "sidebar-item active">
                    <h2>Upload Files</h2>
                </div>
            </aside>
        
            <main className = "main-content">
                <p className = "note">
                    <b>Note:</b> This link is temporary and will cease working after (insert time here). Please ensure that you upload your files by the given time remaining.
                </p>
                <div className = "upload-box">
                    <p>Choose file(s) or drag and drop here</p>
                    <button className = "browse-button">Browse Files </button>
                </div>
            </main>
        </div>
        </div>
    );
    */

    return (
        <div className="support-layout">
            <header className="support-header">
                <div className="support-brand">
                    <img
                        src="/images/aegis-logo.svg"
                        alt="Aegis Software"
                        className="support-logo"
                    />

                    <div className="support-title">
                        <span className="support-product-name">
                            Customer Upload
                        </span>

                        <span className="support-section-name">
                            Provide files for support
                        </span>
                    </div>
                </div>
            </header>

            <aside className="support-sidebar">
                <nav>
                    <div className="support-nav-link support-nav-link-active">
                        Upload Files
                    </div>
                    <div className="support-nav-link support nav-link-active">
                        View Link Details
                    </div>
                </nav>
            </aside>

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
        </div>
    );

}