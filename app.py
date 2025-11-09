from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

# Database configuration
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'devopsdb')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASSWORD', 'password')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST, 
        database=DB_NAME, 
        user=DB_USER, 
        password=DB_PASS
    )
    return conn

@app.route('/')
def home():
    return "Hello, DevOps World!"


@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})


@app.route('/users')
def get_users():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, username FROM users')
        users = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([{"id": u[0], "username": u[1]} for u in users])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

