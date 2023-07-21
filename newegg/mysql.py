import mysql.connector

# Replace these with your actual database credentials
db_host = "172.17.0.3"
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
