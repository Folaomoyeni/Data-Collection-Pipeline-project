from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep

driver = webdriver.Chrome()
URL = 'https://www.rottentomatoes.com/browse/movies_at_home/affiliates:netflix~ratings:pg?page=2'
driver.get(URL)
time.sleep(3)

film_listing = driver.find_element(by=By.XPATH, value ='//*[@data-id="movies_at_home_affiliates:netflix~ratings:pg"]')
a_tag = film_listing.find_element_by_tag_name('a')
link = a_tag.get_attribute('href')
print('href'