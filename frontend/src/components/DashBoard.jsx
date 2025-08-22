export default function DashBoard() {
    return (
        <div>
            <h1 className="Header">
                TextGuard
            </h1>
            <div className="container">
                <div className="instructions">
                    <h3>
                        Paste your text content here:
                    </h3>
                    <div>
                        <form>
                            <textarea
                                className="text-input"
                                placeholder="Paste your text here..."
                                rows="10"
                            />
                            <select className="content-dropdown">
                                <option value="">Select content type...</option>
                                <option value="article">Article</option>
                                <option value="essay">Essay</option>
                                <option value="email">Email</option>
                                <option value="story">Story</option>
                                <option value="review">Review</option>
                                <option value="social">Social Media Post</option>
                                <option value="other">Other</option>
                            </select>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}