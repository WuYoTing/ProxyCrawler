import requests
from bs4 import BeautifulSoup

from lib.test_proxy import test_proxy_usability


def proxy_scan():
    ip_pool = dict()
    url = 'https://www.proxyscan.io/Home/FilterResult'
    data = {
        "status": 1,
        "ping": 1000,
        "selectedType": 'HTTP',
        "selectedType": 'HTTPS',
        "sortPing": True,
        "sortTime": False,
        "sortUptime": False
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        response_dom = BeautifulSoup(response.text, 'lxml')
        ip_tr_list = response_dom.select('tr')
        for ip_tr in ip_tr_list:
            ip = ip_tr.select('th')[0].get_text()
            port = ip_tr.select('td')[0].get_text()
            # check proxy effectiveness
            if test_proxy_usability(ip, port):
                ip_pool[ip] = port
    return ip_pool
