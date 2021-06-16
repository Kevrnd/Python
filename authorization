from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("http://www.avtoto.ru")

input_button = driver.find_element_by_css_selector('.header-dark__login')
input_button.click ()

""" Login"""
user_name = driver.find_element_by_css_selector("input")
user_name.send_keys("Koshelev")

"""Password"""
user_passw = driver.find_element_by_css_selector('input[type="password" i]')
user_passw.send_keys("5At4JmoZ5lk")

"""Поехали"""
user_button = driver.find_element_by_tag_name('button')
user_button.click ()
