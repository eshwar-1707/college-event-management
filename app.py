from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Configure database path (allows override in tests)
DATABASE = os.environ.get('DATABASE_PATH', 'events.db')

def get_db_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database schema and seeds initial sample events if empty."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            venue TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    
    # Check if table is empty, and insert sample events
    cursor.execute('SELECT COUNT(*) FROM events')
    count = cursor.fetchone()[0]
    if count == 0:
        sample_events = [
            (
                'Annual Tech Symposium',
                '2026-10-15',
                'Auditorium A',
                'National level technical paper presentation and coding hackathon.'
            ),
            (
                'Cultural Fest - Waves',
                '2026-11-05',
                'Open Air Theatre',
                'Inter-college music, dance, drama, and artistic competitions.'
            ),
            (
                'Campus Placement Drive',
                '2026-12-01',
                'Seminar Hall 2',
                'Recruitment drive featuring leading IT and core engineering companies.'
            )
        ]
        cursor.executemany('''
            INSERT INTO events (name, date, venue, description)
            VALUES (?, ?, ?, ?)
        ''', sample_events)
        conn.commit()
    conn.close()

@app.route('/')
def index():
    """Route to view all college events."""
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', events=events)

@app.route('/add', methods=['POST'])
def add_event():
    """Route to add a new event."""
    name = request.form.get('name')
    date = request.form.get('date')
    venue = request.form.get('venue')
    description = request.form.get('description')

    if name and date and venue and description:
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO events (name, date, venue, description)
            VALUES (?, ?, ?, ?)
        ''', (name, date, venue, description))
        conn.commit()
        conn.close()

    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete_event(id):
    """Route to delete an event by ID."""
    conn = get_db_connection()
    conn.execute('DELETE FROM events WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    # Runs on port 5000, accessible externally within Docker or local host
    app.run(host='0.0.0.0', port=5000, debug=True)
