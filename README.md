# python-mysqldb-reconnect
A minimal MySQL database management with auto-reconnection after session timeout

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

