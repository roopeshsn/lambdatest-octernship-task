from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def get_logs():
    capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
    chrome_options = Options()
    driver = webdriver.Chrome(desired_capabilities=capabilities, options=chrome_options)
    driver.get("https://www.lambdatest.com/")

    links = driver.find_elements(By.CLASS_NAME, "nav-link")
#((//div[@class='row'])[3]//h3)[3]
    for link in links:
        if link.tag_name == 'button':
            link.click()
            time.sleep(1)
            parent = link.find_element(By.XPATH, "..")
            unordered_lists = parent.find_elements(By.TAG_NAME, 'ul')
            for i in range(0, len(unordered_lists)):
                a_tags = unordered_lists[i].find_elements(By.TAG_NAME, 'a')
                for j in range(0, len(a_tags)):
                    # ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
                    # your_element = WebDriverWait(driver, 3, ignored_exceptions=ignored_exceptions) \
                    #     .until(expected_conditions.presence_of_element_located((By.ID, my_element_id)))
                    a_tags[j].click()
    logs = driver.get_log('performance')
    with open('/data/network_logs.json', 'a') as f:
        for log in logs:
            f.write(json.dumps(log) + '\n')
    driver.quit()


if __name__ == '__main__':
    get_logs()
