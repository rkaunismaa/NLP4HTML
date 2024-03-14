# conda activate selenium

# This scans the list of users from the search pages,
# then compares it to the latest edition of the ...
# MatchProfilesMasterList ...
# and then generates the newest ...
# NewUsers ... list ...

import pickle

import time
import datetime
from datetime import date

from MatchFunctions import *

# Master Profile list ... always specify the most recent master list last!
fnProfileMaster = 'matchLists/MatchProfilesMasterList.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-08-30--10-25.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-09-03--12-21.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-09-06--16-14.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-09-13--09-49.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-09-18--10-20.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-09-25--16-27.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-10-06--07-12.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-10-15--11-39.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-10-22--06-53.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-11-02--05-56.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-11-09--10-18.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-11-16--17-00.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-11-23--06-22.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-11-29--13-57.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-12-06--10-17.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-12-10--14-29.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-12-14--07-42.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-12-21--17-07.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2023-12-28--08-11.txt'

fnProfileMaster = 'matchLists/MatchProfilesMasterList_2024-01-05--11-42.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2024-01-12--06-36.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2024-01-17--10-18.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2024-02-13--07-16.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2024-02-20--06-52.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2024-02-23--13-20.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2024-02-27--06-45.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2024-03-05--09-45.txt'
fnProfileMaster = 'matchLists/MatchProfilesMasterList_2024-03-09--06-16.txt'


with open(fnProfileMaster, "rb") as input_file:
    profileMaster = pickle.load(input_file)

# If this fails to load, make sure you are using the selenium environment!!
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
