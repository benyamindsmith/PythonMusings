from selenium import webdriver
from time import sleep

# A tool used for "purifying" non-complete addresses by getting them from google maps.
# not a perfect tool but definitely good for ad-hoc work where your client will say 
#"Not all our addresses our properly formatted so you will have to figure out the route"


def getProperAddress(driverPath, addressesToValidate):

    browser = webdriver.Chrome(driverPath)

    browser.get("https://www.google.com/maps")

    sleep(2)
    textBox = browser.find_element_by_xpath('//*[@id="searchboxinput"]')
    textBox.click()
    sleep(1)
    textBox.send_keys(addressesToValidate)

    sleep(1)
    searchMaps = browser.find_element_by_xpath('//*[@id="searchbox-searchbutton"]')
    searchMaps.click()

    sleep(2)
    ProperAddress_1 = browser.find_element_by_xpath(
        '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]')
    ProperAddress_2 = browser.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h2/span')

    ProperAddress = ProperAddress_1.text + " " + ProperAddress_2.text

    return ProperAddress
