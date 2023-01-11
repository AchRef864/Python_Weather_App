import Check as Ck
import json

if Ck.response['cod'] != '404':
    json = json.dumps(Ck.response)

    f = open("weather.json", "w")

    f.write(json)

    f.close()
