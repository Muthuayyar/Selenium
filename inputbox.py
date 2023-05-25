from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import selenium
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://mytestingthoughts.com/Sample/home.html")
ele=driver.find_elements(By.CLASS_NAME,"form-control")
print(len(ele))