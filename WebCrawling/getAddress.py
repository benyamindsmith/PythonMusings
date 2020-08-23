def getAddress(driverPath, placeName):
    '''
    A function for getting addresses based off of buisness/location name by querying
    Google Maps with Selenium. This is currently compatible with Google Driver only.

    :arg driverPath - path to your driver
    :arg placeName - Whats the name of the place you are looking for?

        # Example

        # places = ["CN Tower", "Long and Maquade Downtown", "Green Beanery", "The ROM"]

        # addresses = []
        # for place in places:
        #     addresses.append(getAddress(myDriverPath, place))

        # print(addresses)



    '''
    browser = webdriver.Chrome(driverPath)

    browser.get("https://www.google.com/maps")

    sleep(2)
    textBox = browser.find_element_by_xpath('//*[@id="searchboxinput"]')
    textBox.click()
    sleep(1)
    textBox.send_keys(placeName)

    sleep(1)
    searchMaps = browser.find_element_by_xpath('//*[@id="searchbox-searchbutton"]')
    searchMaps.click()

    sleep(3)
    try:
        ProperAddress = browser.find_element_by_class_name("ugiz4pqJLAG__text").text
    except:
        ProperAddress="Could not find address"

    browser.close()

    return ProperAddress
