import time
from selenium import webdriver
driver = webdriver.Chrome(r"C:\Users\Ravi Raushan\Downloads\chromedriver.exe")  
driver.get('http://www.google.com/');
time.sleep(5) 
search_box = driver.find_element_by_name('q')
search_box.send_keys('India')
search_box.submit()
time.sleep(5) 
driver.quit()