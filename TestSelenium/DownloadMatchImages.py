import pickle
import requests
import shutil
import os
from os.path import exists

# Save the userProfiles to a local file
fileName = 'matchLists/masterProfiles_2023-08-18--17-38.txt' 
fileName = 'matchLists/masterProfiles_2023-08-21--08-54.txt' 
fileName = 'matchLists/masterProfiles_2023-08-23--07-40.txt'
fileName = 'matchLists/matchProfiles_2023-08-25--08-13.txt'
fileName = 'matchLists/masterProfiles_2023-08-25--08-13.txt'

fileName = 'matchLists/MatchProfilesMasterList.txt'

fileName = 'matchLists/NewProfiles_2023-08-30--10-25.txt'

fileName = 'matchLists/NewProfiles_2023-09-03--12-21.txt'

fileName = 'matchLists/NewProfiles_2023-09-06--16-14.txt'

fileName = 'matchLists/NewProfiles_2023-09-13--09-49.txt'

fileName = 'matchLists/NewProfiles_2023-09-18--10-20.txt'

fileName = 'matchLists/NewProfiles_2023-09-25--16-27.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-10-06--07-12.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-10-15--11-39.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-10-22--06-53.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-11-02--05-56.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-11-09--10-18.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-11-16--17-00.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-11-23--06-22.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-11-29--13-57.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-12-06--10-17.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-12-10--14-29.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-12-14--07-42.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-12-21--17-07.txt'

fileName = 'matchLists/UpdatedNewProfiles_2023-12-28--08-11.txt'


fileName = 'matchLists/UpdatedNewProfiles_2024-01-05--11-42.txt'
fileName = 'matchLists/UpdatedNewProfiles_2024-01-12--06-36.txt'
fileName = 'matchLists/UpdatedNewProfiles_2024-01-17--10-18.txt'
fileName = 'matchLists/UpdatedNewProfiles_2024-02-13--07-16.txt'
fileName = 'matchLists/UpdatedNewProfiles_2024-02-20--06-52.txt'


with open(fileName, "rb") as input_file:
    userProfiles = pickle.load(input_file)

imageFolderRoot = 'matchImages/'

for user in userProfiles:

    profileHomePage = user[0]
    profileParts = profileHomePage.split("/")
    profileId = profileParts[-1]

    profileFolder = imageFolderRoot + profileId
    if not os.path.exists(profileFolder):
        os.makedirs(profileFolder)

    imageList = user[8]

    for image in imageList:

        url = image[0]
        urlParts = url.split("/")
        iName = profileFolder + "/" + urlParts[-1]

        # only download if the file does not exist ...
        if exists(iName):
            print(f'{url} => Image already downloaded!')
        else:
            res = requests.get(url, stream = True)

            if res.status_code == 200:

                with open(iName,'wb') as f:
                    shutil.copyfileobj(res.raw, f)

                print(f'{url} => Image sucessfully Downloaded!')
            else:
                print(f'{url} => Could not be retrieved')


