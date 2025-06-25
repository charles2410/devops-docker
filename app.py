import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    try:
        print("🔥 Flask app iniciada con nueva versión")
        print("MYSQL_HOST =", os.getenv("MYSQL_HOST"))
        print("MYSQL_USER =", os.getenv("MYSQL_USER"))
        print("MYSQL_PASSWORD =", os.getenv("MYSQL_PASSWORD"))
        print("MYSQL_DATABASE =", os.getenv("MYSQL_DATABASE"))

        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
        )
        return conn
    except mysql.connector.Error as err:
        print("Error al conectar a MySQL:", err)
        return None

@app.route("/")
def index():
    conn = get_db_connection()
    if not conn:
        return "No se pudo conectar a la base de datos."
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    conn.close()
    return f"Conectado a la base de datos: {db_name[0]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

