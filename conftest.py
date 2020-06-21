'''
Created on Jun 20, 2020

@author: kostu
'''
import pytest 
from selenium import webdriver

param_choice_browser = "chrome"
import yaml
with open("C:/Users/kostu/eclipse-workspace/MusalaCheck_PY/run_config.yaml") as file:
    documents = yaml.full_load(file)

for item, doc in documents.items():
    if item == 'browser':
        param_browser_choice= doc


@pytest.fixture(scope="session") 
def browser():
    if param_choice_browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:/web_drivers/chromedriver.exe") 
        yield driver 
        driver.quit()
    if param_choice_browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:/web_drivers/geckodriver.exe") 
        yield driver 
        driver.quit()

