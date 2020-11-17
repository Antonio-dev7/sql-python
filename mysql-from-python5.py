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
# course ---> INSERT MANY ROWS .

try:
    # run query
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1990-02-06 23:04:56"),  # 3 tuple !%s! remember this. / rows changed
                ("Jim", 56, "1995-05-09 13:12:45"),
                ("Fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows) # executemany and rows change!
        connection.commit()
        
finally:
        # Note that the above will still display a warning (not error) if the table already exists
        connection.close()


