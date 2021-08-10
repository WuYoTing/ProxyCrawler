import re
import requests
from bs4 import BeautifulSoup


def free_proxy_cz(driver):
    ip_pool = dict()
    for page in range(1, 11):
        print("{} : {}".format("page", page))
        # 用迴圈逐一打開分頁
        url = 'http://free-proxy.cz/en/proxylist/main/ping/{}'.format(page)
        print('Dealing with {}'.format(url))
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        for tbody_tr in soup.select('tbody > tr'):
            # 用正則表達式抓取IP
            if re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(tbody_tr)):
                IP = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(tbody_tr))[0]
                Port = re.findall('class="fport" style="">(.*?)</span>', str(tbody_tr))[0]
                # check proxy effectiveness
                proxy = {'http': 'http://' + IP + ':' + Port,
                         'https': 'https://' + IP + ':' + Port}
                try:
                    url = 'https://www.chinatimes.com/realtimenews/20200205004069-260408'
                    resp = requests.get(url, proxies=proxy, timeout=2)
                    if str(resp.status_code) == '200':
                        ip_pool[IP] = Port
                        print('Succed: {}:{}'.format(IP, Port))
                    else:
                        print('Failed: {}:{}'.format(IP, Port))
                except:
                    print('Failed: {}:{}'.format(IP, Port))
    print('There are {} IPs in Pool'.format(len(ip_pool)))
