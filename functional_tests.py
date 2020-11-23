from selenium import webdriver

browser = webdriver.Firefox() # Starting a Selenium "webdriver"
browser.get('http://localhost:8000') # Using it to open up a web page

assert 'Django' in browser.title # Checking(making a test assertion)
