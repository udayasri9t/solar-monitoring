import sqlite3
import random
from datetime import datetime
from sms_alert import send_sms_alert

def insert_data():
    conn = sqlite3.connect("solar.db")
    c = conn.cursor()

    # Simulated sensor readings
    voltage = round(random.uniform(180, 260), 2)
    current = round(random.uniform(1.0, 10.0), 2)
    temperature = round(random.uniform(40.0, 80.0), 2)
    power = round((voltage * current) / 1000, 2)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert into database
    c.execute("""
        INSERT INTO solar_data (timestamp, voltage, current, temperature, power)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, voltage, current, temperature, power))
    conn.commit()
    conn.close()

    print(f"📥 Inserted: {timestamp}, V={voltage}, A={current}, T={temperature}, P={power}")

    # ⚠️ Fault Detection Conditions
    if voltage < 190 or voltage > 250 or temperature > 65:
        alert = f"⚠️ Solar Fault!\nVoltage: {voltage}V\nTemp: {temperature}°C\nTime: {timestamp}"
        send_sms_alert(alert)
        print("📤 SMS sent!")

# Run once for test
insert_data()
