import Conv as C
import datetime as DT
import Check as Ck


if Ck.response['cod'] != '404':
    longitude = round(Ck.response["coord"]["lon"], 2)
    latitude = round(Ck.response["coord"]["lat"], 2)
    stat = Ck.response["weather"][0]["main"]
    description = Ck.response["weather"][0]["description"]
    temp_kelvin = round(Ck.response["main"]["temp"])
    temp_min_kelvin = round(Ck.response["main"]["temp_min"])
    temp_max_kelvin = round(Ck.response["main"]["temp_max"])
    feels_like_kelvin = round(Ck.response["main"]["feels_like"])
    temp_celcius = round(C.kelvin_to_celcius(Ck.response["main"]["temp"]), 2)
    temp_min_celcius = round(C.kelvin_to_celcius(
        Ck.response["main"]["temp_min"]), 2)
    temp_max_celcius = round(C.kelvin_to_celcius(
        Ck.response["main"]["temp_max"]), 2)
    feels_like_celcius = round(C.kelvin_to_celcius(
        Ck.response["main"]["feels_like"]), 2)
    temp_fahrenheit = round(
        C.kelvin_to_fahrenheit(Ck.response["main"]["temp"]), 2)
    temp_min_fahrenheit = round(
        C.kelvin_to_fahrenheit(Ck.response["main"]["temp_min"]), 2)
    temp_max_fahrenheit = round(
        C.kelvin_to_fahrenheit(Ck.response["main"]["temp_max"]), 2)
    feels_like_fahrenheit = round(
        C.kelvin_to_fahrenheit(Ck.response["main"]["feels_like"]), 2)
    humidity = Ck.response["main"]["humidity"]
    wind_speed = round(Ck.response["wind"]["speed"], 2)
    sunrise_time = DT.datetime.utcfromtimestamp(
        Ck.response["sys"]["sunrise"] + Ck.response["timezone"]).strftime("%H:%M:%S")
    sunset_time = DT.datetime.utcfromtimestamp(
        Ck.response["sys"]["sunset"] + Ck.response["timezone"]).time()
