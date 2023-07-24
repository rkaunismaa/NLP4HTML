# from mysql.connector import *
import mysql.connector

# Replace these with your actual database credentials
db_host = "172.17.0.2"
db_user = "root"
db_password = "12345"
db_name = "NewEggCa"
table_name = "Products"

# Establish a connection
conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

import json
import ast

dir = 'newegg/'
ext = '.jsonl'
source = 'newegg' 

sourceFile = dir + source + ext

# # Step 1: Read the JSONL file into a list
# with open(sourceFile, 'r') as file:
#     lines = file.readlines()

# # Step 2: Parse each line as JSON and sort the list based on the "name" key
# data_list = [json.loads(line) for line in lines]

# line0 = ast.literal_eval(lines[0])

# for key, value in line0.items():
#     print(key, value)

# Open the file and read JSON objects line by line
with open(sourceFile, "r") as file:
    for line in file:

        # Parse the JSON object in each line
        product = json.loads(line)

        with conn.cursor() as cursor:
            for key, value in product.items():
                if key in ['sourceUrl', 'tagmedal', 'title', 'url', 'imgsrc', 'price', 'wasprice', 'savings']:
                    insertQuery = f'INSERT INTO {table_name} ({key}) VALUES (%s)'
                    shortValue = value[0:10]
                    cursor.execute(insertQuery,(shortValue,))

conn.close()
