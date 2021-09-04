import re
from bs4 import BeautifulSoup

from lib.test_proxy import test_proxy_usability


def free_proxy_cz(driver):
    ip_pool = dict()
    for page in range(1, 5):
        # 用迴圈逐一打開分頁
        url = 'http://free-proxy.cz/en/proxylist/country/all/http/ping/all/{}'.format(page)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        for tbody_tr in soup.select('tbody > tr'):
            # 用正則表達式抓取IP
            if re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(tbody_tr)):
                ip = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(tbody_tr))[0]
                port = re.findall('class="fport" style="">(.*?)</span>', str(tbody_tr))[0]
                # check proxy effectiveness
                if test_proxy_usability(ip, port):
                    ip_pool[ip] = port
    return ip_pool
