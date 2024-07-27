# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.google.com/")

# get element 
element = driver.find_element(By.XPATH, "//div[@class='RNmpXc']")

# click the element
element.click()
