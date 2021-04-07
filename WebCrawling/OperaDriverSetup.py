from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome import service
from selenium.webdriver.opera.options import Options

options = Options()
options.binary_location ="path_to_driver"
webdriver_service = service.Service("path_to_driver")
webdriver_service.start()

driver = webdriver.Opera(options = options, executable_path="path_to_.exe_file")
driver.get('http://www.google.com')
sleep(2)
driver.quit()
