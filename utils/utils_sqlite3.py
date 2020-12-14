import sqlite3 
import hashlib
import os
import logging # Logging: https://docs.python.org/3/howto/logging.html

# Setuo logging to file
#logging.basicConfig(filename=os.path.join("logs","db.log"),level=logging.INFO)
logging.basicConfig(level=logging.INFO)


def connect_db(database):
    res = False
    conn = None
    try:
        conn = sqlite3.connect(database)
        res = True
    except Exception as  e:
        logging.warning("Connection Error: %s",e)
    return res, conn

def create_users_table(conn):
    res = False
    try:
        c = conn.cursor()
        sql_query = ''' CREATE TABLE IF NOT EXISTS dataTable (
                        date text NOT NULL,
                        url  text NOT NULL,
                        PRIMARY KEY(date)
                    ); '''
        c.execute(sql_query)
        conn.commit()
        logging.info("Table [dataTable] Created")
        res = True
    except Exception as e:
        logging.info("Unable to Create [users_table]  Table: %s",e)
    return res
    
def add_userdata(username,password,conn):
    res = False
    if username=="" or password=="":
        logging.info("Empty Username or password")
        return res
    try:
        c = conn.cursor()
        password = make_hashes(password)
        sql_query = '''INSERT INTO users_table(username,password) VALUES(?,?)'''
        c.execute(sql_query,(username,password))
        conn.commit()
        logging.info("Added userdata  username=%s, password=%s", username, password)
        res = True
    except Exception as e:
        logging.info("Unable to insert userdata: %s", e)
    return res

def get_password(username,conn):
    res = False
    data = None
    try:
        c = conn.cursor()
        c.execute('SELECT password FROM users_table WHERE username=?', (username,))
        data = c.fetchall()[0][0]
        logging.info("Get userdata password completed %s" , data)
        res = True
    except Exception as e:
        logging.info("Unable to get password userdata: %s",e)
    return res, data

def view_all_users(conn):
    res = False
    data = None
    try:
        c = conn.cursor()
        c.execute('SELECT * FROM users_table')
        data = c.fetchall()
        logging.info("Get all login user completed %s" % data)
        res = True
    except Exception as e:
        logging.info("Unable to get login userdata: %s",e)
    return res, data

def delete_users_data():
    res = False
    try:
        sql = 'DELETE FROM users_table'
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        res = True
    except Exception as e:
        logging.info("Unable to gdelete users data: %s",e)
    return res

def delete_users_table():
    res = False
    try:
        sql = 'DROP TABLE users_table'
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        res = True
    except Exception as e:
        logging.info("Unable to gdelete users data: %s",e)
    return res

def login(username, password):
    result = False
    res, conn = connect_db("database.db") 
    if res:
        res,hashed_pswd = get_password(username,conn)
        if res: 
            result = check_hashes(password, hashed_pswd)        
    return result

def register(username, password):
    result = False
    res, conn = connect_db("database.db") 
    if res:
        result = add_userdata(username=username, password=password,conn=conn)
    return result


if __name__ == "__main__":
    # Create Db and Table
    res, conn = connect_db("database.db") 
    #res = delete_users_data() if res  else exit()
    res = delete_users_table() if res  else exit()
    res = create_users_table(conn) if res  else exit()
    for username,password in zip(USERNAMES,PASSWORDS):
        res = add_userdata(username=username, password=password,conn=conn) if res  else exit()
    res = view_all_users(conn) if res  else exit()
