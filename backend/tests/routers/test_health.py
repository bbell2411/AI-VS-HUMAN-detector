import pytest
def test_health_endpoint(client):
    """Test health endpoint returns correct response"""
    response = client.get("/api/v1/health")
    
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy", 
        "service": "ML Text Detector"
    }
    
def test_root_endpoint(client):
    """Test root endpoint works"""
    response = client.get("/")
    
    assert response.status_code == 200
    assert "ML Text Detector API" in response.json()["message"]