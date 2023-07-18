import urllib.request as request
import csv, json


# connect to url
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(url) as response:

    # get list in the json data
    results = json.load(response)['result']['results']

# ---- build attraction.csv ----
attraction_csv_list = []
for element in results:

    # clean address and extract distric sting
    address = element['address']
    distric = address.replace(" ","")[3:6]

    # extract first img url 
    file = element['file']
    img_url = f' https://{file.split("https://")[1]}'


    # create a list and store whole data
    list = [element['stitle'], distric, element['longitude'], element['latitude'], img_url]
    attraction_csv_list.append(list)

# save attraction_csv_list in csv file
with open("attraction.csv","wt") as file:
    csv_file = csv.writer(file)
    csv_file.writerows(attraction_csv_list)


# ---- build mrt.csv ----
# find all MRT in the JSON data and store in a list
mrt_list = [ element['MRT'] for element in results ]

# remove duplicate
unique_mrt_list = []
for mrt in mrt_list:

    # if mrt is None, do not append
    if mrt == None:
        continue

    if mrt not in unique_mrt_list:
        unique_mrt_list.append(mrt)

# match each mrt in JSON with unique_mrt_list and build mrt csv_list
mrt_csv_lsit = []
for mrt in unique_mrt_list:
    mrt_attraction_list = [mrt]
    for element in results:
        if element['MRT'] == mrt:
            mrt_attraction_list.append(element['stitle'])
    mrt_csv_lsit.append(mrt_attraction_list)

# save mrt_csv_list in csv file
with open("mrt.csv",'wt') as file:
    csv_file = csv.writer(file)
    csv_file.writerows(mrt_csv_lsit)


# confirm whether code loses attraction,
# there is a None in MRT data, mrt.csv does not contain this attraction.
length = [len(element)-1 for element in mrt_csv_lsit]

attraction_amount = 0
for value in length:
    attraction_amount += value

print(f'Total amount of attraction in Tapei government web : {len(results)}')
print(f'Total amount of attraction in mrt.csv : {attraction_amount},\nthere is {len(results) - attraction_amount} null data in the web.')





