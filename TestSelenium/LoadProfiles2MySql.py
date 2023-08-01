import mysql.connector
from datetime import datetime
import pickle

# The ip of the server may change ... find out what it is by running ...
# docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql20230720

# Replace these with your actual database credentials
db_host = "127.0.0.1"
db_user = "root"
db_password = "12345"

db_name = "MatchDb"
table_name = "Users"

# Establish a connection
conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

purgeTable = True
if purgeTable:
    
    with conn.cursor() as cursor:
        
        query = f'DELETE FROM Users'
        cursor.execute(query)
        query = f'ALTER TABLE Users AUTO_INCREMENT=1'
        cursor.execute(query)

        query = f'DELETE FROM Images'
        cursor.execute(query)
        query = f'ALTER TABLE Images AUTO_INCREMENT=1'
        cursor.execute(query)

    conn.commit()

profileFile = 'matchLists/masterProfiles_20230801.txt'
with open(profileFile, "rb") as input_file:
    profiles = pickle.load(input_file)

scanDateTime = datetime.strptime('2023-08-01 08:01:01', '%Y-%m-%d %H:%M:%S')
for profile in profiles:

    isSubscriber = (profile[3] == 'Subscriber')
    values = [ scanDateTime, profile[0], profile[1], profile[2], isSubscriber, profile[4], profile[5], profile[6], profile[7] ]
    valueS = tuple(values) 
    with conn.cursor() as cursor:
        insertQuery = f'INSERT INTO Users (ScanDateTime, Url, FirstName, AgeLocation, Subscriber, LastOnline, MiniEssayTitle, MiniEssayContent, Summary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(insertQuery, valueS)

conn.commit()
conn.close()
