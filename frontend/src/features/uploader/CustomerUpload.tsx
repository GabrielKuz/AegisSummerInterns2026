import "./CustomerUpload.css";
import "../../styles/SupportTheme.css";

export function CustomerUpload() {
    return (
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
    );

}