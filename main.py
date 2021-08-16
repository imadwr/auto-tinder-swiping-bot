from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Development/chromedriver.exe"


driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.tinder.com")

time.sleep(3)

# login to tinder

login_button = driver.find_element_by_xpath("//*[@id='q-2110398392']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
login_button.click()
time.sleep(2)
login_with_facebook = driver.find_element_by_xpath("//*[@id='q456187828']/div/div/div[1]/div/div[3]/span/div[2]/button")
login_with_facebook.click()
time.sleep(2)

tinder_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_input = driver.find_element_by_xpath("//*[@id='email']")
email_input.send_keys("YOUR FACEBOOK EMAIL")
password_input = driver.find_element_by_xpath("//*[@id='pass']")
password_input.send_keys("YOUR FACEBOOK PASSWORD")
password_input.send_keys(Keys.ENTER)

driver.switch_to.window(tinder_window)
time.sleep(5)

# Dismiss all requests

allow_location = driver.find_element_by_xpath('//*[@id="q456187828"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
disable_notification = driver.find_element_by_xpath('//*[@id="q456187828"]/div/div/div/div/div[3]/button[2]')
disable_notification.click()
accept_cookies = driver.find_element_by_xpath('//*[@id="q-2110398392"]/div/div[2]/div/div/div[1]/button')
accept_cookies.click()
time.sleep(5)

# auto swiping

body = driver.find_element_by_tag_name("body")
body.click()

# 100 swipes a day
for _ in range(100):
    time.sleep(3)
    body.click()
    body.send_keys(Keys.ESCAPE)
    body.send_keys(Keys.RIGHT)


driver.quit()
