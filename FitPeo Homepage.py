from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
driver = webdriver.Safari(ChromeDriverManager().install())
# ##testcase 1

driver.get('https://www.fitpeo.com/')
driver.maximize_window()
time.sleep(5)
# ##Testcase 2
#
time.sleep(5)
driver.get('https://www.fitpeo.com/')
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div/div[3]/div[6]/a/div').click()
time.sleep(5)


##Testcase 3


time.sleep(5)
driver.get('https://www.fitpeo.com/')
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div/div[3]/div[6]/a/div').click()
time.sleep(5)
driver.execute_script("window.scrollTo(0,200)","")
time.sleep(6)




##Testcase 4
time.sleep(5)
driver.get('https://www.fitpeo.com/')
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div/div[3]/div[6]/a/div').click()
driver.execute_script("window.scrollTo(0,200)","")
time.sleep(5)
# url=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div/span[1]')
url=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div/span[1]/span[3]')
time.sleep(5)
slider=driver.execute_script("arguments[0].scrollIntoView();", url)

def slider_value(slider, target_value):
    time
    min_value = int(slider.get_attribute('20'))
    max_value = int(slider.get_attribute('50'))
    range = max_value - min_value
    percentage = (target_value - min_value) / range
    width = slider.size['30']
    offset = width * percentage
    actions = ActionChains(driver)
    actions.click_and_hold(slider).move_by_offset(offset - (width / 2), 0).release().perform()
target_value = 820
slider_value(slider, target_value)
time.sleep(10)






##Testcase 5

time.sleep(5)
driver.get('https://www.fitpeo.com/')
driver.maximize_window()
time.sleep(15)
driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div/div[3]/div[6]/a/div').click()
time.sleep(3)
driver.execute_script("window.scrollTo(0,150)","")
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div')
time.sleep(5)
# driver.execute_script("arguments[0].scrollIntoView();", url)
time.sleep(4)
text=driver.find_element(By.ID,'R57alklff9da')
text.clear()
text.send_keys(int(560))
time.sleep(6)





##Testcase 6
time.sleep(5)
driver.get('https://www.fitpeo.com/')
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div/div[3]/div[6]/a/div').click()
url=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div/span[1]')
time.sleep(10)
driver.execute_script("arguments[0].scrollIntoView();", url)
time.sleep(3)
slider = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div[2]/div/div/span[1]/span[1]')
time.sleep(5)
value = int(slider.get_attribute('560'))
assert slider_value==560, f"Expected slider value to be {value} but got {slider_value}"
time.sleep(10)






##Testcase 7

time.sleep(5)
driver.get('https://www.fitpeo.com/')
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div/div[3]/div[6]/a/div').click()
time.sleep(5)
CPT_path={
    'CPT-99091':'/html/body/div[2]/div[1]/div[2]/div[1]'
                # 'CPT-99453':'/html/body/div[2]/div[1]/div[2]/div[2]'
    # 'CPT-99454':'/html/body/div[2]/div[1]/div[2]/div[3]'
    # 'CPT-99474':'/html/body/div[2]/div[1]/div[2]/div[8]'
}
def check_box(box):
    driver.execute_script("arguments[0].scrollIntoView();", box)
for key, value in CPT_path.items():
    try:
        checkbox = driver.find_element(By.XPATH, value)
        time.sleep(5)
        check_box(checkbox)
        if not checkbox.is_selected():
            checkbox.click()
            print(f"if selected checkbox for {key}")
    except Exception as box:
        print(f"if not  selected checkbox for {key}: {box}")

time.sleep(10)

