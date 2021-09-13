from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver93', options=chrome_options)
import time
from datetime import date
import json

with open("config.json","r") as fb:

    json = json.load(fb)
    driver.get(json['url'])
    for p in json['persons']:
        print("Starting %s, %s" %( p['first'], p['last']))

        driver.get(json['url'])
        time.sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Guest Screening')]").click()
        driver.find_element_by_xpath("//label[@for='guest_isStudent']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='guest_first_name']").send_keys(p['first'])
        driver.find_element_by_xpath("//input[@id='guest_last_name']").send_keys(p['last'])
        driver.find_element_by_xpath("//input[@id='guest_email']").send_keys(p['email'])
        driver.find_element_by_xpath("//label[@id='other_label']").click()
        driver.find_element_by_xpath("//input[@id='guest_location']").send_keys(["school"])
        driver.find_element_by_xpath("//div[@id='btnDailyScreeningSubmit']/button").click()
        time.sleep(1)
        driver.find_element_by_xpath("//label[@for='q1no']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//label[@for='q2no']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//label[@for='q3no']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//label[@for='q4no']").click()
        driver.find_element_by_xpath("//*[contains(text(),'Submit Screening')]").click()
        time.sleep(3)
        today = date.today()
        driver.save_screenshot('./screeners/%s_%s_%s.png' % (p['first'], p['last'], today))
        print("Completed %s, %s" % (p['first'], p['last']))
print("ALL PERSONS COMPLETED")
driver.close()
driver.quit()