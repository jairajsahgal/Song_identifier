from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
browser= webdriver.Chrome(options=chrome_options)

browser.get('http://s000.tinyupload.com/index.php')
browser.find_element_by_class_name("pole_plik").click()
browser.find_element_by_name("sessionid").click()

browser.quit()