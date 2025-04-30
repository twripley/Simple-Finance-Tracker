from flask import Flask, render_template, request, redirect, url_for
from models import db, Transaction, Category
import pandas as pd
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finances.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            df = pd.read_excel(file)
            for _, row in df.iterrows():
                transaction = Transaction(date=row['Date'], amount=row['Amount'], description=row['Description'])
                db.session.add(transaction)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('upload.html')

@app.route('/reports')
def reports():
    transactions = Transaction.query.all()
    # Add logic to generate reports here
    return render_template('reports.html', transactions=transactions)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
