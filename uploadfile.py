from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from  selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
sleep(5)

driver.switch_to.frame(0)
driver.find_element(By.ID,"RESULT_FileUpload-10").send_keys("C://Users/ASM/Downloads/testyara.txt")   # upload file

sleep(5)