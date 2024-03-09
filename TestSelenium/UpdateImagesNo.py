
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

# Create a cursor object to interact with the database
cursor = conn.cursor()

try:

    cursor.execute("SELECT * FROM Images")
    allImages = cursor.fetchall()

    idUser = 0
    imageNo = 0

    for image in allImages:

        idImage = image[0]
        idCurrentUser = image[1]

        # New user?
        if (idCurrentUser!= idUser):
            idUser = idCurrentUser
            imageNo = 1

        # Update the userImageNo field.
        updateQuery = f"UPDATE Images SET userImageNo = %s WHERE idImages = %s"
        updateValues = (imageNo, idImage)
        cursor.execute(updateQuery, updateValues)

        imageNo += 1

    # Commit the changes to the database
    conn.commit()
    print("UserImageNo updated successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()


