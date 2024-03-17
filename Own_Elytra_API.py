from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
    
def get_db_connection():
    conn = sqlite3.connect('elytra_prices.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def hello_world():
    return 'Hello, wow'

@app.route('/prices', methods=['GET'])
def prices():
    conn = get_db_connection()
    prices = conn.execute('SELECT * FROM elytra_prices').fetchall()  # Fetch data from elytra_prices table
    conn.close()
    return render_template('prices.html', prices=[dict(ix) for ix in prices])

if __name__ == '__main__':
    app.run(debug=True)
