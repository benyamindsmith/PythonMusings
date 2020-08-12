
from selenium import webdriver
from time import sleep

def search_amazon(driver_type,driver_path, query):
    '''
    Search for products on Amazon.ca  all from the comfort of your IDE!

    ** Argument Definitions **

    :arg driver_type - Specify which driver you will be using.
                            Currently Compatible with Chrome, Edge,
                            Safari and Opera
    :arg driver_path - Path to your driver
    :arg query - What you want to look up

    ** Example **

    # I'm using the Chrome Driver

    myDriverPath =C:\\Path\\chromedriver.exe
    search_amazon('Chrome',myDriverPath,'Diapers')

    '''
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


