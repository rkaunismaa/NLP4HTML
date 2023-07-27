# https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/test_first_script.py#L6

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_eight_components():

    # driver = webdriver.Chrome()
    # PATH_TO_GECKO_DRIVER = '/usr/local/bin'
    PATH_TO_GECKO_DRIVER = '/home/rob/Data/Documents/SeleniumDrivers'
   # driver = webdriver.Firefox(executable_path=PATH_TO_GECKO_DRIVER)

    # Let's try Brave with the chromium driver ...
    PATH_TO_BRAVE = '/snap/bin/brave'
    PATH_TO_CHROMIUM_DRIVER = '/usr/local/bin'

    driver = webdriver.Chrome(executable_path=PATH_TO_GECKO_DRIVER)

    # Replace 'PATH_TO_CHROMEDRIVER' with the actual path to the chromedriver executable
    brave_options = webdriver.ChromeOptions()
    brave_options.binary_location = PATH_TO_BRAVE  # Replace with the actual path to Brave browser binary

    # driver = webdriver.Chrome(executable_path=PATH_TO_CHROMIUM_DRIVER, options=brave_options)

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.quit()


test_eight_components()