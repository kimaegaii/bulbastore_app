from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
    
def get_db_connection():
    conn = sqlite3.connect('elytra_prices.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/prices', methods=['GET'])
def prices():
    conn = get_db_connection()
    prices = conn.execute('SELECT * FROM prices').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in elytra_prices])

if __name__ == '__main__':
    app.run(debug=True)
