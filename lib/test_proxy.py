import requests


def test_proxy_usability(ip, port):
    proxy = {'http': 'http://' + ip + ':' + port}
    try:
        url = 'http://icanhazip.com/'
        resp = requests.get(url, proxies=proxy, timeout=8)
        proxy_ip = resp.text
        if len(proxy_ip) > 15:
            print('Failed: {}:{}'.format(ip, port))
            return False
        proxy_ip = proxy_ip.strip('\n')
        if proxy_ip == ip:
            print('Succed: {}:{}'.format(ip, port))
            return True
        else:
            print('Failed: {}:{}'.format(ip, port))
            return False
    except Exception as e:
        print('Except: {}:{} , e: {}'.format(ip, port, e))
        return False
