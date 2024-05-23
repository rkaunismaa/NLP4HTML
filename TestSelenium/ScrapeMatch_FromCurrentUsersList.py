# conda activate selenium

# This reads from the most CurrentUsers file,
# and then scans the full profile of every current user, and saves
# the data into CurrentProfiles file, and
# the failed profiles into the FailedCurrentProfiles file.

import pickle

import time
import datetime
from datetime import date

from MatchFunctions import *

todaysDate = date.today()
startTime = time.time()

# now = datetime.datetime.now()
# now = datetime.now()
# yyymmdd_hhmm = now.strftime('%Y-%m-%d--%H-%M')

# grab the name of the lastest CurrentUsers file we will read from
currentusersFileName = get_newest_file_creation_date('matchLists', 'CurrentUsers_')
# set the names of the 2 files we will write the profiles into
profilesFileName = currentusersFileName.replace('CurrentUsers_', 'CurrentProfiles_')
failedProfilesFileName = currentusersFileName.replace('CurrentUsers_', 'FailedCurrentProfiles_')

# open the source users file
with open(currentusersFileName, "rb") as input_file:
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
        scanProfilePage(userNumber, userCount, driver, userProfiles, profilePage, failedProfiles, testUser)

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

# Final save ...
if (len(failedProfiles) > 0) :
    with open(failedProfilesFileName, "wb") as fp:   #Pickling
        pickle.dump(failedProfiles, fp)

print("Match Success!")

# driver.quit()


