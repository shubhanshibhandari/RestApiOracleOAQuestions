import requests
import json
city=input()
cost=int(input())
url="https://jsonmock.hackerrank.com/api/food_outlets?city="+city+"&page="
x=requests.get(url+str(4))
# print(x)
y=json.loads(x.content)
# print(y)
arr=[]
page=0
total=int(y["total"])
# print(total)

while(total) :
    page=page+1
    res=requests.get(url+str(page))
    p=json.loads(res.content)
    total=total-p["per_page"]
    for entry in p["data"]:
        if(entry["city"]==city and entry["estimated_cost"]<=cost):
            arr.append(entry["name"])
            
arr.sort()
print(arr)


