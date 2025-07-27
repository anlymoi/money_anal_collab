import markdown # type: ignore
from markupsafe import Markup # type: ignore

import os
from flask import Flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}"
    f"@{os.environ.get('POSTGRES_HOST')}:{os.environ.get('POSTGRES_PORT')}/{os.environ.get('POSTGRES_NAME')}"
)

db = SQLAlchemy(app)
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST"),
        port=os.environ.get("POSTGRES_PORT"),
        dbname=os.environ.get("POSTGRES_NAME"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
    )
    return conn

# @app.route('/')
# def hello_world():
#     return "<h1>UwU<h1><h2>проверяем, что всё работает и все счастливы няяя<h2>"


@app.route('/')
def hello_world():
    readme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'README.md'))
    try:
        with open(readme_path, encoding='utf-8') as f:
            lines = f.readlines()
        content = ''.join(lines)
        html = markdown.markdown(content)
        return Markup(html)
    except Exception as e:
        return f"<h3 style='color:red;'>ашипка при чтении README.md:</h3><pre>{e}</pre>"
    



@app.route('/dbtest')
def db_test():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return f"<h3>Postgres connection OK!</h3><p>DB version: {version}</p>"
    except Exception as e:
        return f"<h3 style='color:red;'>DB connection error:</h3><pre>{e}</pre>"

if __name__ == '__main__':
   app.run(host='0.0.0.0')