# This program will read from the current MatchProfilesMasterList file, and 
# re-scan all profiles for the most current profiles.

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

# Master Profile list ... always specify the most recent master list last!
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2024-02-27--06-45.txt'

with open(fnProfileMaster, "rb") as input_file:
    profileMaster = pickle.load(input_file)

userNumber = 0
userCount = len(profileMaster)

# This will store all the metadata we want on the user.
userProfiles = []
failedProfiles = []

# If this fails to load, make sure you are using the selenium environment!!
driver = createNewDriver()

if (driver is not None):

    # loop through the profileMaster file ...

    for profile in profileMaster:

        # we only need the one field ...
        # userProfiles.append( (profilePage, personName, personAgeLocation, personSubscriber, personLastActive, personBannerHeading, personBannerText, personSummary, imageList) )
        profilePage = profile[0]

        # print(profilePage)
        userNumber += 1

        # load the profilePage ...
        driver.get(profilePage)

        # scanProfilePage(userNumber, userCount)
        scanProfilePage(userNumber, userCount, driver, userProfiles, profilePage, failedProfiles, profile)

    # we are done with the driver ... close it down ...
    driver.quit()


# file we write their profiles into ...
profilesFileName = 'matchLists/ValidatedProfiles_' + yyymmdd_hhmm + '.txt'
# with open(profilesFileName, "rb") as fp:   
#     userProfiles = pickle.load(fp)

# file we write the failed profiles into ...
failedProfilesFileName = 'matchLists/FailedURLNotFoundProfiles_' + yyymmdd_hhmm + '.txt'

# Final save ...
with open(profilesFileName, "wb") as fp:   #Pickling
    pickle.dump(userProfiles, fp)

# Final save ...
if (len(failedProfiles) > 0) :
    with open(failedProfilesFileName, "wb") as fp:   #Pickling
        pickle.dump(failedProfiles, fp)

endTime = time.time()
elapsedTime = time.strftime("%H:%M:%S", time.gmtime(endTime - startTime))

print(todaysDate.strftime('# Run Date: %A, %B %d, %Y'))
print(f"# Run Time: {elapsedTime}")



