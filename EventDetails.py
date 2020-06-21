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
    LOCATOR_FOOTER_EVENTDESC_PAGE = (By.XPATH, "//*//footer")
    LOCATOR_GENERIC_ELEMENT = (By.XPATH, "//ul[@class='list-group checked-list-box']")
    
    #${EVENT_URL}    https://masters.musala.com/event/master-class
    
class EventDesc(BasePage):

    def check_bottom_vibile(self):
        return self.visualize_element(MusalaLocators.LOCATOR_FOOTER_EVENTDESC_PAGE, 3)
    
    def check_desc_elemnts_exist(self):
        return self.find_elements(MusalaLocators.LOCATOR_GENERIC_ELEMENT, 4)
    
    def get_event_summary(self):
        all_descritptive_fields = []
        all_descritptive_fields = self.driver.find_elements(By.XPATH, "//ul[@class='list-group checked-list-box']")
        description = ""
        elem_txt = ""
        for i in all_descritptive_fields:
            elem_txt = i.text
            last_line = elem_txt.splitlines()[-1]
            
            description = description + last_line + "\n"
        return description
        
    def scroll_to_last_desc(self):
        return self.driver.scroll