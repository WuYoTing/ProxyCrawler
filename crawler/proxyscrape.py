import re
import requests

from lib.test_proxy import test_proxy_usability


def proxy_scrape():
    ip_pool = dict()
    url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=8000&country=all&ssl=all&anonymity=all&simplified=true'
    response = requests.get(url)
    match_ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', response.text)
    # check proxy effectiveness
    for match_ip in match_ips:
        ip_port = match_ip.split(":")
        ip = ip_port[0]
        port = ip_port[1]
        # check proxy effectiveness
        if test_proxy_usability(ip, port):
            ip_pool[ip] = port
    return ip_pool
