from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.google.com')

elem = driver.find_element(By.NAME,'q')
elem.clear()
search='고죠 사토루'
elem.send_keys(search)
elem.send_keys(Keys.RETURN)
assert 'No results found.' not in driver.page_source
