import { Link } from "react-router-dom";

export const NotFound = () => {
    return (
        <div style={{ padding: "2rem", textAlign: "center" }}>
            <h1>404 - Page Not Found</h1>
            <p>Oops! The page you are looking for does not exist.</p>
            <Link to="/" style={{ color: "#0077cc", textDecoration: "underline" }}>
                Go back to Homepage
            </Link>
        </div>
    )
}