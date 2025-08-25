import { useEffect, useState } from "react";
import { getAllPredict } from "../api";
import { useNavigate } from "react-router-dom";

export function History() {
  const [predictions, setPred] = useState([])
  const [singlePred, setSinglePred] = useState([])
  const navigate = useNavigate()

  const [loading, setLoading] = useState(false)
  const [err, setErr] = useState(null)

  useEffect(() => {
    setLoading(true)
    getAllPredict()
      .then((res) => {
        setPred(res)
      })
      .catch((e) => {
        setErr(true)
        console.log(e)
      })
      .finally(() => {
        setLoading(false)
      })
  }, [])


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

  if (loading) return <div className="loader-container"><h1 className="loader"></h1></div>
  if (err) return <p className="error">something went wrong</p>

  return (
    <div className="history-container">
      <div className="history-header">
        <h1>Prediction History</h1>
        <button className="back-button" onClick={() => navigate('/')}>
          ←
        </button>
      </div>

      {predictions.length === 0 ? (
        <div className="empty-state">
          <p>No predictions yet. Start by analyzing some text!</p>
        </div>
      ) : (
        <div className="predictions-grid">
          {predictions.map((prediction, index) => (
            <div key={index}
            className="prediction-card"
            onClick={() => {
              navigate(`/history/${index}`, { state: { prediction, index } })
            }}>
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

              <div className="prediction-details">
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
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

