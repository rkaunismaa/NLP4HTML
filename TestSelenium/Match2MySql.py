import pickle
import requests
import shutil
import os

# Save the userProfiles to a local file
fileName = 'matchProfiles.txt'

with open(fileName, "rb") as input_file:
    userProfiles = pickle.load(input_file)

imageFolderRoot = 'images/'

for user in userProfiles:

    profileHomePage = user[0]
    profileParts = profileHomePage.split("/")
    profileId = profileParts[-1]

    profileFolder = imageFolderRoot + profileId
    if not os.path.exists(profileFolder):
        os.makedirs(profileFolder)

    imageList = user[4]

    for image in imageList:

        url = image[0]
        urlParts = url.split("/")
        iName = profileFolder + "/" + urlParts[-1]

        res = requests.get(url, stream = True)

        if res.status_code == 200:
            with open(iName,'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',iName)
        else:
            print('Image Couldn\'t be retrieved')


