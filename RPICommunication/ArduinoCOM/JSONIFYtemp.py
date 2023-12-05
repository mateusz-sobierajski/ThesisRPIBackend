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
    for (temperature, humidity) in cur:
        print(f"id: {id}, temperature: {temperature}, humidity: {humidity}")
    conn.commit()
    conn.close()

