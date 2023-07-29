import pickle

# Save the userProfiles to a local file
fileName = 'matchProfiles.txt'

with open(fileName, "rb") as input_file:
    userProfiles = pickle.load(input_file)

print(userProfiles)