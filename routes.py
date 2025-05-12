from flask import Flask, render_template, request, redirect, url_for
from models import db, Transaction

app = Flask(__name__)

# Home route - Display the form to add transactions
@app.route('/')
def index():
    return render_template('index.html')

# Route to view all transactions
@app.route('/transactions')
def transactions():
    all_transactions = Transaction.query.all()
    return render_template('transactions.html', transactions=all_transactions)

# Route to add a new transaction
@app.route('/add', methods=['POST'])
def add_transaction():
    if request.method == 'POST':
        transaction_type = request.form['transaction_type']
        customer_name = request.form['customer_name']
        details = request.form['details']
        amount_paid = float(request.form['amount_paid'])

        # Create a new transaction object
        new_transaction = Transaction(transaction_type=transaction_type, customer_name=customer_name,
                                      details=details, amount_paid=amount_paid)

        # Add the transaction to the database
        db.session.add(new_transaction)
        db.session.commit()

        return redirect(url_for('transactions'))

if __name__ == "__main__":
    app.run(debug=True)
