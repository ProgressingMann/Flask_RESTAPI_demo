import pytest
from factory import create_app
from settings import TestConfig

# @pytest.fixture
# def client():
#     # Set TESTING to True when testing.
#     ap.config['TESTING'] = True
#     # Create the in built test client using the flask app configured for testing
#     with ap.test_client() as client:
#         with ap.app_context():
#             # The below yield with do testing
#             yield client 

@pytest.fixture
def client():
    # Set TESTING to True when testing.
    app = create_app(TestConfig)
    yield app.test_client()
