
import sqlite3 
from sqlite3.dbapi2 import Error
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def search_location(city):
    
    database = r"szy.db"
    conn = create_connection(database)
    cursor = conn.cursor()
    sql='select location from location where city=?'
    cursor.execute(sql,(city,))
    location=cursor.fetchone()
    conn.commit()
    conn.close()
    return location

def search_order(number):
    
    database = r"szy.db"
    conn = create_connection(database)
    cursor = conn.cursor()
    
    sql='select time_of_receipt from order1 where order_number=?'
    cursor.execute(sql,(number,))
    time=cursor.fetchone()
    
    time1=time[0]
    conn.commit()
    conn.close()
    return time1
