import pickle


fileName = 'matchLists/FailedURLNotFoundProfiles_2024-03-09--10-44.txt'

# fileName = 'matchLists/ValidatedProfiles_2024-03-09--10-44.txt'
with open(fileName, "rb") as input_file:
    profiles = pickle.load(input_file)

print(len(profiles))

for profile in profiles:

    if (profile[1] != 'Profile Not Available'):

        matchURL = profile[0]
        
    

    