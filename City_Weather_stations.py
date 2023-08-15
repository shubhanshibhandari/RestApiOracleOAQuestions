import requests
import json
kd=input()
url="https://jsonmock.hackerrank.com/api/weather/search?name="+kd+"&page="
x=requests.get(url+str(1))
y=json.loads(x.content)
total=y["total_pages"]
ans=[]
for page in range(1,total+1):
    res=requests.get(url+str(page))
    p=json.loads(res.content)
    for entry in p["data"]:
        e=""
        e=e+entry["name"]+","
        deg=entry["weather"].split(" ")[0]
        
        e=e+deg+","
        wind=entry["status"][0].split(" ")[1]
        wind=wind.split("K")[0]
        e=e+wind+","
        hum=entry["status"][1].split(" ")[1]
        hum=hum.split("%")[0]
        e=e+hum
        ans.append(e)
ans.sort
print(ans)