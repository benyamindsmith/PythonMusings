from selenium import webdriver
from time import sleep

def search_amazon(driver_type,driver_path, query):
    global browser
    if driver_type =='Chrome' or driver_type=='chrome':
        browser=webdriver.Chrome(driver_path)
    elif driver_type == 'Edge' or driver_type == 'edge':
        browser = webdriver.Edge(driver_path)
    elif driver_type == 'Safari' or driver_type == 'safari':
        browser = webdriver.Safari(driver_path)
    elif driver_type =="Opera" or driver_type =="opera":
        browser=webdriver.Opera(driver_path)

    browser.get('https://www.amazon.ca/')
    searchBar = browser.find_element_by_css_selector('#twotabsearchtextbox')
    sleep(1)
    searchBar.send_keys(query)
    enter = browser.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
    enter.click()
