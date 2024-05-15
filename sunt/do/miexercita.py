from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.google.com")

element = driver.find_element_by_name("q")
ActionChains(driver).move_to_element(element).click(element).perform()
