# conda activate nlp4html

# sudo systemctl start mysql
# systemctl status mysql


import mysql.connector
from datetime import datetime
import pickle

from MatchFunctions import *

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

purgeTables = True
if purgeTables:
    
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


profileFile = get_newest_file_creation_date('matchLists', 'CurrentProfiles_')

# extract from the string profileFile everything following 'matchLists/CurrentProfiles_'
# and before the '.txt'
scanDate = profileFile.replace('matchLists/CurrentProfiles_', '')
scanDate = scanDate.replace('.txt', '')
scanDate += '-00'

scanDateTime = datetime.strptime(scanDate, '%Y-%m-%d--%H-%M-%S')

with open(profileFile, "rb") as input_file:
    profiles = pickle.load(input_file)


for profile in profiles:

    isSubscriber = (profile[3] == 'Subscriber')
    url = profile[0]
    matchUserId = url.split("/")[-1]
    # test existing record ...
    # matchUserId = 'wxzetG5wchZXxt7qDn6HPQ2'

    # only insert the record if it's not in the db!
    uidExists = False
    with conn.cursor() as cursor:
        selectQuery = f"SELECT * FROM Users WHERE MatchUserid = %s"
        selectId = (matchUserId,)
        cursor.execute(selectQuery, selectId)
        selectResult = cursor.fetchone()
        uidExists = (selectResult is not None)

    if (not uidExists):
        values = [ matchUserId, url, profile[1], profile[2], isSubscriber, profile[4], profile[5], profile[6], profile[7], scanDateTime ]
        valueS = tuple(values) 
        with conn.cursor() as cursor:
            insertQuery = f'INSERT INTO Users (MatchUserId, Url, FirstName, AgeLocation, Subscriber, LastOnline, MiniEssayTitle, MiniEssayContent, Summary, ScanDateTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(insertQuery, valueS)
            userInsertId = cursor.lastrowid

        images = profile[8]
        for image in images:
            valueS = tuple([userInsertId, image[0], image[1], image[2]])
            with conn.cursor() as cursor:
                insertQuery = f'INSERT INTO Images (idUsers, Url, Message, userImageNo) VALUES (%s, %s, %s, %s)'
                cursor.execute(insertQuery, valueS)

conn.commit()
conn.close()

print('MySql Success!')