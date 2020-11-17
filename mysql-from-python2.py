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
# course ---> CURSOR
try:
# Run a query(get results as dictionaries pass /pymysql.cursors.DictCursor/)
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
        # Close the connetion, regarless of wether the above was 
        # successful or not !
        connection.close()


# (get results as dictionaries pass /pymysql.cursors.DictCursor/)
# The advantage of using the DictCursor is that the rows now include the column names.
# This format also lends itself to being converted into JSON.