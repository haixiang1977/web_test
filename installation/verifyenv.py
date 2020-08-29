# open a Firefox browser sessions and navigate to http://www.ubuntu.com/

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.google.com')
