import urllib.request as request
import csv, json


# connect to url
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(url) as response:

    # get list in the json data
    results = json.load(response)['result']['results']

csv_list = []
for element in results:

    # clean address and extract distric sting
    address = element['address']
    distric = address.replace(" ","")[3:6]

    # extract first img url 
    file = element['file']
    img_url = f' https://{file.split("https://")[1]}'


    # create a list and store whole data
    list = [element['stitle'], distric, element['longitude'], element['latitude'], img_url]
    csv_list.append(list)

# save csv_list in csv file
with open("attraction.csv","wt") as file:
    csv_file = csv.writer(file)
    csv_file.writerows(csv_list)


