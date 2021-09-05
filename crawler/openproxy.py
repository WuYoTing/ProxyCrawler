import re

import requests
import time

from bs4 import BeautifulSoup

from lib.test_proxy import test_proxy_usability


def open_proxy(driver):
    ip_pool = dict()
    ts = format(time.time() * 1000, ".3f")
    print(ts)
    index_url = 'https://api.openproxy.space/list?skip=0&ts={}'.format(ts)

    response = requests.get(index_url)
    if response.status_code == 200:
        for block_data in response.json():
            if block_data['title'] == 'FRESH HTTP/S':
                print(block_data['code'])
                url_code = block_data['code']
                break
    proxy_list_url = 'https://openproxy.space/list/{}'.format(url_code)
    driver.get(proxy_list_url)
    proxy_list_page = BeautifulSoup(driver.page_source, 'lxml')
    proxy_list = proxy_list_page.select_one("textarea").get_text()
    match_ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', proxy_list)
    for match_ip in match_ips:
        ip_port = match_ip.split(":")
        ip = ip_port[0]
        port = ip_port[1]
        # check proxy effectiveness
        if test_proxy_usability(ip, port):
            ip_pool[ip] = port
    return ip_pool
