# Wednesday, May 22, 2024

# This scans the list of users from the search pages,
# and then generates the current ...
# CurrentUsers ... list ...

# conda activate selenium

import pickle

import time
import datetime
from datetime import date

from MatchFunctions import *

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

    print(f'There are {len(userList)} current users!')
    
    # Save the userProfiles to a local file
    fnCurrentUsers = 'matchLists/CurrentUsers_' + yyymmdd_hhmm + '.txt'
    with open(fnCurrentUsers, "wb") as fp:   #Pickling
        pickle.dump(userList, fp)

    endTime = time.time()
    elapsedTime = time.strftime("%H:%M:%S", time.gmtime(endTime - startTime))

    print(todaysDate.strftime('# Run Date: %A, %B %d, %Y'))
    print(f"# Run Time: {elapsedTime}")
