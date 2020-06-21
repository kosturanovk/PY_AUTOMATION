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
    #LOCATOR_FB_PROFILE_PIC  =  (By.XPATH,"//div[@id='navbar']//a[@class='brand' and contains(@href,musala)]//p")
    #${MUFFIN_FB_URL}    https://www.facebook.com/MUFFINconference/
    LOCATOR_PROFILE_PICURE =   (By.XPATH," //a[@aria-label='Profile picture']//img")
    #${MASTERS_TAB_RETURN}    Meet the Masters
    
class FbProfile(BasePage):
    

    def profile_pic_exists(self):
        return self.find_element(MusalaLocators.LOCATOR_PROFILE_PICURE, 3)
  
    
    def profile_pic_visible(self):
        return self.visualize_element(MusalaLocators.LOCATOR_PROFILE_PICURE, 3)