import requests
from bs4 import BeautifulSoup

from lib.test_proxy import test_proxy_usability


def us_proxy():
    ip_pool = dict()
    url = 'https://www.sslproxies.org/'
    response = requests.get(url)
    if response.status_code == 200:
        response_dom = BeautifulSoup(response.text, 'lxml')
        ip_tr_list = response_dom.select('.fpl-list tbody tr')
        for ip_tr in ip_tr_list:
            ip = ip_tr.select('td')[0].get_text()
            port = ip_tr.select('td')[1].get_text()
            # check proxy effectiveness
            if test_proxy_usability(ip, port):
                ip_pool[ip] = port
    return ip_pool
