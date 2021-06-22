import requests

apiUrl = "https://api.openweathermap.org/data/2.5/weather?q="
filename = "test.txt"
chunk_size = 100

response = requests.get( apiUrl )

with open(filename, 'wb') as fd:
    for chunk in response.iter_content(chunk_size):
        fd.write(chunk)