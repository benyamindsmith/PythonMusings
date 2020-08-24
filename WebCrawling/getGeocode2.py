
def getGeocode2(driverPath, Address):
    '''
    A function for getting geocodes of a given address on https://geocode.xyz/ with Selenium
    and is in compliance with the robots.txt (as of 8/23/2020)

    Currently only compatible with ChromeDriver.

    :param driverPath: path to ChromeDriver
    :param Address: Address you are interested in searching.
    '''
    browser = webdriver.Chrome(driverPath)
    browser.get("https://geocode.xyz/")
    textBox = browser.find_element_by_xpath('//*[@id="hello"]/div/div/div/div[1]/div/div/form/div/div/div[1]/input')
    textBox.click()
    textBox.send_keys(Address)
    enter = browser.find_element_by_xpath('//*[@id="hello"]/div/div/div/div[1]/div/div/form/div/input')
    sleep(5)
    enter.click()
    try:
        geoCode = browser.find_element_by_xpath('//*[@id="bg-text"]/small/a').text
        browser.close()
    except:
        geoCode = "Na"
        browser.close()
    return geoCode
