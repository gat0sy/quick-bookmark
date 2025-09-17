import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bookmark_db"
)

cursor = conn.cursor()