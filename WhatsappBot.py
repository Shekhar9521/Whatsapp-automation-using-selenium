from selenium import webdriver
import time

chrome_browser = webdriver.Chrome(executable_path='C:/chromedriver')
chrome_browser.get('https://web.whatsapp.com/')

time.sleep(15)

user_name = 'Whatsapp bot'

user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()

message_box = chrome_browser.find_element_by_xpath('//div[@class"DuUXI"]')
message_box.send_keys(Hey there,I am your Whatsapp bot)

message_box = chrome_browser.find_element_by_xpath('//button[@class"_3M-N-"]')
message_box.click()