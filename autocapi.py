#!/usr/bin/python3

from selenium import webdriver
import cgi
import time

print("content-type:text/plain")
print("Access-Control-Allow-Origin: *")
print()

form_values = cgi.FieldStorage()
fen_string = form_values.getvalue("fen")

#Chrome options
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("--headless")
chrome_opt.add_argument("--no-sandbox")
chrome_opt.add_argument("--disable-dev-shm-usage")

#Setting webdriver
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", chrome_options=chrome_opt)
driver.maximize_window()

fen_url = "https://nextchessmove.com/?fen=" + fen_string

driver.get(fen_url)

time.sleep(5)

calculate_move_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[5]/button")
calculate_move_button.click()

time.sleep(10)

next_move = driver.find_element_by_xpath('//*[@id="ncm-controls"]/div[6]/div/div[1]/div/div/div/a/span')
print(next_move.text)
