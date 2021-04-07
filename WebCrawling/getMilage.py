def getMilage(From,To,path):
    browser = webdriver.Chrome(path)

    # navigate to website
    browser.get("https://www.mapdevelopers.com/distance_from_to.php")

    to = browser.find_element_by_xpath('//*[@id="toInput"]')
    frm = browser.find_element_by_xpath('//*[@id="fromInput"]')
    frm.send_keys(From)
    to.send_keys(To)

    calculate = browser.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/span/form/a")
    calculate.click()
    sleep(3.6)

    drivingDistance = browser.find_element_by_xpath('//*[@id="driving_status"]')

    text = drivingDistance.text
    browser.quit()

    return text
