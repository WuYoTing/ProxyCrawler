from webside.free_proxy_cz import free_proxy_cz
from webdriver.get_selenium_page import create_driver_instance


driver = create_driver_instance()
free_proxy_cz(driver)
driver.close()
