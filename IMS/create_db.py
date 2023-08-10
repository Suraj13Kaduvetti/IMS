import sqlite3

def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(date text,supid INTEGER PRIMARY KEY AUTOINCREMENT,company text,name text,contact text,Category text,desc text)")
    con.commit()

    # cur.execute("CREATE TABLE IF NOT EXISTS sup_apmc(date text,invoice INTEGER PRIMARY KEY AUTOINCREMENT,company text,name text,contact text,gala text,desc text)")
    # con.commit()

    # cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY,m_name text,s_name text)")
    # con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY,m_name text)")
    con.commit()

    # cur.execute("CREATE TABLE IF NOT EXISTS cat_apmc(cid INTEGER PRIMARY KEY,name text)")
    # con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS products(date text,pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,name text,price text,mrp text,qty text,status text)")
    con.commit()

create_db()
