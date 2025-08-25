import { useLocation, useNavigate } from "react-router-dom";
import bin from "../assets/bin.png"
import { deletePred } from "../api"
import { useState } from "react";

export function SinglePrediction() {
    const navigate = useNavigate()
    const location = useLocation()
    const id = location.state?.index
    const prediction = location.state?.prediction
    const [loading, setLoading] = useState(false)
    const [err, setErr] = useState(null)

    if (!prediction) navigate("/history")

    const formatDate = (timestamp) => {
        return new Date(timestamp).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        })
    }

    const getResultColor = (result) => {
        return result === 'ai_generated' ? '#ff6b6b' : '#51cf66'
    }

    const getResultText = (result) => {
        return result === 'ai_generated' ? 'AI Generated' : 'Human Written'
    }

    const handleDelete = () => {
        const confirmed = window.confirm("Are you sure you want to delete this predictions")
        if (!confirmed) return
        setLoading(true)
        deletePred(id + 1)
        .then(()=>{
            alert("Prediction deleted successfully.")
            navigate("/history")
        })
        .catch((e)=>{
            setErr(true)
            console.log(e)
        })
        .finally(()=>{
            setLoading(false)
        })

    }
    if (loading) return <div className="loader-container"><h1 className="loader"></h1></div>
    if (err) return <p className="error">something went wrong</p>
    return (
        <div>
            <div style={{ position: "relative", top: -215 }}>
                <h1>Prediction {id + 1}</h1>
            </div>
            <button className="back-button" onClick={() => navigate('/')}>
                ←
            </button>
            <div className="predictionID-card">
                <div className="prediction-header">
                    <span
                        className="result-badge"
                        style={{ backgroundColor: getResultColor(prediction.result) }}
                    >
                        {getResultText(prediction.result)}
                    </span>
                    <span className="confidence">
                        {Math.round(prediction.confidence * 100)}% confident
                    </span>
                </div>

                <div className="predictionID-details">
                    <div className="detail-row">
                        <span>Text Length: </span>
                        <span>{prediction.text_length} characters</span>
                    </div>
                    <div className="detail-row">
                        <span>Processing Time: </span>
                        <span>{Math.round(prediction.processing_time_ms)}ms</span>
                    </div>
                    <div className="detail-row">
                        <span>Date: </span>
                        <span>{formatDate(prediction.timestamp)}</span>
                    </div>
                    <div style={{
                        width: "0.5px",
                        height: "10px",
                        transform: "scale(0.07)",
                        position: "absolute",
                        left: 390,
                        bottom: 50,
                        cursor: "pointer"
                    }}>
                        <img src={bin} onClick={handleDelete} />
                    </div>
                </div>
            </div>
        </div>
    )

}