from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.common.by import By

# Friday, July 28, 2023
# This runs without problems under the conda environment finance on KAUWITB ...
# conda nlp4html or docker container hfpt_July21 ... it does not work. 

def test_eight_components():


    useChrome = True
    useFireFox = not useChrome

    # IF this fails, then try killing any running instances of brave, then try again ... 
    if useChrome:
        chromeOptions = ChromeOptions()
        chromeOptions.headless = True
        chromeOptions.binary_location = '/snap/bin/brave'
        chromeOptions.add_argument('--remote-debugging-port=9224') #NOT 9222
        driver = webdriver.Chrome(options=chromeOptions)

    if useFireFox:
        firefoxOptions = FireFoxOptions()
        firefoxOptions.headless = True
        # interesting ... this next line will break this app ... so yeah, don't use it
       # firefoxOptions.binary_location = '/snap/bin/firefox'
        driver = webdriver.Firefox(options=firefoxOptions)

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
    
    print("Success!!")

    driver.quit()

test_eight_components()
