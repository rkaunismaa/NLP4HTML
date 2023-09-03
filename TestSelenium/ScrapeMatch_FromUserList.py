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



# yyymmdd_hhmm = '_2023-08-25--08-13' # This has the MOST USERS OF ALL THE UserList files! Consider it a master list!
# # file we read the users from ...
# usersFileName = 'matchLists/matchUserList' + yyymmdd_hhmm + '.txt'

# Let's use the NewUsers file, 
# NewUsers_2023-09-03--12-21.txt
yyymmdd_hhmm = '2023-09-03--12-21' # This should be the most recently created new user list!
# file we read the users from ...
usersFileName = 'matchLists/NewUsers_' + yyymmdd_hhmm + '.txt'

# open the source users file
with open(usersFileName, "rb") as input_file:
    userList = pickle.load(input_file)

# file we write their profiles into ...
profilesFileName = 'matchLists/NewProfiles_' + yyymmdd_hhmm + '.txt'
# with open(profilesFileName, "rb") as fp:   
#     userProfiles = pickle.load(fp)

# This will store all the metadata we want on the user.
userProfiles = []

userNumber = 0
userCount = len(userList)

# startTime = time.time()
# todaysDate = date.today()

driver = createNewDriver()

for testUser in userList:

    userNumber += 1
    profilePage = testUser[1]

    # only scan once ...
    found = False
    for profile in userProfiles:
        profileUrl = profile[0]
        if profileUrl == profilePage:
            found = True
        if found:
            break

    if (not found):

        driver.get(profilePage)

        # scanProfilePage(userNumber, userCount)
        scanProfilePage(userNumber, userCount, driver, userProfiles, profilePage)

        # save the userProfiles to a local file
        if (userNumber % 25) == 0 :
            with open(profilesFileName, "wb") as fp:   #Pickling
                pickle.dump(userProfiles, fp)

endTime = time.time()
elapsedTime = time.strftime("%H:%M:%S", time.gmtime(endTime - startTime))

print(todaysDate.strftime('# Run Date: %A, %B %d, %Y'))
print(f"# Run Time: {elapsedTime}")

# Final save ...
with open(profilesFileName, "wb") as fp:   #Pickling
    pickle.dump(userProfiles, fp)

print("Match Success!")

driver.quit()


