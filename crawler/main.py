import os
import shutil

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import json

from selenium.webdriver.common.by import By

ACCEPT_COOKIES_ELEMENT_XPATH = '//*[@id="__next"]/div[2]/div/div/div[2]/div/span[1]'
PLATFORM_ELEMENT_XPATH = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[1]/div[1]/a'
ENTERPRISE_ELEMENT_XPATH = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/a[1]'
RESOURCES_ELEMENT_XPATH = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[2]/button'
DEVELOPERS_ELEMENT_XPATH = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[3]/button'
PRICING_ELEMENT_XPATH = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/a[2]'
LOGIN_ELEMENT_XPATH = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[2]/a[1]'
BOOK_A_DEMO_ELEMENT_XPATH = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[2]/button'
SIGN_UP_XPATH = '//*[@id="header"]/nav/div/div/div[2]/div/div/div[2]/a[2]'


def get_logs():
    capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
    chrome_options = Options()
    driver = webdriver.Chrome(desired_capabilities=capabilities, options=chrome_options)
    driver.get("https://www.lambdatest.com/")

    time.sleep(2)

    # Accept cookies
    click_button(driver, ACCEPT_COOKIES_ELEMENT_XPATH)

    # Platform nav link
    click_nav_link(driver, PLATFORM_ELEMENT_XPATH)
    time.sleep(2)
    driver.back()
    hover_platform(driver)

    for i in range(1, 7):
        platform_link = driver.find_element(By.XPATH,
                                            '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/ul/li[{0}]/a'.format(
                                                i))
        time.sleep(2)
        if i == 6:
            scroll_page(driver)
        platform_link.click()
        time.sleep(2)
        driver.back()
        if i != 6:
            hover_platform(driver)

    hover_platform(driver)
    for i in range(1, 7):

        # sub nav link inside the platform dropdown
        platform_link = driver.find_element(By.XPATH,
                                            '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/ul/li[{0}]/a'.format(
                                                i))
        time.sleep(2)
        if i == 6:
            scroll_page(driver)
        platform_link.click()
        time.sleep(2)
        driver.back()
        if i != 6:
            hover_platform(driver)

    # # Enterprise nav link
    # click_nav_link(driver, ENTERPRISE_ELEMENT_XPATH)
    # time.sleep(2)
    # driver.back()
    #
    # # Resources nav link
    # click_nav_link(driver, RESOURCES_ELEMENT_XPATH)
    # for i in range(1, 7):
    #     resources_link = driver.find_element(By.XPATH,
    #                                          '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/ul/li[{0}]/a'.format(
    #                                              i))
    #     time.sleep(2)
    #     if i == 6:
    #         scroll_page(driver)
    #     resources_link.click()
    #     time.sleep(2)
    #     driver.back()
    #     if i != 6:
    #         click_nav_link(driver, RESOURCES_ELEMENT_XPATH)
    #
    # time.sleep(2)
    # click_nav_link(driver, RESOURCES_ELEMENT_XPATH)
    # time.sleep(2)
    # for i in range(1, 7):
    #     resources_link = driver.find_element(By.XPATH,
    #                                          '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div/div[2]/ul/li[{0}]/a'.format(
    #                                              i))
    #     if i == 6:
    #         scroll_page(driver)
    #     resources_link.click()
    #     time.sleep(2)
    #     driver.back()
    #     if i != 6:
    #         click_nav_link(driver, RESOURCES_ELEMENT_XPATH)
    #
    # # Developers nav link
    # click_nav_link(driver, DEVELOPERS_ELEMENT_XPATH)
    # for i in range(1, 5):
    #     developers_link = driver.find_element(By.XPATH,
    #                                           '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div[1]/ul/li[{0}]/a'.format(
    #                                               i))
    #     time.sleep(2)
    #     developers_link.click()
    #     time.sleep(2)
    #     driver.back()
    #     if i != 4:
    #         click_nav_link(driver, DEVELOPERS_ELEMENT_XPATH)
    # click_nav_link(driver, DEVELOPERS_ELEMENT_XPATH)
    # for i in range(1, 5):
    #     developers_link = driver.find_element(By.XPATH,
    #                                           '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div[2]/ul/li[{0}]/a'.format(
    #                                               i))
    #     time.sleep(2)
    #     if i != 4:
    #         developers_link.click()
    #         driver.back()
    #         click_nav_link(driver, DEVELOPERS_ELEMENT_XPATH)
    #
    # # Pricing nav link
    # click_nav_link(driver, PRICING_ELEMENT_XPATH)
    # time.sleep(2)
    # driver.back()
    #
    # # Login nav link
    # click_nav_link(driver, LOGIN_ELEMENT_XPATH)
    # time.sleep(2)
    # driver.back()
    #
    # # "Book a Demo" nav link -> It's a popup
    #
    # # "Sign Up" nav link
    # click_nav_link(driver, SIGN_UP_XPATH)
    # time.sleep(2)
    # driver.back()

    logs = driver.get_log('performance')
    source_file_path = 'data/network_logs.json'
    destination_file_path = '../data/network_logs.json'
    try:
        os.remove(source_file_path)
    except FileNotFoundError:
        print(f"{source_file_path} not found.")
        
    with open('data/network_logs.json', 'a') as f:
        f.write('{' + '\n')
        f.write('"logs"' + ':' + ' ' + '[' + '\n')
        log_count = len(logs)
        for idx, log in enumerate(logs):
            f.write(json.dumps(log))
            if idx != log_count - 1:
                f.write(',')
            f.write('\n')
        f.write(']' + '\n' + '}')

    try:
        os.remove(destination_file_path)
    except FileNotFoundError:
        print(f"{destination_file_path} not found.")

    shutil.copy(source_file_path, destination_file_path)
    driver.quit()


def hover_platform(driver):
    actions = ActionChains(driver)
    platform_button = driver.find_element(By.XPATH,
                                          '//*[@id="header"]/nav/div/div/div[2]/div/div/div[1]/div[1]/div[1]/a')
    actions.move_to_element(platform_button)
    actions.perform()


def click_nav_link(driver, x_path):
    nav_link = driver.find_element(By.XPATH, x_path)
    nav_link.click()


def click_button(driver, x_path):
    button = driver.find_element(By.XPATH, x_path)
    button.click()


def scroll_page(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)


if __name__ == '__main__':
    get_logs()
