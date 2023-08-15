import requests
import json
# low=int(input())
# high=int(input())
url="https://jsonmock.hackerrank.com/api/medical_records?page="
x=requests.get(url+str(1))
# print(x)
y=json.loads(x.content)
# print(y)
count=0
total=int(y["total_pages"])
# for page in range(1, total+1):
#     res=requests.get(url+str(page))
#     p=json.loads(res.content)
#     for entry in p["data"]:
#         x=entry["vitals"]["bloodPressureDiastole"]
#         if(x<=high and x>=low):
#             count=count+1
# print(count)

# find average pulse rate for doctor id and diaganois name
id=int(input())
name=input()
num=0
sum=0
for page in range(1,total+1):
    res=requests.get(url+str(page))
    p=json.loads(res.content)
    for entry in p["data"]:
        if(entry["doctor"]["id"]==id and entry["diagnosis"]["name"]==name):
            num=num+1
            sum=sum+int(entry["vitals"]["pulse"])
if(num==0) :
    avg=0           
else:
    avg= int(sum/num)
print(avg)

