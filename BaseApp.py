'''
Created on Jun 20, 2020

@author: kostu
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import yaml



class BasePage:
    
    param_url_choice= "https://masters.musala.com/"
    
    with open("C:/Users/kostu/eclipse-workspace/MusalaCheck_PY/run_config.yaml") as file:
        documents = yaml.full_load(file)

    for item, val in documents.items():
        if item == 'url':
            param_url_choice= val
            
    def __init__(self, driver):
        link = self.param_url_choice
        self.driver = driver
        self.base_url = link
    
    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),message=f"Can't find element by locator {locator}")
    
    def visualize_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.visibility_of_element_located(locator),message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
    
    def get_link(self):
        return self.driver.current_url
    
    def scroll_bottom(self):
        return self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    
    def take_screen_shot(self,filename_screen):
        return self.driver.get_screenshot_as_file(filename_screen)
    
    def reload_page(self):
        address_page = self.driver.current_url
        return self.driver.get(address_page)
    
    def pause(self,sec_interval):
        return self.driver.implicitly_wait(sec_interval)
    
    def switch_last_open_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])
    
    def switch_to_first_open_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[0])
    
    
    
        
