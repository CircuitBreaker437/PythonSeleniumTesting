#Filename: redirection_and_navigation.py
#Programmer: Marcin Czajkowski
#Purpose: Example of rediection handling and forward, back history navigation

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#setup driver
driver = webdriver.Firefox()

#get to the webpage
driver.get("http://circuitbreakerlab.com/")

#find the link by text
linkedInLink = driver.find_element_by_link_text("Contact Information")

#navigate to the link by pressing ENTER
linkedInLink.send_keys(Keys.RETURN)

#verify current URL - this doesnt work if the webpage was open in new window/session
print(driver.current_url)

#find the link by text in the new/redirected URL
linkedInLink = driver.find_element_by_link_text("LinkedIn Profile")

#navigate to the link by pressing ENTER
linkedInLink.send_keys(Keys.RETURN)

#navigation between window histories
#driver.forward()
#driver.back()
