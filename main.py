from crawler.free_proxy_cz import free_proxy_cz
from crawler.free_proxy_list_net import us_proxy
from crawler.proxyscrape import proxy_scrape
from lib.get_selenium_page import create_driver_instance

driver = create_driver_instance()

free_proxy_cz_dict = free_proxy_cz(driver)
us_proxy_dict = us_proxy()
proxy_scrape_dict = proxy_scrape()
print('There are {} IPs in free_proxy_cz_Pool'.format(len(free_proxy_cz_dict)))
print('There are {} IPs in us_proxy_Pool'.format(len(us_proxy_dict)))
print('There are {} IPs in us_proxy_Pool'.format(len(proxy_scrape_dict)))
driver.close()
