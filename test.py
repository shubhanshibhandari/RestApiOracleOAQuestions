import os 
import requests 
import json
url = "https://www.omdbapi.com/?apikey=138476a5&s=Wonder Woman&page="
x = requests.get("https://www.omdbapi.com/?apikey=138476a5&s=Wonder Woman&page=1")
data = json.loads(x.content)
totalResults = int(data['totalResults'])
page = 0
hmap = {}
arr = []
while(totalResults > 0) :
    page = page + 1
    res = requests.get(url+ str(page))
    data = json.loads(res.content)
    totalRecords = len(data['Search'])
    totalResults = totalResults - totalRecords
    print(totalResults)
    for record in data['Search'] :
        if record['Year'] in hmap :
            hmap[record['Year']] = hmap[record['Year']] + 1
        else :
            arr.append(record['Year'])
            hmap[record['Year']] = 1
arr.sort()
for y in arr :
    print(y,hmap[y])
