import { useState } from "react"
import { postPredict } from "../api";

export default function DashBoard() {
    const [text, setText] = useState("")
    const [contentType, setContentType] = useState("")
    const [result, setResult] = useState(null)

    const [loading, setLoading] = useState(false)
    const [err, setErr] = useState(null)

    const handleSubmit = (e) => {
        e.preventDefault()
        setLoading(true)
        postPredict(text, contentType)
            .then((prediction) => {
                setResult(prediction)
            })
            .catch((e) => {
                setErr(true)
                console.log(e)
            })
            .finally(() => {
                setLoading(false)
            })
    }
    if (loading) return <div className="loader-container"><h1 className="loader"></h1></div>
    if (err) return <p className="error">something went wrong</p>
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
                        <form onSubmit={handleSubmit}>
                            <textarea
                                className="text-input"
                                placeholder="Paste your text here..."
                                rows="10"
                                onChange={(e) => setText(e.target.value)}
                            />
                            <select
                                className="content-dropdown"
                                value={contentType}
                                onChange={(e) => setContentType(e.target.value)}>
                                <option value="">Select content type...</option>
                                <option value="academic_paper">Acedemic paper</option>
                                <option value="essay">Essay</option>
                                <option value="article">Article</option>
                                <option value="creative_writing">Creative writing</option>
                                <option value="news_article">News article</option>
                                <option value="social_media">Social Media</option>
                                <option value="product_review">Product review</option>
                                <option value="blog_post">Blog post</option>
                            </select>
                            <button
                                className='submit-button'
                                type="submit"
                                disabled={!contentType || !text.trim() || text.length < 10}
                            >Get Results</button>
                            {text.trim().length > 0 && text.trim().length < 10 && (
                                <p className="error-text">Please enter at least 10 characters</p>
                            )}
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}
// processing_time_ms: 186.01, timestamp: "2025-08-22T16:36:06.695614", text_length: 36 }
// ​
// confidence: 0.85
// ​
// processing_time_ms: 186.01
// ​
// result: "ai_generated"
// ​
// text_length: 36
// ​
// timestamp: "2025-08-22T16:36:06.695614"