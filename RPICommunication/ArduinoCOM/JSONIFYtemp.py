import mariadb
import sys


def jsonifyTemp():
    try:
        conn = mariadb.connect(
            host="localhost",
            port=3306,
            user="rpi4",
            password="raspberrydb",
            database="pidatabase")
        print("MariaDB Platform Connected Successfully!")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    cur = conn.cursor()
    cur.execute("SELECT * FROM AHT10 ORDER BY id DESC LIMIT 10")
    for (id, temperature, humidity, timestamp) in cur:
        print(f"id: {id}, temperature: {temperature}, humidity: {humidity}, timestamp: {timestamp}")
    conn.commit()
    conn.close()

