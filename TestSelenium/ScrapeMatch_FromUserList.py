# conda activate selenium

# This reads from the most current NewUsers file,
# and then scans the full profile of every new user, and saves
# the data into NewProfiles file, and
# the failed profiles into the FailedProfiles file.

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
yyymmdd_hhmm = '2023-11-16--17-00'
yyymmdd_hhmm = '2023-11-23--06-22'
yyymmdd_hhmm = '2023-11-29--13-57'
yyymmdd_hhmm = '2023-12-06--10-17'
yyymmdd_hhmm = '2023-12-10--14-29'
yyymmdd_hhmm = '2023-12-14--07-42'
yyymmdd_hhmm = '2023-12-21--17-07'
yyymmdd_hhmm = '2023-12-28--08-11'

yyymmdd_hhmm = '2024-01-05--11-42'
yyymmdd_hhmm = '2024-01-12--06-36'
yyymmdd_hhmm = '2024-01-17--10-18'
yyymmdd_hhmm = '2024-02-13--07-16'
yyymmdd_hhmm = '2024-02-20--06-52'
yyymmdd_hhmm = '2024-02-23--13-20'
yyymmdd_hhmm = '2024-02-27--06-45'
yyymmdd_hhmm = '2024-03-05--09-45'
yyymmdd_hhmm = '2024-03-09--06-16'
yyymmdd_hhmm = '2024-03-14--10-29'
yyymmdd_hhmm = '2024-03-19--10-08'
yyymmdd_hhmm = '2024-03-28--07-12'
yyymmdd_hhmm = '2024-04-03--09-17'
yyymmdd_hhmm = '2024-04-10--18-18'
yyymmdd_hhmm = '2024-04-17--08-36'
yyymmdd_hhmm = '2024-04-25--17-00'
yyymmdd_hhmm = '2024-05-03--10-08'
yyymmdd_hhmm = '2024-05-08--08-09'
yyymmdd_hhmm = '2024-05-17--08-39'


# file we read the users from ...
usersFileName = 'matchLists/NewUsers_' + yyymmdd_hhmm + '.txt'

# open the source users file
with open(usersFileName, "rb") as input_file:
    userList = pickle.load(input_file)

# file we write their profiles into ...
profilesFileName = 'matchLists/NewProfiles_' + yyymmdd_hhmm + '.txt'
# with open(profilesFileName, "rb") as fp:   
#     userProfiles = pickle.load(fp)

# file we write the failed profiles into ...
failedProfilesFileName = 'matchLists/FailedProfiles_' + yyymmdd_hhmm + '.txt'

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


