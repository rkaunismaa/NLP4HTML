import pickle
import requests
import shutil
import os

import time
from datetime import date

from MatchFunctions import *

# What we start with ...
matchUsers = 'matchLists/matchUserList.txt'
matchProfiles = 'matchLists/matchProfiles.txt' 
# override to test stuff ...
matchProfiles = 'matchLists/masterProfiles.txt' 

# What we finish with ...
missedUsersFn = 'matchLists/missedUsers.txt'
missedProfilesFn = 'matchLists/missedProfiles.txt'

with open(matchUsers, "rb") as input_file:
    users = pickle.load(input_file)

with open(matchProfiles, "rb") as input_file:
    profiles = pickle.load(input_file)

# There will be users that did not scan properly, 
# and so there will be no profile. 
# Identify those missed users, and place them into a new file

missedUsers = []
for user in users:

    userName = user[0]
    userUrl = user[1]

    found = False
    for profile in profiles:
        profileUrl = profile[0]
        if profileUrl == userUrl:
            found = True
        if found:
            break

    if (not found):
        missedUsers.append( (userName, userUrl) )

# Persist these missed users into a file
# with open(missedUsersFn, "wb") as fp:   
#     pickle.dump(missedUsers, fp)

chromeOptions = ChromeOptions()
chromeOptions.headless = True
chromeOptions.binary_location = '/snap/bin/brave'
chromeOptions.add_argument('--remote-debugging-port=9224') 
driver = webdriver.Chrome(options=chromeOptions)

userNumber = 0
userCount = len(missedUsers)

# This will store all the metadata we want on the user.
userProfiles = []

startTime = time.time()
todaysDate = date.today()

for testUser in missedUsers:

    userNumber += 1
    profilePage = testUser[1]

    driver.get(profilePage)

    # scanProfilePage(userNumber, userCount)
    scanProfilePage(userNumber, userCount, driver, userProfiles, profilePage)

driver.quit()

endTime = time.time()
elapsedTime = time.strftime("%H:%M:%S", time.gmtime(endTime - startTime))

print(todaysDate.strftime('# Run Date: %A, %B %d, %Y'))
print(f"# Run Time: {elapsedTime}")

# Save the missed userProfiles to a local file
with open(missedProfilesFn, "wb") as fp:   #Pickling
    pickle.dump(userProfiles, fp)

print("Match Success!")







    



    


    