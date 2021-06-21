import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
filename = 'reserv.txt'

with open(filename) as file_object:
    line1 = str(file_object.readlines(1))
    username = line1.rstrip(" \ n ' ] ")
    username = username.lstrip ("['")
    line2 = str(file_object.readlines(2))
    password = line2.rstrip(" \ n ' ] ")
    password = password.lstrip ("['")

print (username.rstrip("\n']"))
print (password)

"""pageopen"""
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://my.drom.ru/sign?return=https%3A%2F%2Fwww.drom.ru%2F%3Ftcb%3D1624270060")

""" Login"""
user_name = driver.find_element_by_id("sign")
user_name.send_keys(username)

"""Password"""
user_name = driver.find_element_by_id("password")
user_name.send_keys(password)

"""Войти с паролем"""
user_button = driver.find_element_by_id('signbutton')
user_button.click ()

driver.set_page_load_timeout(10)
driver.get("https://my.drom.ru/personal/edit/password")

#random password
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
newpassword =''
for i in range(8):
    newpassword += random.choice(chars)
print(newpassword)

#write new password
file_object = open(filename,'w') 
file_object.write (username)
file_object.write("\n")
file_object.write (newpassword)
file_object.close()

"""Changepassword"""
newpassword = driver.find_element_by_name ('newPassword')
newpassword.send_keys(password)

newpassword2 = driver.find_element_by_name ('newPassword2')
newpassword2.send_keys(password)

results = driver.find_elements_by_css_selector('body .em-button, body .em-button')
first_result = results[0]
first_result.click()

driver.close()
