# 登陆和注册 Login.py

import sqlite3
import os

# 建表
'''sql_creatAllTable="""CREATE TABLE user(
                ID VARCHAR(30) PRIMARY KEY NOT NULL,
                PWD VARCHAR(30) NOT NULL,
                filename VARCHAR(100) NOT NULL
                );"""
cur.execute(sql_creatAllTable)'''


# 登陆
#ID，pwd:用户名和密码
# return 0:登陆成功,返回登陆者的ID
# return 1:登陆失败，输入账号或密码为空
# return 2:登陆失败，账号密码不存在
def Login(ID, pwd):
    con = sqlite3.connect('lib.db')
    cur = con.cursor()
    if ID == '' or pwd == '':
        cur.close()
        con.commit()
        con.close()
        return 1,''
    l = cur.execute("SELECT count(*) as cou FROM user WHERE ID=? and PWD=?", (ID, pwd))
    row = l.fetchone()
    if row[0] == 0:
        cur.close()
        con.commit()
        con.close()
        return 2,''
    else:
        cur.close()
        con.commit()
        con.close()
        return 0,ID


# 注册
#ID，pwd:用户名和密码
# return 0:注册成功
# return 1:注册失败，输入账号或密码为空
# return 2:注册失败，账号已存在
def register(ID, pwd):
    con = sqlite3.connect('lib.db')
    cur = con.cursor()
    if ID == '' or pwd == '':
        cur.close()
        con.commit()
        con.close()
        return 1
    l = cur.execute("SELECT count(*) as cou FROM user WHERE ID=? and PWD=?", (ID, pwd))
    row = l.fetchone()
    if row[0] > 0:
        cur.close()
        con.commit()
        con.close()
        return 2
    else:
        #每位新用户创建一个表记录其信息 地址为./useRecord/(ID)/record.db
        filename = "./useRecord/" + ID
        os.makedirs(filename)
        c = sqlite3.connect(filename+'/record.db')
        cu = c.cursor()
        table = """CREATE TABLE user(
                        FROML VARCHAR(30) NOT NULL,
                        TOL VARCHAR(30) NOT NULL,
                        SEARCH VARCHAR(2000) NOT NULL,
                        RESULT VARCHAR(2000) NOT NULL,
                        TIME VARCHAR(100) NOT NULL
                        );"""
        cu.execute(table)
        name=filename+'/record.db'
        cur.execute("insert into user values(?,?,?)", (ID, pwd, name))
        cur.close()
        con.commit()
        con.close()
        return 0


# = register('11', '22')
#print(k)
