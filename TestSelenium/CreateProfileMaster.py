import pickle

# What we start with ...
matchProfiles = 'matchLists/matchProfiles_20230802.txt' 
missedProfilesFn = 'matchLists/missedProfiles_20230802.txt'

masterProfilesFn = 'matchLists/masterProfiles_20230802.txt'

with open(matchProfiles, "rb") as input_file:
    profiles = pickle.load(input_file)

with open(missedProfilesFn, "rb") as input_file:
    missedProfiles = pickle.load(input_file)

masterProfile = []

# I am sure there is a way more efficient way of doing this, but .. meh .. 

for profile in profiles:
    masterProfile.append(profile)

for profile in missedProfiles:
    masterProfile.append(profile)

with open(masterProfilesFn, "wb") as fp:   
    pickle.dump(masterProfile, fp)



