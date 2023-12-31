# conda activate selenium

from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pickle

import time
import datetime
from datetime import date

from MatchFunctions import *

todaysDate = date.today()
startTime = time.time()

now = datetime.datetime.now()
yyymmdd_hhmm = now.strftime('%Y-%m-%d--%H-%M')

chromedriver_path = '/usr/local/bin/chromedriver'
chromeService = ChromeService(executable_path=chromedriver_path)

chromeOptions = ChromeOptions()
chromeOptions.headless = True
chromeOptions.binary_location = '/usr/bin/brave-browser'
chromeOptions.add_argument('--remote-debugging-port=9224') 

driver = webdriver.Chrome(options = chromeOptions,  service=chromeService)

# driver.quit()

# chromeOptions = ChromeOptions()
# # chromeOptions.headless = True
# # chromeOptions.binary_location = '/snap/bin/brave'
# chromeOptions.binary_location = '/usr/bin/google-chrome'
# chromeOptions.add_argument('--remote-debugging-port=9224') 
# driver = webdriver.Chrome(options=chromeOptions)

# driver = webdriver.Chrome(executable_path='/usr/bin/brave-browser')

# chromeOptions = ChromeOptions()
# # chromeOptions.headless = True
# # chromeOptions.binary_location = '/snap/bin/brave'
# chromeOptions.binary_location = '/usr/bin/brave-browser'
# chromeOptions.add_argument('--remote-debugging-port=9224') 
# driver = webdriver.Chrome(options=chromeOptions)

# now set in MatchFunctions.py ...
# targetSearchPages = [
#     ('Top Picks' ,     'https://www.match.com/search?sortBy=1',  True),
#     ('Photo Count' ,   'https://www.match.com/search?sortBy=2',  True),
#     ('Age' ,           'https://www.match.com/search?sortBy=3',  True),
#     ('Activity Date' , 'https://www.match.com/search?sortBy=4',  True),
#     ('Newest First' ,  'https://www.match.com/search?sortBy=6',  True),
#     ('Mutual Search' , 'https://www.match.com/search?sortBy=9',  True),
#     ('Reverse Search' ,'https://www.match.com/search?sortBy=10', True),
#     ('Distance' ,      'https://www.match.com/search?sortBy=11', True)
# ]
 
userList = []
profileIDS = []   
profileCount = 0
exceptionCount = 0

scanDepth = 24

# Launch the scan of all the target search pages ...
for tsPage in targetSearchPages:

    searchPage = tsPage[1]
    scanThisPage = tsPage[2]

    if scanThisPage == True:

        driver.get(searchPage)

        # Set an implicit wait of 5 seconds
        driver.implicitly_wait(5)

        for _ in range(scanDepth):
            # scanSearchPage()
            scanSearchPage(driver, profileIDS, userList)
            driver.execute_script("window.scrollBy(0,1000)","")
            driver.implicitly_wait(5)

# Let's save this list, shall we ...
# Save the userProfiles to a local file
fileName = 'matchLists/matchUserList_' + yyymmdd_hhmm + '.txt'
with open(fileName, "wb") as fp:   
    pickle.dump(userList, fp)

# 269 ... 
print(len(userList))

# This will store all the metadata we want on the user.
userProfiles = []

userNumber = 0
userCount = len(userList)

# startTime = time.time()
# todaysDate = date.today()

for testUser in userList:

    userNumber += 1
    profilePage = testUser[1]

    driver.get(profilePage)

    # scanProfilePage(userNumber, userCount)
    scanProfilePage(userNumber, userCount, driver, userProfiles, profilePage)


endTime = time.time()
elapsedTime = time.strftime("%H:%M:%S", time.gmtime(endTime - startTime))

print(todaysDate.strftime('# Run Date: %A, %B %d, %Y'))
print(f"# Run Time: {elapsedTime}")

# Save the userProfiles to a local file
fileName = 'matchLists/matchProfiles_' + yyymmdd_hhmm + '.txt'
with open(fileName, "wb") as fp:   #Pickling
    pickle.dump(userProfiles, fp)

print("Match Success!")


driver.quit()


