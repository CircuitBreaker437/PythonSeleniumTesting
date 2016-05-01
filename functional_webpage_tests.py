'''
@filename: functionale_webpage_tests.py
@author: Marcin Czajkowski
@purpose: W3C Markup Validation using selenium
'''

from selenium import webdriver

driver = webdriver.Firefox()

#test1: W3C validation
driver.get("http://validator.w3.org/check?uri=" + "http://circuitbreakerlab.com/")
