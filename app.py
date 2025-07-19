from flask import Flask, render_template, jsonify, send_file
import sqlite3
import pandas as pd
import io
import random
from datetime import datetime

app = Flask(__name__)

# Route to load dashboard
@app.route('/')
def index():
    return render_template('index.html')

# API route to send data as JSON
@app.route('/data')
def get_data():
    conn = sqlite3.connect("solar.db")
    c = conn.cursor()
    c.execute("SELECT timestamp, voltage, current, temperature, power FROM solar_data ORDER BY timestamp")
    rows = c.fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "timestamp": row[0],
            "voltage": row[1],
            "current": row[2],
            "temperature": row[3],
            "power": row[4]
        })
    return jsonify(data)

# Route to download CSV
@app.route('/download')
def download_csv():
    conn = sqlite3.connect("solar.db")
    df = pd.read_sql_query("SELECT * FROM solar_data", conn)
    conn.close()

    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name='solar_data.csv'
    )

# Run the app
if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

