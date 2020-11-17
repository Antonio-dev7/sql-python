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
# course ---> INSERT IN NEW TABLE YOU CREATED BEFORE

try:
    # run query
    with connection.cursor() as cursor:
        row = ("Bob", 21, "1990-02-06 23:04:56") # 3 tuple -> %s <- remember this.
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
        # Note that the above will still display a warning (not error) if the table already exists
finally:
        connection.close()


