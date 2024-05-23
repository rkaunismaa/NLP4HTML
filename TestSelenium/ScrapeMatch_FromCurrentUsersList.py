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

print(f'Found {len(userList)} users to scan.')

# open the CurrentProfiles file ... this may not exist!
userProfiles = []
if os.path.isfile(profilesFileName):

    with open(profilesFileName, "rb") as input_file:
        userProfiles = pickle.load(input_file)

    print(f'Found {len(userProfiles)} existing profiles to skip.')
    
    # remove from userList any profile that exists in userProfiles
    existingProfiles = 0
    for profile in userProfiles:
        profileUrl = profile[0]
        for user in userList:
            userUrl = user[1]
            if profileUrl == userUrl:
                existingProfiles += 1
                userList.remove(user)

print(f'After finding {existingProfiles} existing profiles, {len(userList)} users remain to scrape ....')


# This will store all the metadata we want on the user.
#userProfiles = []
failedProfiles = []

userNumber = 0
userCount = len(userList)

# startTime = time.time()
# todaysDate = date.today()

driver = createNewDriver()

for testUser in userList:

    userNumber += 1
    profilePage = testUser[1]

    driver.get(profilePage)

    # scanProfilePage(userNumber, userCount)
    scanProfilePage(userNumber, userCount, driver, userProfiles, profilePage, failedProfiles, testUser)

    # save the userProfiles to a local file
    if (userNumber % 25) == 0 :
        with open(profilesFileName, "wb") as fp:   #Pickling
            pickle.dump(userProfiles, fp)

    if (len(failedProfiles) > 5) :
        break
        
endTime = time.time()
elapsedTime = time.strftime("%H:%M:%S", time.gmtime(endTime - startTime))

print(todaysDate.strftime('# Run Date: %A, %B %d, %Y'))
print(f"# Run Time: {elapsedTime}")

# Final save ...
with open(profilesFileName, "wb") as fp:   #Pickling
    pickle.dump(userProfiles, fp)

# Final save ...
# if (len(failedProfiles) > 0) :
#     with open(failedProfilesFileName, "wb") as fp:   #Pickling
#         pickle.dump(failedProfiles, fp)

print("Match Success!")

# driver.quit()


