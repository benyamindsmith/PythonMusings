from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import urllib

def googleTranslate(text,langFrom, driver_path,  sleep_time=4):
  '''
  Right now this is only compatible with chrome driver. 
  You can edit the code to work with another driver. 
  
  
  Translates to english with autodetect. Play with the api for other
  languages. 
  '''
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  
  link = "https://translate.google.ca/?sl="+ langFrom +  "&tl=en&text=" + urllib.parse.quote(text) + '&op=translate'
  
  browser = webdriver.Chrome(driver_path)
  browser.get(link)
  sleep(sleep_time)
  #browser.find_element_by_css_selector('#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea').send_keys(text)
  #sleep(sleep_time)
  txt=browser.find_element_by_css_selector('#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.P6w8m.BDJ8fb.BLojaf > div.dePhmb > div > div.J0lOec > span.VIiyi > span > span').text
  return(txt)
