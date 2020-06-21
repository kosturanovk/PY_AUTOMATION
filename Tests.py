'''
Created on Jun 20, 2020

@author: kostu
'''
from MusalaHome import Home
from SignIn import UserArea
from MuffinFb import FbProfile
from Official import Landing
from Archive import EventArchiveList
from EventDetails import EventDesc
import yaml
import time
from builtins import str

def test_case_1(browser):
    print("test case 1 start.....")
    musala_main_page = Home(browser)
    musala_main_page.go_to_site()
    musala_main_page.click_on_the_sign_in_button()
    a = musala_main_page.get_link()
    print("Link:", a)
    assert  musala_main_page.get_link().find("login") != -1
    musala_sign_in_page = UserArea(browser)
    #read parametric credentials file
    with open('credentials.yaml') as f:
        my_dict = yaml.safe_load(f)
    dict_list = []
    #manipulate list and dict in order to achieve [usr1, pwd1, usr2, pwd2] list
    for i in my_dict.values():
        dict_list.append(i)
    if len(dict_list) % 2 == 0:
        last_index= int(len(dict_list) / 2)
        for i in range(last_index):
            timestr = time.strftime("%Y%m%d%H%M%S")
            musala_sign_in_page.input_user(my_dict["usr"+str(i+1)])
            musala_sign_in_page.input_pass(my_dict["pwd"+str(i+1)])
            musala_sign_in_page.click_sign_in_button()
            musala_sign_in_page.scroll_bottom()
            assert musala_sign_in_page.check_presence_wrong_pass_msg()
            musala_sign_in_page.take_screen_shot("msgpass"+str(timestr)+".png")
            musala_sign_in_page.reload_page()
    print("test case 1 END")        

def test_case_2(browser):
    print("test case 2 start.....")
    musala_main_page = Home(browser)
    musala_main_page.go_to_site()
    musala_main_page.verify_top_navbar()
    musala_main_page.scroll_bottom()
    musala_main_page.verify_footer()
    musala_main_page.click_musala_official_link_footer()
    
    musala_main_page.switch_last_open_tab()
    musala_main_page.pause(10)
    #http://www.musala.com/ check
    official_page = Landing(browser)
    assert official_page.logo_exists()
    assert official_page.logo_is_visible()
    assert official_page.get_link().find("www.musala.com") != -1
    # muffin management
    musala_main_page.switch_to_first_open_tab()
    musala_main_page.pause(10)
    musala_main_page.scroll_bottom()
    musala_main_page.verify_footer()
    musala_main_page.click_muffin_event()
    musala_main_page.switch_last_open_tab()
    musala_main_page.pause(10)
    #(https://www.facebook.com/MUFFINconference/)
    muffin_fb_page = FbProfile(browser)
    assert muffin_fb_page.profile_pic_exists()
    assert muffin_fb_page.profile_pic_visible()
    assert muffin_fb_page.get_link().find("facebook.com/MUFFIN") != -1
    print("test case 2 END") 
    
def test_case_3(browser):
    print("test case 3 start.....") 
    musala_main_page = Home(browser)
    musala_main_page.go_to_site()
    musala_main_page.verify_top_navbar()
    musala_main_page.click_on_archive_button()
    event_archive_page = EventArchiveList(browser)
    #https://masters.musala.com/archive
    assert event_archive_page.get_link().find("archive") != -1
    event_archive_page.scroll_bottom()
    event_archive_page.check_presence_footer_archive()
    event_archive_page.click_last_event()
    event_desc_page = EventDesc(browser)
    event_desc_page.check_desc_elemnts_exist()
    # https://masters.musala.com/event/master-class 
    #last event title
    assert event_desc_page.get_link().find("master-class") != -1
    summary = ""
    summary = event_desc_page.get_event_summary()
    assert summary.find("Day ") != -1
    print(summary)
    print("test case 3 END")
    
