import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


username = os.environ.get("LINKEDIN_UNAME")
password = os.environ.get("LINKEDIN_PWD")
phone_number = os.environ.get("PHONE")

linkedin_link = 'https://www.linkedin.com/jobs/search/?f_AL=true&geoId=105117694&keywords=python%20developer&location=Sweden&sortBy=R'
chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(linkedin_link)

time.sleep(3)
sign_in = driver.find_element_by_xpath("//*[@id='main-content']/div/form/p/button")
sign_in.click()

time.sleep(5)

email_input = driver.find_element_by_xpath("//*[@id='session_key']")
email_input.send_keys(username)
email_input = driver.find_element_by_xpath("//*[@id='session_password']")
email_input.send_keys(password)
sign_in_button = driver.find_element_by_xpath("//*[@id='main-content']/div/div/div/form/button")
sign_in_button.click()

# time.sleep(5)

driver.get(linkedin_link)
time.sleep(6)

all_ads = driver.find_elements_by_class_name('job-card-container')

for ad in all_ads:
    ad.click()
    time.sleep(2)

    try:
        easy_apply_button = driver.find_element_by_class_name("jobs-apply-button--top-card")
        easy_apply_button.click()

        submit_button = driver.find_element_by_class_name('artdeco-button--primary')
        if submit_button.is_displayed() and submit_button.text == 'Submit application':
            submit_button.click()
            time.sleep(2)
            close_button_1 = driver.find_element_by_class_name("mercado-match")
            close_button_1.click()


        else:
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(4)
            discard_button = driver.find_element_by_class_name('artdeco-button--secondary')
            discard_button.click()


        # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()


# easy_apply_button = driver.find_element_by_xpath("//*[@id='ember364']")
# easy_apply_button.click()
#
# phone_input = driver.find_element_by_xpath("//*[@id='urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3028642397,9,phoneNumber~nationalNumber)']")
# phone_input.send_keys(phone)
#
# submit = driver.find_element_by_xpath("//*[@id='ember386']")
# submit.click()
#
# close_confirmation = driver.find_element_by_xpath("//*[@id='ember506']/li-icon/svg")
# close_confirmation.click()
# email = driver.find_element_by_id("#email-or-phone")
# email.send_keys("hi")
# driver.close()
# os.environ["name"] = "Alaa"
# USER = os.getenv('name')
# print(username)
