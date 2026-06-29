import "./CustomerUpload.css";
import "../../styles/SupportTheme.css";
import { useRef, type ChangeEvent } from "react";

export function CustomerUpload() {
    const fileInputRef = useRef<HTMLInputElement>(null);
    const handleBrowseClick = () => {
        fileInputRef.current?.click();
    };
    
    const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
        const files = event.target.files;
        if(files){
            console.log(files);
        }
    }

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
                    <button className="browse-button" onClick={handleBrowseClick}>
                        Browse Files
                    </button>

                    <input type="file" ref={fileInputRef} multiple style={{ display: "none" }} onChange={handleFileChange} />
                </div>
            </div>
        </main>
    );

}