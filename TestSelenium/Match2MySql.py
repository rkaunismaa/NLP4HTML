import pickle
import requests
import shutil

# Save the userProfiles to a local file
fileName = 'matchProfiles.txt'

with open(fileName, "rb") as input_file:
    userProfiles = pickle.load(input_file)


for user in userProfiles:

    imageList = user[3]

    for image in imageList:

        url = image[0]
        urlParts = url.split("/")
        iName = urlParts[-1]

        res = requests.get(url, stream = True)

        if res.status_code == 200:
            with open(iName,'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',iName)
        else:
            print('Image Couldn\'t be retrieved')


