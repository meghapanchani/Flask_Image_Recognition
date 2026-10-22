
"""Tests for the Flask application homepage."""


def test_homepage_loads(client):
    """Verify that the homepage loads successfully."""
    response = client.get("/")

    assert response.status_code == 200
