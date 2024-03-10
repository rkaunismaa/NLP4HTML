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

fileName = 'matchLists/FailedURLNotFoundProfiles_2024-03-09--10-44.txt'


with open(fileName, "rb") as input_file:
    profiles = pickle.load(input_file)

userNumber = 0
userCount = len(profiles)

# This will store all the metadata we want on the user.
userProfiles = []
failedProfiles = []

# If this fails to load, make sure you are using the selenium environment!!
driver = createNewDriver()

if driver is not None:

    profileNotAvailable = 'Profile Not Available'

    for profile in profiles:

        userNumber += 1

        if (profile[1] == profileNotAvailable):

            print(userNumber, '/', userCount, profileNotAvailable)

        else:

            profilePage = profile[0]

            print(userNumber, '/', userCount, profilePage)

            # load the profilePage ...
            driver.get(profilePage)

            # scanProfilePage(userNumber, userCount)
            scanProfilePage(userNumber, userCount, driver, userProfiles, profilePage, failedProfiles, profile)


    # close the driver ... we are done with it ..
    driver.quit()

    # file we write their profiles into ...
    profilesFileName = 'matchLists/ValidatedProfiles_' + yyymmdd_hhmm + '.txt'
    # with open(profilesFileName, "rb") as fp:   
    #     userProfiles = pickle.load(fp)

    # file we write the failed profiles into ...
    failedProfilesFileName = 'matchLists/FailedValidatedProfiles_' + yyymmdd_hhmm + '.txt'

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

        
    

    