import markdown
from markupsafe import Markup
import os
from flask_migrate import Migrate
from models import *




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
        return f"<h3>Postgres успешно подключился!</h3><p>DB version: {version}</p>"
    except Exception as e:
        return f"<h3 style='color:red;'>DB connection error:</h3><pre>{e}</pre>"

if __name__ == '__main__':
   app.run(host='0.0.0.0')