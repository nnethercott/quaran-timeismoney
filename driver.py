"""
@Cuong Tran's scroll function did not work with this website for some reason :(
"""

import requests
from selenium import webdriver
import time

class driver():
    browser = webdriver.Chrome('/Users/nathanielnethercott/Desktop/Coding/Stonks/quaran-timeismoney/chromedriver')

    def __init__(self, base):
        self.base = base

    def launch(self):
        self.browser.get(self.base)

    def terminate(self):
        self.browser.quit()

    def scroll_Bottom(self):
        #could do this based on time elapsed (like only scroll for x seconds)
        #maybe figure out sometime why the document.body.scrollHeight aint working
        #could also make the range a function of desired history length 
        for i in range(4):
            self.browser.execute_script("window.scrollBy(0, 20*document.body.scrollHeight);")
            time.sleep(0.25)

    def html_scrolled(self):
        self.launch()
        self.scroll_Bottom()
        return self.browser.page_source


'''
#Cuong's method:

def scroll_Bottom(self):
    # Get scroll height
    last_height = self.browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(0.5)
        # Calculate new scroll height and compare with last scroll height
        new_height = self.browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height'''