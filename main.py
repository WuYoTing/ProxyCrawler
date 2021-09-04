from crawler.free_proxy_cz import free_proxy_cz
from crawler.us_proxy import us_proxy
from lib.get_selenium_page import create_driver_instance

driver = create_driver_instance()
free_proxy_cz_dict = free_proxy_cz(driver)
us_proxy_dict = us_proxy()
print('There are {} IPs in free_proxy_cz_Pool'.format(len(free_proxy_cz_dict)))
print('There are {} IPs in us_proxy_Pool'.format(len(us_proxy_dict)))
driver.close()
