import pickle

# What we are reading from  ...
runDateEnding = '_2023-08-21--08-54.txt'
runDateEnding = '_2023-08-23--07-40.txt'
runDateEnding = '_2023-08-25--08-13.txt'

matchProfiles = 'matchLists/matchProfiles' + runDateEnding
missedProfilesFn = 'matchLists/missedProfiles' + runDateEnding
# What we are writing to ...
masterProfilesFn = 'matchLists/masterProfiles' + runDateEnding

# The final thing ...
matchProfiles = 'matchLists/MatchProfiles.txt' 
missedProfilesFn = 'matchLists/missedProfiles2023-08-26--09-48.txt'
# What we are writing to ...
masterProfilesFn = 'matchLists/MatchProfilesMasterList.txt' 

# The final thing ...
matchProfiles = 'matchLists/MatchProfilesMasterList.txt' 
missedProfilesFn = 'matchLists/NewProfiles_2023-08-30--10-25.txt'
# What we are writing to ...
masterProfilesFn = 'matchLists/MatchProfilesMasterList_2023-08-30--10-25.txt' 

# Read from these 2 files ...
matchProfiles = 'matchLists/MatchProfilesMasterList_2023-08-30--10-25.txt' 
missedProfilesFn = 'matchLists/NewProfiles_2023-09-03--12-21.txt'
# ... and write to this file ...
masterProfilesFn = 'matchLists/MatchProfilesMasterList_2023-09-03--12-21.txt' 


# Read from these 2 files ...
matchProfiles = 'matchLists/MatchProfilesMasterList_2023-09-03--12-21.txt' 
missedProfilesFn = 'matchLists/NewProfiles_2023-09-06--16-14.txt'
# ... and write to this file ...
masterProfilesFn = 'matchLists/MatchProfilesMasterList_2023-09-06--16-14.txt' 

# Read from these 2 files ...
matchProfiles = 'matchLists/MatchProfilesMasterList_2023-09-06--16-14.txt' 
missedProfilesFn = 'matchLists/NewProfiles_2023-09-13--09-49.txt'
# ... and write to this file ...
masterProfilesFn = 'matchLists/MatchProfilesMasterList_2023-09-13--09-49.txt' 


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



