import time
from ingest_alert import insert_data

while True:
    insert_data()
    time.sleep(3)  # Add 1 row every 3 seconds
