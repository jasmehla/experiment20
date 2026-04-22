from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

host = os.getenv("DB_HOST", "db")
user = os.getenv("DB_USER", "test_user")
password = os.getenv("DB_PASSWORD", "test_pass")
database = os.getenv("DB_NAME", "test_db")

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def home():
    return "Backend Running with MySQL!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)