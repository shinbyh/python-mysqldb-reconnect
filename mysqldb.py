# -*- coding: utf-8 -*-
import pymysql

class DB:
    conn = None
    cursor = None
    ip = None # MySQL connection IP
    port = None # MySQL connection port (e.g. 3306)
    user = None # MySQL user account (e.g. root)
    pw = None # MySQL user password
    db_name = None # Database name in MySQL
    charset = None # Character encoding (default: utf8)

    def __init__(self, ip, port, user, pw, db_name, charset=None):
        self.ip = ip
        self.port = port
        self.user = user
        self.pw = pw
        self.db_name = db_name
        if charset is None:
            self.charset = 'utf8'

    def connect(self):
        self.conn = pymysql.connect(host=self.ip, port=self.port, user=self.user, password=self.pw, db=self.db_name, charset=self.charset)
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def query(self, sql, sql_tuple=None):
        try:
            if sql_tuple is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, sql_tuple)
        except (AttributeError, pymysql.err.OperationalError):
            self.connect()
            if sql_tuple is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, sql_tuple)
        return self.cursor

    #
    def get_connection():
        return self.conn

#
# Test code
# Just for testing queries with the user table in the MySQl DB.
#
if __name__ == '__main__':
    db = DB(ip='127.0.0.1', port=3306, user='root', pw='YOUR_ROOT_PASSWORD', db_name='mysql')

    # Test with a SQL query
    sql = 'SELECT Host,User FROM user'
    cursor = db.query(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Test with a SQL query and a tuple
    sql_with_tuple = ('SELECT Host,User FROM user WHERE Host=%s')
    cursor = db.query(sql_with_tuple, ('localhost'))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
