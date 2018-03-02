# python-mysqldb-reconnect
A minimal MySQL database management with auto-reconnection after session timeout.

Because MySQL shuts down a connection after a certain timeout, a long-running Python code with a mysql connection must be renewed. I create a wrapper class for pymysql which automatically re-connects to the mysql database when an exception occurs due to timeout (e.g. an error message with "MySQL has gone away").

## Prerequisites
* Python 2.X or 3.X
* pymysql
* MySQL or a server running MySQL

## Usage
Running the test code
```
$ python mysqldb.py
```

Sample code
```
import mysqldb

db = DB(ip='MYSQL_SERVER_IP', port=PORT_NUMBER, user='DB_USER', pw='DB_USER_PASSWORD', db_name='DATABASE_NAME')

sql = 'SELECT * FROM YOUR_TABLE_NAME_FOR_QUERY'
cursor = db.query(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)
```

