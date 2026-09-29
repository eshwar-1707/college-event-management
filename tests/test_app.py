import pytest
import os
import sys
import tempfile

# Add project root directory to sys.path for direct pytest invocation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import app as event_app

@pytest.fixture
def client():
    """Create a temporary database and configure the Flask test client."""
    db_fd, db_path = tempfile.mkstemp(suffix='.db')
    event_app.DATABASE = db_path
    event_app.app.config['TESTING'] = True

    with event_app.app.test_client() as client:
        # Initialize schema and seed data in test database
        event_app.init_db()
        yield client

    # Cleanup temporary test database
    os.close(db_fd)
    if os.path.exists(db_path):
        os.remove(db_path)

def test_app_starts(client):
    """Test 1: Verify the application starts successfully and test client is created."""
    assert event_app.app is not None
    assert event_app.app.config['TESTING'] is True

def test_home_page_returns_200(client):
    """Test 2: Verify the home page returns HTTP 200 and loads HTML content."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'College Event Management System' in response.data

def test_add_event(client):
    """Test 3: Verify a new event can be added through the /add route."""
    new_event_data = {
        'name': 'Robotics Workshop',
        'date': '2026-10-20',
        'venue': 'Lab 4',
        'description': 'Hands-on training on autonomous robotics and sensors.'
    }
    # Submit POST request to add event
    response = client.post('/add', data=new_event_data, follow_redirects=True)
    assert response.status_code == 200
    assert b'Robotics Workshop' in response.data
    assert b'Lab 4' in response.data

def test_delete_event(client):
    """Test 4: Verify an event can be deleted through the /delete/<id> route."""
    # First, add a specific event to delete
    sample_data = {
        'name': 'Temporary Event To Delete',
        'date': '2026-11-11',
        'venue': 'Room 101',
        'description': 'This event will be deleted.'
    }
    client.post('/add', data=sample_data, follow_redirects=True)

    # Check that it exists in the database
    conn = event_app.get_db_connection()
    event = conn.execute(
        "SELECT id FROM events WHERE name = 'Temporary Event To Delete'"
    ).fetchone()
    conn.close()
    assert event is not None
    event_id = event['id']

    # Delete the event
    response = client.post(f'/delete/{event_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Temporary Event To Delete' not in response.data

    # Verify event no longer exists in DB
    conn = event_app.get_db_connection()
    deleted_event = conn.execute(
        "SELECT * FROM events WHERE id = ?", (event_id,)
    ).fetchone()
    conn.close()
    assert deleted_event is None
