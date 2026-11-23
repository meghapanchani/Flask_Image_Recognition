
import pytest
from app import app


@pytest.fixture
def client():
    original_testing = app.config["TESTING"]
    original_csrf = app.config["WTF_CSRF_ENABLED"]

    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False

    try:
        with app.test_client() as test_client:
            yield test_client
    finally:
        app.config["TESTING"] = original_testing
        app.config["WTF_CSRF_ENABLED"] = original_csrf
