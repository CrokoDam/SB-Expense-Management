from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)

# Database configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define Transaction model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_type = db.Column(db.String(50), nullable=False)  # Grocery or Lodge
    customer_name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(255), nullable=False)  # Product or Room details
    amount_paid = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, default=db.func.current_timestamp())

# Home route
def index():
    return render_template('index.html')

if __name__ == "__main__":
    db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
