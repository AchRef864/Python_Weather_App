import GetInfo as GI
import Check as Ck
import DumpInfo as DI

# make account at https://openweathermap.org or use my key : a14f1bb6b9103f4e98a0e84d5a389778

if Ck.response['cod'] == '404':
    print("No City Found")
else:
    print(f"Latitude: {GI.latitude}°")
    print(f"Longitude: {GI.longitude}°")
    print(f"Weather: {GI.stat}")
    print(f"Description: {GI.description}")
    print(f"Humidity: {GI.humidity}")
    print(f"Wind : {GI.wind_speed}m/s")
    print(f"Temperature: {GI.temp_celcius}°C")
    print(f"Feels Like: {GI.feels_like_celcius}°C")
    print(f"Minimum Temperature: {GI.temp_min_celcius}°C")
    print(f"Max Temperature: {GI.temp_max_celcius}°C")
    print(f"Sunrise: {GI.sunrise_time}")
    print(f"Sunrise: {GI.sunset_time}")
