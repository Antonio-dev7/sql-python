import os
import pymysql

# Get username from cloud9 or github 
# (modify this variable if runnin on another environment)
username = os.getenv('C9_USER')

# connect to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
# course ---> CREATE TABLE

try:
    # run query
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                       Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the table already exists
finally:
        connection.close()


