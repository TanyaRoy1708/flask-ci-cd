from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": os.getenv("DB_HOST", "mysql"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "database": os.getenv("DB_NAME", "flaskdb")
}


@app.route("/")
def health():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    conn.close()
    return "Flask + MySQL is running!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
