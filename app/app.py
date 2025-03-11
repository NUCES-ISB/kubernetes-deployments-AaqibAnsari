from flask import Flask
import psycopg2
import os

app = Flask(__name__)

db_host = os.getenv("DB_HOST", "postgres")
db_name = os.getenv("POSTGRES_DB", "flaskdb")
db_user = os.getenv("POSTGRES_USER", "flaskuser")
db_password = os.getenv("POSTGRES_PASSWORD", "postgresql")

@app.route('/')
def hello():
    try:
        conn = psycopg2.connect(
            dbname=db_name, user=db_user, password=db_password, host=db_host
        )
        return "Connected to PostgreSQL successfully!"
    except Exception as e:
        return f"Database connection error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
