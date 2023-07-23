# from mysql.connector import *
import mysql.connector

# Replace these with your actual database credentials
db_host = "172.17.0.2"
db_user = "root"
db_password = "12345"
db_name = "NewEggCa"

# Establish a connection
conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

import json

dir = 'newegg/'
ext = '.jsonl'
source = 'newegg' 
target = dir + source + '_sorted' + ext

# Step 1: Read the JSONL file into a list
with open(dir + source + ext, 'r') as file:
    lines = file.readlines()

# Step 2: Parse each line as JSON and sort the list based on the "name" key
data_list = [json.loads(line) for line in lines]



conn.close()
