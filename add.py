import sys
import requests
import mysql.connector 

def run(q, date):
    query = q
    response = requests.get('https://api-adresse.data.gouv.fr/search/?q={}'.format(query))
    data = response.json()
    name = data["features"][0]["properties"]["city"]
    id_city = data["features"][0]["properties"]["id"]
    coords = data["features"][0]["geometry"]["coordinates"]
    lat = coords[1]
    lng = coords[0]
    city = {"id":id_city, "name": name, "lat": lat, "lng": lng, "date":date}

    # Read bdd file config
    with open('config_bdd.txt') as f:
        datas = f.readlines()
    count = -1
    config = []
    for line in datas:
        count += 1
        config.append( "{}".format(line.strip()) )

    conn = mysql.connector.connect(host=config[0],user=config[1],password=config[2], database=config[1])
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO cities (id, name, lat, lng, date) VALUES(%(id)s, %(name)s, %(lat)s, %(lng)s, %(date)s)""", city)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    q = sys.argv[1]
    date = sys.argv[2]
    run(q, date)
