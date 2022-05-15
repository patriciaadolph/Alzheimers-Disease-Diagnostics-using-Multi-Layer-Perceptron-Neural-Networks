import mysql.connector
def select(q):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='alzheimers_diagnostics')
    cur = cnx.cursor(dictionary=True)
    cur.execute(q)
    return cur.fetchall()

def insert(q):
    cnx=mysql.connector.connect(user='root',password='',host='localhost',database='alzheimers_diagnostics')
    cur=cnx.cursor(dictionary=True)
    cur.execute(q)
    cnx.commit()
    return cur.lastrowid

def update(q):
    cnx=mysql.connector.connect(user='root',password='',host='localhost',database='alzheimers_diagnostics')
    cur=cnx.cursor(dictionary=True)
    cur.execute(q)
    cnx.commit()
    return cur.rowcount

def delete(q):
    cnx=mysql.connector.connect(user='root',password='',host='localhost',database='alzheimers_diagnostics')
    cur=cnx.cursor(dictionary=True)
    cur.execute(q)
    cnx.commit()
    return cur.rowcount