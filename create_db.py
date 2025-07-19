import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("solar.db")
c = conn.cursor()

# Create a table for solar data
c.execute('''
CREATE TABLE IF NOT EXISTS solar_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    voltage FLOAT,
    current FLOAT,
    temperature FLOAT,
    power FLOAT
)
''')

conn.commit()
conn.close()

print("✅ Database and table created successfully!")
