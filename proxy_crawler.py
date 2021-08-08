import pandas as pd
import re

import requests

from get_selenium_page import create_driver_instance, get_selenium_page

driver = create_driver_instance()

IPPool = []
for page in range(1, 10):
    # 用迴圈逐一打開分頁
    url = 'http://free-proxy.cz/zh/proxylist/country/US/https/ping/all/{}'.format(page)
    print('Dealing with {}'.format(url))
    page_data = get_selenium_page(url, driver)
    for tbody_tr in page_data.select('tbody > tr'):
        # 用正則表達式抓取IP
        if re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(tbody_tr)):
            IP = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(tbody_tr))[0]
            Port = re.findall('class="fport" style="">(.*?)</span>', str(tbody_tr))[0]
            IPPool.append(pd.DataFrame([{'IP': IP, 'Port': Port}]))
    print('There are {} IPs in Pool'.format(len(IPPool)))
IPPool = pd.concat(IPPool, ignore_index=True)
print(IPPool)

# test proxy effectiveness
ActIps = []
for IP, Port in zip(IPPool['IP'], IPPool['Port']):
    proxy = {'http': 'http://' + IP + ':' + Port,
             'https': 'https://' + IP + ':' + Port}
    try:
        # 隨機找的一篇新聞即可
        url = 'https://www.chinatimes.com/realtimenews/20200205004069-260408'
        resp = requests.get(url, proxies=proxy, timeout=2)
        if str(resp.status_code) == '200':
            ActIps.append(pd.DataFrame([{'IP': IP, 'Port': Port}]))
            print('Succed: {}:{}'.format(IP, Port))
        else:
            print('Failed: {}:{}'.format(IP, Port))
    except:
        print('Failed: {}:{}'.format(IP, Port))
ActIps = pd.concat(ActIps, ignore_index=True)
ActIps