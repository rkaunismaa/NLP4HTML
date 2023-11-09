# conda activate selenium

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
yyymmdd_hhmm = '2023-09-06--16-14'
yyymmdd_hhmm = '2023-09-13--09-49'
yyymmdd_hhmm = '2023-09-18--10-20'
yyymmdd_hhmm = '2023-09-25--16-27'
yyymmdd_hhmm = '2023-10-06--07-12'
yyymmdd_hhmm = '2023-10-15--11-39'
yyymmdd_hhmm = '2023-10-22--06-53'
yyymmdd_hhmm = '2023-11-02--05-56'
yyymmdd_hhmm = '2023-11-09--10-18'


# failed profiles list ...
usersFileName = 'matchLists/FailedProfiles_' + yyymmdd_hhmm + '.txt'

# open the source users file
with open(usersFileName, "rb") as input_file:
    userList = pickle.load(input_file)

# existing New Profiles we want to APPEND rescanned profiles into ...
profilesFileName = 'matchLists/NewProfiles_' + yyymmdd_hhmm + '.txt'
with open(profilesFileName, "rb") as fp:   
    newProfiles = pickle.load(fp)

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


# We now want to append to the newProfiles list the 
# rescanned userProfiles
updatedNewProfiles = newProfiles + userProfiles
# and save ...
updatedProfilesFileName = 'matchLists/UpdatedNewProfiles_' + yyymmdd_hhmm + '.txt'
with open(updatedProfilesFileName, "wb") as fp:   #Pickling
    pickle.dump(updatedNewProfiles, fp)

print("Match Success!")

endTime = time.time()
elapsedTime = time.strftime("%H:%M:%S", time.gmtime(endTime - startTime))

print(todaysDate.strftime('# Run Date: %A, %B %d, %Y'))
print(f"# Run Time: {elapsedTime}")

driver.quit()


