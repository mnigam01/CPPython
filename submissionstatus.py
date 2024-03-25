

import requests
import time
url = "https://codeforces.com/api/user.status?handle=killua123&from=1&count=5"

while True:

    res = requests.get(url)
    obj = res.json()['result']
    i = obj[0]
    # print(i)
    if i['verdict']=='OK':
        print('solution passed!!!')
        break
    elif i['verdict']=='TESTING':
        print('Testing')
    else:
        print(i['verdict'])
        break
    time.sleep(2)
    



