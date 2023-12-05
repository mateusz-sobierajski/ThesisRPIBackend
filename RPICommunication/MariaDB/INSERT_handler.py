import mariadb
import sys

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


def insert_aht10(splitvalues):
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
    cur.execute("INSERT INTO AHT10 (temperature, humidity) VALUES (?, ?)", (splitvalues[1], splitvalues[3]))
    conn.commit()
    print(f"Last Inserted ID: {cur.lastrowid}")
    conn.close()


conn.close()
