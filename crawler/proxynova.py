import requests
from bs4 import BeautifulSoup

from lib.test_proxy import test_proxy_usability


def proxy_nova():
    ip_pool = dict()
    anonymous_url = 'https://www.proxynova.com/proxy-server-list/anonymous-proxies/'
    elite_url = 'https://www.proxynova.com/proxy-server-list/elite-proxies/'
    response = requests.get(anonymous_url)
    if response.status_code == 200:
        response_dom = BeautifulSoup(response.text, 'lxml')
        for ip_tr in response_dom.select('tbody tr'):
            if len(ip_tr.select('td')) > 1:
                js_ip = ip_tr.select_one('td abbr script')
                ip = str(js_ip).replace("<script>document.write('", "").replace("');</script>", "")
                port_td = ip_tr.select('td')[1].get_text()
                port = port_td.replace(" ", "").replace("\n", "")
                # check proxy effectiveness
                if test_proxy_usability(ip, port):
                    ip_pool[ip] = port
    return ip_pool
