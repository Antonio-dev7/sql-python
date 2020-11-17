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

# course ---> DELETE many |  

try:
    # run query
    with connection.cursor() as cursor:
        rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", 
                                ['bob', 'jim'])  # execute- many After ", --> ['bob', 'jim'])
        connection.commit()
        
finally:
        # Note that the above will still display a warning (not error) if the table already exists
        connection.close()


