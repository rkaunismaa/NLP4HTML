from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

# chromeService = ChromeService(executable_path='/usr/local/bin/chromedriver', port=9224)
# chromeService = ChromeService(executable_path='/usr/local/bin/chromedriver')

chromeOptions = ChromeOptions()
chromeOptions.binary_location = "/usr/bin/brave-browser"
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-gpu ")
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--remote-debugging-port=9224') 
chromeOptions.add_argument("--user-data-dir=/home/rob/.config/BraveSoftware/Brave-Browser")

# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",  options = chromeOptions, port=9224)
# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",  chrome_options = chromeOptions)
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",  options = chromeOptions, port=9224)
# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

myPage = "https://www.match.com/profile/W5z7CrtS5fF62opPzSuCfg2"

driver.get(myPage)

driver.quit()

