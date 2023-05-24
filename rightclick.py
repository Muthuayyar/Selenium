from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from  selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
sleep(10)
driver.find_element(By.ID,"field1").send_keys("Muthu")
sleep(3)
new= double=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
sleep(3)

action= ActionChains(driver)
action.context_click(new).perform()  #Right click action 
sleep(5)