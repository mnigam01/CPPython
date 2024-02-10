import requests
# import json
import time


a = []

with open('C://Users//mridu//Python_Code//jsons//input.txt', 'r') as f:
    lines = f.readlines()
    
    for line in lines:
        handle = line.strip()
        a.append(handle)
print(a)


#         url = f'https://codeforces.com/api/user.status?handle={handle}'

#         response = requests.get(url)

#         if response.status_code == 200:
#             data = response.json()
            
#             with open(f'C://Users//mridu//Python_Code//jsons//{handle}.json', 'w', encoding="utf-8") as file:
#                 json.dump(data, file)
            
            
#         time.sleep(0.3)


