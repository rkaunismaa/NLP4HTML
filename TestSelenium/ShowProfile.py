import pickle

with open('matchLists/masterProfiles_20230801.txt', "rb") as input_file:
    profiles = pickle.load(input_file)

for profile in profiles:

    print(profile)

    break