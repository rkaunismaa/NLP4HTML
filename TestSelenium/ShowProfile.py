import pickle


fileName = 'matchLists/FailedURLNotFoundProfiles_2024-02-27--16-51.txt'
with open(fileName, "rb") as input_file:
    profiles = pickle.load(input_file)

for profile in profiles:

    print(profile)

    break