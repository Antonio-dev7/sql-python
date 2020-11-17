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

# course ---> Update Many | rows 

try:
    # run query
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'), # rows added and row-s S at the end or row
                (24, 'Jim'),
                (25, 'Fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", # changed to - execute-many
                        rows)  # this is how you update many rows) at the end
        connection.commit()
        
finally:
        # Note that the above will still display a warning (not error) if the table already exists
        connection.close()


