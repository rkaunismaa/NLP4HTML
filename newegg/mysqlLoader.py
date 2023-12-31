# from mysql.connector import *
import mysql.connector

# The ip of the server may change ... find out what it is by running ...
# docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql20230720

# Replace these with your actual database credentials
db_host = "172.17.0.3"
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
source = 'newegg_sorted' 

sourceFile = dir + source + ext

purgeTable = True
if purgeTable:

    with conn.cursor() as cursor:
        query = f'DELETE FROM {table_name}'
        cursor.execute(query)
        query = f'ALTER TABLE {table_name} AUTO_INCREMENT=1'
        cursor.execute(query)
    conn.commit()

# Open the file and read JSON objects line by line
with open(sourceFile, "r") as file:
    for line in file:

        # Parse the JSON object in each line
        product = json.loads(line)

        keys = []
        values = []
        for key, value in product.items():
            if key in ['dateTime', 'sourceUrl', 'tagmedal', 'title', 'url', 'imgsrc', 'price', 'wasprice', 'savings', 'bullets']:
                keys.append(key)
                if key == 'bullets':
                    value = ",".join(value)
                values.append(value)

        keyS = ",".join(keys)
        valueS = tuple(values) 
        with conn.cursor() as cursor:
            insertQuery = f'INSERT INTO {table_name} ({keyS}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(insertQuery, valueS)

conn.commit()
conn.close()
