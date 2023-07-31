import random
import time
import sqlite3


conn = sqlite3.connect('../raspberry_backend/db.sqlite3')
cursor = conn.cursor()
while True:
    random_data = random.randint(0, 100)
    print(f"Temperature: {random_data:.2f}°C")
    time.sleep(1)
    cursor.execute("INSERT INTO core_temperaturesensordata (temperature) VALUES (?)", (random_data,))
    conn.commit()

    