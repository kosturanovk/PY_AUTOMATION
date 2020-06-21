'''
Created on Jun 20, 2020

@author: kostu
'''
from BaseApp import BasePage
from selenium.webdriver.common.by import By



class MusalaLocators:
    LOCATOR_SIGN_IN = (By.XPATH, "//ul[@class='nav navbar-nav navbar-right']//li//a[@class='btn btn-nav' and contains(text(),'Sign In')]")
    LOCATOR_ARCHIVE = (By.XPATH, "//ul[@class='nav navbar-nav navbar-right']//li//a[@class='btn btn-nav' and contains(text(),'Archive')]")
    LOCATOR_FOOTER = (By.XPATH, "//Footer")
    LOCATOR_NAVBAR_TOP = (By.XPATH, "//div[@class='navbar-header']")
    LOCATOR_FOOTER_LINK_OFFICIAL = (By.XPATH, "//div[@class='leftPartFooter']//img[@class='footer-image']")
    LOCATOR_FOOTER_MUFFIN_LINK = (By.XPATH, "//div[@class='rightPartFooter']//a[contains(@href, 'MUFFIN')]")

class Home(BasePage):

    def click_on_the_sign_in_button(self):
        return self.find_element(MusalaLocators.LOCATOR_SIGN_IN,time=2).click()
    
    def verify_top_navbar(self):
        return self.visualize_element(MusalaLocators.LOCATOR_NAVBAR_TOP, 3)
    
    def verify_footer(self):
        return self.visualize_element(MusalaLocators.LOCATOR_FOOTER, 3)
    
    def click_musala_official_link_footer(self):
        return self.find_element(MusalaLocators.LOCATOR_FOOTER_LINK_OFFICIAL, 3).click()
    
    def click_muffin_event(self):
        return self.find_element(MusalaLocators.LOCATOR_FOOTER_MUFFIN_LINK, 3).click()
    
    def click_on_archive_button(self):
        return self.find_element(MusalaLocators.LOCATOR_ARCHIVE, 3).click()
