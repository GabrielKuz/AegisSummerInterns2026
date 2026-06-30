import "./UploadDetails.css";
//import { useState } from "react";
import "../../styles/SupportTheme.css";
import { useParams } from "react-router-dom";

export function UploadDetails() {
    //const [mode, setMode] = useState<"USA" | "EU">("USA");
    const { uuid } = useParams();
    return (

        <main className="support-main">
            <div className="details-panel">
                <div className="details-row">
                    <div className="details-label">UUID</div>
                    <div className="details-value">
                        {uuid ? uuid : "No upload session found"}
                    </div>
                </div>
                <div className="details-row">
                    <div className="details-label">Is ITAR?</div>
                    <div className="details-value">No</div>
                </div>

                {/*</div><div className="details-row">
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
                */}
            </div>
        </main>
    );

}