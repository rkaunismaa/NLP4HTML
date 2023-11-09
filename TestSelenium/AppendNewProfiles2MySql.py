# conda activate nlp4html

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
profileFile = 'matchLists/masterProfiles_20230802.txt'
profileFile = 'matchLists/matchProfiles_2023-08-23--07-40.txt'
profileFile = 'matchLists/MatchProfilesMasterList.txt'
profileFile = 'matchLists/NewProfiles_2023-08-30--10-25.txt'
profileFile = 'matchLists/NewProfiles_2023-09-03--12-21.txt'
profileFile = 'matchLists/NewProfiles_2023-09-06--16-14.txt'
profileFile = 'matchLists/NewProfiles_2023-09-13--09-49.txt'
profileFile = 'matchLists/NewProfiles_2023-09-18--10-20.txt'
profileFile = 'matchLists/NewProfiles_2023-09-25--16-27.txt'

profileFile = 'matchLists/UpdatedNewProfiles_2023-10-06--07-12.txt'

profileFile = 'matchLists/UpdatedNewProfiles_2023-10-15--11-39.txt'

profileFile = 'matchLists/UpdatedNewProfiles_2023-10-22--06-53.txt'

profileFile = 'matchLists/UpdatedNewProfiles_2023-11-02--05-56.txt'

profileFile = 'matchLists/UpdatedNewProfiles_2023-11-09--10-18.txt'

with open(profileFile, "rb") as input_file:
    profiles = pickle.load(input_file)

scanDateTime = datetime.strptime('2023-08-02 08:01:01', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-08-23 07:40:00', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-08-25 08:13:00', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-08-30 10:25:00', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-09-03 12:21:00', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-09-06 16:14:00', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-09-13 09:49:00', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-09-18 10:20:00', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-09-25 16:27:00', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-10-06 07:12:00', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-10-15 11:39:00', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-10-22 06:35:00', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-11-02 05:56:00', '%Y-%m-%d %H:%M:%S')
scanDateTime = datetime.strptime('2023-11-09 10:18:00', '%Y-%m-%d %H:%M:%S')

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
            valueS = tuple([userInsertId, image[0], image[1]])
            with conn.cursor() as cursor:
                insertQuery = f'INSERT INTO Images (idUsers, Url, Message) VALUES (%s, %s, %s)'
                cursor.execute(insertQuery, valueS)

conn.commit()
conn.close()

print('MySql Success!')