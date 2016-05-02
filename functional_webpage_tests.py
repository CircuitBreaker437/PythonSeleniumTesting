'''
@filename: functionale_webpage_tests.py
@author: Marcin Czajkowski
@version: 2.0
@purpose: Functionality test for a web-page
@resources: http://nullege.com/
'''

import re
import sys
import unittest
from selenium import webdriver

class W3C_Validation(unittest.TestCase):
    reportFile = open("report.txt", "w")
    reportFile.truncate()

    def setUp(self):
        #setup webdriver
        self.driverFireFox = webdriver.Firefox()
        
        
    def test_W3C_Score(self):
        #initialize circuitbreakerlab.com W3C validation check
        self.driverFireFox.get("http://validator.w3.org/check?uri=" + "http://circuitbreakerlab.com/")
        
        #gather all error messages and display them
        self.numberOfErrors = self.driverFireFox.find_elements_by_css_selector("li[class='error']")
        self.errorMsgs = [{category.text}
                          for category in self.numberOfErrors]
        print('\n' + 'Number of errors: ' + str(len(self.numberOfErrors)))
        W3C_Validation.reportFile.write('\n' + 'Number of errors: ' + str(len(self.numberOfErrors)))
        print('\n' + 'Error messages: ')
        W3C_Validation.reportFile.write('\n' + 'Error messages: ')
        for errormsg in self.errorMsgs:
            print('\n' + str(str(errormsg).encode("utf-8")))
            W3C_Validation.reportFile.write('\n' + str(str(errormsg).encode("utf-8")))
        
        #gather all warning messages and display them
        self.numberOfWarnings = self.driverFireFox.find_elements_by_css_selector("li[class='info warning']")
        self.warningMsgs = [{category.text}
                          for category in self.numberOfWarnings]
        print('\n' + 'Number of warnings: ' + str(len(self.numberOfWarnings)))
        W3C_Validation.reportFile.write('\n' + 'Number of warnings: ' + str(len(self.numberOfWarnings)))
        print('\n' + 'Warning messages: ')
        W3C_Validation.reportFile.write('\n' + 'Warning messages: ')
        for warningmsg in self.warningMsgs:
            print('\n' + str(str(warningmsg).encode("utf-8")))
            W3C_Validation.reportFile.write('\n' + str(str(warningmsg).encode("utf-8")))

        #final result - warnings are acceptable, errors are not
        self.assertLessEqual(len(self.numberOfErrors), 0, "ERRORS FOUND BY W3C VALIDATOR!")

    #def test_Links_Testing(self):


if __name__ == '__main__':
    unittest.main(verbosity=2) 
