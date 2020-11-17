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

# course ---> Delete Where In |  
# --> If we write a where clause that matches multiple records, then we can delete them all at once.
# --> The first thing we need to do is work out how to turn a list of names into an SQL statement.

try:
    # run query
    with connection.cursor() as cursor:
        names = ['jim','bob']
        cursor.execute("DELETE FROM Friends WHERE name in (%s,%s)", names) 
        connection.commit()
        
finally:
        # Note that the above will still display a warning (not error) if the table already exists
        connection.close()


