import json

dir = 'newegg/'
ext = '.jsonl'
source = 'newegg' 
target = dir + source + '_sorted' + ext

# Step 1: Read the JSONL file into a list
with open(dir + source + ext, 'r') as file:
    lines = file.readlines()

# Step 2: Parse each line as JSON and sort the list based on the "sourceUrl" and "tagmedal" keys
data_list = [json.loads(line) for line in lines]
sorted_data_list = sorted(data_list, key=lambda x: (x['sourceUrl'], x['tagmedal']))

maxBullets = 0
for key, value in data_list.items():
    if key == "bullets":
        lenBullets = len(value)
        if lenBullets > maxBullets:
            maxBullets = lenBullets

# Step 3: Write the sorted list back to the JSONL file
with open(target, 'w') as file:
    for item in sorted_data_list:
        file.write(json.dumps(item) + '\n')
