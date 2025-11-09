import psycopg2
import os

def test_connection():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='devopsdb', 
            user='postgres',
            password='password',
            port=5433
        )
        print("✅ Database connection successful!")
        
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print(f"📊 PostgreSQL version: {db_version[0]}")
        
        cur.close()
        conn.close()
        print("✅ Connection closed properly!")
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    test_connection()