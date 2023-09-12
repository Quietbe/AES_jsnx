import requests

#  https://webapi.cninfo.com.cn/#/marketData

cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1694499729',
    'JSESSIONID': 'D14974586745AC16892252B6F2D162D5',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1694506034',
}

headers = {
    'Accept': '*/*',
    # 'Accept-EncKey': 'jprtYayxVskJ0b6rgqSjcQ==',
    'Accept-EncKey':   'M3RgQf02NkY64rggG8hsDg==',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1694499729; JSESSIONID=D14974586745AC16892252B6F2D162D5; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1694506034',
    'Origin': 'https://webapi.cninfo.com.cn',
    'Referer': 'https://webapi.cninfo.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'scode': '000001-SZE',
    'sdate': '2022-09-12',
    'edate': '2023-09-12',
    'ctype': '0',
}

response = requests.post('https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1008',
                         # cookies=cookies,
                         headers=headers, data=data)
print(response.json())