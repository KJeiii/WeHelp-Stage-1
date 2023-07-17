import urllib.request as request
import csv, json

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
connect = request.urlopen(url)

print(connect)