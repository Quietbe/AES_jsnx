import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import requests

cookies = {
    'UM_distinctid': '18a871d0c4c739-0c7841a65dbc69-26031d51-1fa400-18a871d0c4d92a',
    'Hm_lvt_1521e0fb49013136e79181f2888214a7': '1694483944',
    'Hm_lpvt_1521e0fb49013136e79181f2888214a7': '1694484817',
    'JSESSIONID': 'FFF97B24C36E8BC7D1AA1CED93F36019',
    '_ACCOUNT_': 'YjVjNDk0NDU3YTg3NDUxNWI3YzUyZGQyZDFiYTUyZDAlNDAlNDBtb2JpbGU6MTY5NTY5OTU5MzczMDpiMmNhZjgxMDcyMTU4OGU0NmU4ZDUyYzUyZWY2ZDJjNw',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Auth-Plus': '',
    'Connection': 'keep-alive',
    # 'Cookie': 'UM_distinctid=18a871d0c4c739-0c7841a65dbc69-26031d51-1fa400-18a871d0c4d92a; Hm_lvt_1521e0fb49013136e79181f2888214a7=1694483944; Hm_lpvt_1521e0fb49013136e79181f2888214a7=1694484817; JSESSIONID=FFF97B24C36E8BC7D1AA1CED93F36019; _ACCOUNT_=YjVjNDk0NDU3YTg3NDUxNWI3YzUyZGQyZDFiYTUyZDAlNDAlNDBtb2JpbGU6MTY5NTY5OTU5MzczMDpiMmNhZjgxMDcyMTU4OGU0NmU4ZDUyYzUyZWY2ZDJjNw',
    'Origin': 'https://www.hanghangcha.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'clientInfo': 'web',
    'clientVersion': '1.0.2',
    'currentHref': 'https://www.hanghangcha.com/products-local',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'filter': '{"city":"","lv":null,"province":"","userId":4511205,"companyId":null,"categoryThree":null,"limit":20,"skip":0,"tagId":38,"keyword":null,"companyType":"local","industry":"","page":2}',
}

data = requests.get('https://api.hanghangcha.com/hhc/invest/getProduct', params=params,
                    cookies=cookies,
                    headers=headers).json()


with open("d.js", 'r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
# res = ctx.call("demo")
# print(res)
print(data['data'])
res = ctx.call('decrypt', str(data['data']))
print(res)