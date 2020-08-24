def getGeocode(driverPath, Address):
    '''
    A function for getting geocodes of a given address on geocode.ca with Selenium.
    Currently only compatible with ChromeDriver.

    :param driverPath:
    :param Address:
    :return:
    '''
    browser = webdriver.Chrome(driverPath)
    browser.get("https://geocoder.ca/")
    sleep(2)
    textBox = browser.find_element_by_class_name('input-block-level')
    textBox.click()
    try:
        textBox.send_keys(Address)
        enter = browser.find_element_by_xpath('//*[@id="geocode"]/input[2]')
        enter.click()
        try:
            geoCode = browser.find_element_by_xpath('/html/body/div[2]/table[2]/tbody/tr/td[2]/p/strong').text
            browser.close()
        except:
            geoCode = "Na"
            browser.close()
    except:
        geoCode="Na"
    return geoCode
