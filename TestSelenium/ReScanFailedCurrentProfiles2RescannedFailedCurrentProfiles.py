# conda activate selenium

import pickle

import time
import datetime
from datetime import date

from MatchFunctions import *

todaysDate = date.today()
startTime = time.time()

# CurrentUsers contains the profilepageurl for existing users
# CurrentProfiles contains successfully scanned profiles from CurrentUsers
# FailedCurrentProfiles contains the failed profiles from CurrentUsers

# So Open up CurrentUsers in read mode, loop through the list, for each user,
# scan to see if that user is in the CurrentProfiles list, if it is, move onto the next record, 
# if not, then scan the profile page, if it is successful, add it to the CurrentProfiles list, 
# and save the CurrentProfiles list every time a new record is appended ... and if you start
# running into failures during scanning, then abort ...


# grab the name of the lastest FailedCurrentProfiles_ file we will read from
currentProfiles = get_newest_file_creation_date('matchLists', 'CurrentProfiles_')
# set the names of the 2 files we will write the profiles into
rescannedfailedCurrentProfiles = failedCurrentProfiles.replace('FailedCurrentProfiles_', 'RescannedFailedCurrentProfiles_')

# open the failedCurrentProfiles users file
with open(failedCurrentProfiles, "rb") as input_file:
    userList = pickle.load(input_file)

# This will store all the metadata we want on the user.
userProfiles = []

failedProfiles = []

userNumber = 0
userCount = len(userList)

# startTime = time.time()
# todaysDate = date.today()

driver = createNewDriver()

for testUser in userList:

    userNumber += 1
    profilePage = testUser[1]

    if (profilePage != 'Profile Not Available'):

        driver.get(profilePage)

        # scanProfilePage(userNumber, userCount)
        scanProfilePage(userNumber, userCount, driver, userProfiles, profilePage, failedProfiles, testUser)


# and save ...
with open(rescannedfailedCurrentProfiles, "wb") as fp:   #Pickling
    pickle.dump(userProfiles, fp)

print("Match Success!")

endTime = time.time()
elapsedTime = time.strftime("%H:%M:%S", time.gmtime(endTime - startTime))

print(todaysDate.strftime('# Run Date: %A, %B %d, %Y'))
print(f"# Run Time: {elapsedTime}")

# driver.quit()


