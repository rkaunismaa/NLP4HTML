import pickle
import requests
import shutil
import os
from os.path import exists


from MatchFunctions import *

fileName = get_newest_file_creation_date('matchLists', 'CurrentProfiles_')

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


