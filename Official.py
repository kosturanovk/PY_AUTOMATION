'''
Created on Jun 20, 2020

@author: kostu
'''
import time
from BaseApp import BasePage
from selenium.webdriver.common.by import By

from selenium import webdriver
from appium.webdriver.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException


class MusalaLocators:
    LOCATOR_COMPANY_LOGO  =  (By.XPATH,"//div[@id='navbar']//a[@class='brand' and contains(@href,musala)]//p")
    
class Landing(BasePage):
    

    def logo_exists(self):
        return self.find_element(MusalaLocators.LOCATOR_COMPANY_LOGO, 3)
    
    def logo_is_visible(self):
        return self.visualize_element(MusalaLocators.LOCATOR_COMPANY_LOGO, 3)
    