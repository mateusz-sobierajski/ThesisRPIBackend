import mariadb
import sys
import json

def get_temp():
    data: list = []
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
    cur.execute("SELECT temperature FROM AHT10 ORDER BY id DESC LIMIT 10")

    for (temperature) in cur:
        item = {"temperature": temperature}
        data.append(item)
        #data.append(temperature)
        #print(f"id: {id}, temperature: {temperature}, humidity: {humidity}, timestamp: {timestamp}")
    print("data:\n", data)
    #jsonData = json.dumps(data, default=str)
    jsonData = json.dumps(data)
    conn.commit()
    conn.close()
    data.clear()
    print("jsonData:\n", jsonData)
    return jsonData
