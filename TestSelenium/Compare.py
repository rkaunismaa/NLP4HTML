import pickle
import requests
import shutil
import os

matchUsers = 'matchLists/matchUserList.txt'
matchProfiles = 'matchLists/matchProfiles.txt' 

with open(matchUsers, "rb") as input_file:
    users = pickle.load(input_file)

with open(matchProfiles, "rb") as input_file:
    profiles = pickle.load(input_file)

# There will be users that did not scan properly, 
# and so there will be no profile. 
# Identify those missed users, and place them into a new file

missedUsers = []
for user in users:

    userName = user[0]
    userUrl = user[1]

    found = False
    for profile in profiles:
        profileUrl = profile[0]
        if profileUrl == userUrl:
            found = True
        if found:
            break

    if (not found):
        missedUsers.append( (userName, userUrl) )

fileName = 'matchLists/missedUsers.txt'
with open(fileName, "wb") as fp:   
    pickle.dump(missedUsers, fp)







    



    


    