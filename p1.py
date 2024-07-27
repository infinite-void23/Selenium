# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# create webdriver object
driver = webdriver.Chrome(options=chrome_options)

# get geeksforgeeks.org
driver.get("https://www.google.com/")
time.sleep(4)
# get element 
a = WebDriverWait(driver, 19).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='M6CB1c rr4y5c']")))
a.click()
bt = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='RNmpXc']")))
bt.click()

print("Login Successful")
# click the element
time.sleep(15)
