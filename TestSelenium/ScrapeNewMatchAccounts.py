# conda activate selenium

import pickle

import time
import datetime
from datetime import date

from MatchFunctions import *

# Master Profile list ... always specify the most recent master list last!
fnProfileMaster = 'matchLists/MatchProfilesMasterList.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-08-30--10-25.txt'

with open(fnProfileMaster, "rb") as input_file:
    profileMaster = pickle.load(input_file)

driver = createNewDriver()

if (driver is not None) :

    todaysDate = date.today()
    startTime = time.time()

    now = datetime.datetime.now()
    yyymmdd_hhmm = now.strftime('%Y-%m-%d--%H-%M')

    userList = []
    profileIDS = []   

    scanDepth = 12

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
                driver.execute_script("window.scrollBy(0,800)","")
                driver.implicitly_wait(5)

    # we are done with the driver. Close the driver.
    driver.quit()

    # Scan through the userList, and determine which users 
    # are not found in the profileMaster, 
    newUserList = []
    for user in userList:

        personName = user[0]
        profileId = user[2]

        bExists = scanProfiles4MatchId(profileMaster, user[2])
        if not bExists:
            print(f'New User {personName} => {profileId} added to the NewUsers List!')
            newUserList.append(user)
        else:
            print(f'User {personName} => {profileId} is already in the Master List!')

    print(f'There are {len(newUserList)} new users!')
    
    # Save the userProfiles to a local file
    fnNewUsers = 'matchLists/NewUsers_' + yyymmdd_hhmm + '.txt'
    with open(fnNewUsers, "wb") as fp:   #Pickling
        pickle.dump(newUserList, fp)

    # write the new users to a file
    endTime = time.time()
    elapsedTime = time.strftime("%H:%M:%S", time.gmtime(endTime - startTime))

    print(todaysDate.strftime('# Run Date: %A, %B %d, %Y'))
    print(f"# Run Time: {elapsedTime}")
