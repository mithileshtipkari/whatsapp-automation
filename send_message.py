from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

contact = "Paisa laya....?"
text = "Hey, this message was sent using Selenium"
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
raw_input()
# time.sleep(15)
print("Logged In")

inp_xpath_search = "//div[@class='_13NKt copyable-text selectable-text'][@role='textbox']"
input_box_search = WebDriverWait(driver,20).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
print("input box found -", input_box_search)
input_box_search.click()
time.sleep(5)
input_box_search.send_keys(contact)
time.sleep(5)

selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@title="Type a message"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
input_box.send_keys(text + Keys.ENTER)
time.sleep(2)

driver.quit()