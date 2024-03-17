from flask import Flask, jsonify
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
    return jsonify([dict(ix) for ix in prices])  # Use 'prices' variable here

if __name__ == '__main__':
    app.run(debug=True)
