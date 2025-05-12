from flask import Flask, render_template, request, redirect, url_for
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
@app.route('/')
def index():
    return render_template('index.html')

# Route for displaying all transactions
@app.route('/transactions')
def transactions():
    all_transactions = Transaction.query.all()  # Get all transactions from the database
    return render_template('transactions.html', transactions=all_transactions)

# Route for adding a transaction
@app.route('/add', methods=['POST'])
def add_transaction():
    # Get data from the form
    customer_name = request.form.get('customer_name')
    transaction_type = request.form.get('transaction_type')
    details = request.form.get('details')
    amount_paid = float(request.form.get('amount_paid'))

    # Create a new Transaction
    new_transaction = Transaction(
        customer_name=customer_name,
        transaction_type=transaction_type,
        details=details,
        amount_paid=amount_paid
    )

    # Add to the database
    db.session.add(new_transaction)
    db.session.commit()

    # Redirect to the transactions page after adding
    return redirect(url_for('transactions'))

# Route for favicon (to avoid 404 error for favicon.ico)
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Empty response with no content (status 204)

if __name__ == "__main__":
    # Ensure the app context is properly set up
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    app.run(host='0.0.0.0', port=8081, debug=True)
