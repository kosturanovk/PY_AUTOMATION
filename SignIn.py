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
    LOCATOR_INPUT_USR_FIELD = (By.XPATH, "//input[@id='login-form_username']")
    LOCATOR_INPUT_PWD_FIELD = (By.XPATH, "//input[@id='login-form_password']")
    LOCATOR_SIGN_IN_BUTTON = (By.XPATH, "//button[@id='btn-sign-in']")
    LOCATOR_WRONG_PASS = (By.XPATH,"//p[contains(text(),'Wrong user or password.')]")
    
class UserArea(BasePage):

    def input_user(self,param_usr):
        return self.find_element(MusalaLocators.LOCATOR_INPUT_USR_FIELD, 3).send_keys(param_usr)
    
    def input_pass(self,param_pwd):
        return self.find_element(MusalaLocators.LOCATOR_INPUT_PWD_FIELD, 3).send_keys(param_pwd)
    
    def click_sign_in_button(self):
        return self.find_element(MusalaLocators.LOCATOR_SIGN_IN_BUTTON, 3).click()
    
    def check_presence_wrong_pass_msg(self):
        return self.visualize_element(MusalaLocators.LOCATOR_WRONG_PASS, 4)