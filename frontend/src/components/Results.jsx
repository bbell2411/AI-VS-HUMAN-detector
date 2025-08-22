import { useLocation, useNavigate } from 'react-router-dom';
export function Results() {
    const location = useLocation()
    const navigate = useNavigate()
    const prediction = location.state?.prediction

    if (!prediction) {
        navigate('/')
        return null
    }

    return (
        <div className='result-container'>
            {/* <img className="logo" src='/textguard.png' /> */}
            <h1 className='results'>Results</h1>
            <div className='results-col'>
            <p>Prediction: {prediction.result}</p>
            <p>Confidence: {prediction.confidence}%</p>
            <p>Processing Time: {prediction.processing_time_ms}</p>
            <p>{prediction.timestamp}</p>
            </div>
            
            <button className='back-button' onClick={() => navigate('/')}>Predict New Text</button>
        </div>
    )
}
