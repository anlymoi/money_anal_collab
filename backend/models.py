from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import Mapped, mapped_column
import psycopg2
import os

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}"
    f"@{os.environ.get('POSTGRES_HOST')}:{os.environ.get('POSTGRES_PORT')}/{os.environ.get('POSTGRES_NAME')}"
)

print(app.config['SQLALCHEMY_DATABASE_URI'])

db.init_app(app)
migrate = Migrate(app, db)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST"),
        port=os.environ.get("POSTGRES_PORT"),
        dbname=os.environ.get("POSTGRES_NAME"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
    )
    return conn




class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    # email: Mapped[str]

class Receipt(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    # user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # source_type = Column(String)
    # original_filename = Column(String)
    # uploaded_at = Column(DateTime, default=datetime.utcnow)
    # total_amount = Column(Numeric(12,2))
    # currency = Column(String(3))
    # vendor_name = Column(String)
    # raw_blob_path = Column(String)
    # parsed = Column(Boolean, default=False)
    # lines = relationship("ReceiptLine", back_populates="receipt")




with app.app_context():
    db.create_all()