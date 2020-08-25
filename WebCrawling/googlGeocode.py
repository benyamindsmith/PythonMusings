from selenium import webdriver
from time import sleep
import re

def googlGeocode(driverPath, addressesToGeoCode):
    '''
    A function for getting properly formatted addresses and based off of address by querying
    Google Maps with Selenium. This is currently compatible with Chrome Driver only.

    :arg driverPath - path to your driver
    :arg addressesToGeoCode - What addresses do you want to geocode?
    '''
    browser = webdriver.Chrome(driverPath)

    try:
        browser.get("https://www.google.com/maps")

        sleep(2)
        textBox = browser.find_element_by_xpath('//*[@id="searchboxinput"]')
        textBox.click()
        sleep(1)
        try:
            textBox.send_keys(addressesToGeoCode)

            sleep(1)
            searchMaps = browser.find_element_by_xpath('//*[@id="searchbox-searchbutton"]')
            searchMaps.click()

            sleep(2)

            ProperAddress_1 = browser.find_element_by_xpath(
                '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]')
            ProperAddress_2 = browser.find_element_by_xpath(
                '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h2/span')

            ProperAddress = ProperAddress_1.text + " " + ProperAddress_2.text
            geoCode=browser.current_url

            geoCode=re.findall('@\d{2}\.\d{7},-\d{2}\.\d{7}',geoCode)
            browser.close()

        except:

            try:
                ProperAddress = browser.find_element_by_class_name("section-hero-header-title-description")
                geoCode = browser.current_url
                browser.close()
            except:
                ProperAddress = "Nan"
                geoCode ="Nan"
                browser.close()
            return [ProperAddress,geoCode]
    except:
        ProperAddress="Nan"
        geoCode="Nan"

    return [ProperAddress,geoCode]
