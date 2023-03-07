import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
browser = webdriver.Chrome()
 

# go to speed typing website
browser.get("https://www.sporcle.com/games/iurewhiuerw/numbers1_100")
 

btn = browser.find_element(By.XPATH, '//*[@id="button-play"]')
browser.execute_script("arguments[0].click();", btn)

for i in range(1,100+1):
    inp = browser.find_element(By.XPATH, '//*[@id="gameinput"]')
    inp.send_keys(i," ")
    print(i)
