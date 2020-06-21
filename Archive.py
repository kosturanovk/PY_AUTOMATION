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
    LOCATOR_FOOTER_ARCHIVE_PAGE = (By.XPATH, "//footer")
    LOCATOR_LAST_EVENT_BOX = (By.XPATH, "(//div[@id='events-cont']//div[@class='event-box-home'])[last()]")
    LOCATOR_SIGN_IN_BUTTON = (By.XPATH, "//button[@id='btn-sign-in']")
    
    
    #${URL_ARCHIVE}    https://masters.musala.com/archive
    #${LAST_EVENT_BOX}    (//div[@id='events-cont']//div[@class='event-box-home'])[last()]
    #${EVENT_URL}    https://masters.musala.com/event/master-class
    
class EventArchiveList(BasePage):

    def last_event_is_visible(self):
        return self.visualize_element(MusalaLocators.LOCATOR_LAST_EVENT_BOX, 3)
    
    def click_last_event(self):
        return self.find_element(MusalaLocators.LOCATOR_LAST_EVENT_BOX, 3).click()
    
    def check_presence_footer_archive(self):
        return self.visualize_element(MusalaLocators.LOCATOR_FOOTER_ARCHIVE_PAGE, 4)