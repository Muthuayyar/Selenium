from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import selenium
from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import  GeckoDriverManager
from selenium.webdriver.firefox.service import Service

driver= webdriver.Firefox(service=Service(".\Browser\geckodriver.exe"))

#driver = webdriver.Firefox(GeckoDriverManager().install())
driver.maximize_window()
driver.get("https://mytestingthoughts.com/Sample/home.html")
#time.sleep(20)
ele=driver.find_element(By.NAME,"department")
drp=Select(ele)

drp.select_by_visible_text('Department of Engineering')
#time.sleep(20)

drp.select_by_index(4)
#time.sleep(10)
print(len(drp.options))  #count the dropdown box value
time.sleep(10)
all=drp.options

for option in all:
    print(option.text) #print th all values in dropdown box