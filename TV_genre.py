import requests
import json

url="https://jsonmock.hackerrank.com/api/tvseries?page="
x=requests.get(url+str(1))
y=json.loads(x.content)
total=y["total_pages"]
gen=input()
rate=0
name=""
for pages in range(1,total+1):
    res=requests.get(url+str(pages))
    p=json.loads(res.content)
    for entry in p["data"]:
        if(gen in entry["genre"]):
            if(entry["imdb_rating"]>rate):
                rate=entry["imdb_rating"]
                name=entry["name"]
            elif(entry["imdb_rating"]==rate):
                if(name>entry["name"]):
                    name=entry["name"]
                
print(name)