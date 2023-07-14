import sqlite3


# 浏览历史记录
# 返回元组
def getHistoryRecord(ID):
    filename = './useRecord/' + ID + '/record.db'
    con = sqlite3.connect(filename)
    cur = con.cursor()
    l = cur.execute("SELECT * FROM user")
    rows = l.fetchall()
    cur.close()
    con.commit()
    con.close()
    return rows

# 添加浏览记录
# 参数有误，
def addHistoryRecord(ID, ToL, FromL, origin, result):
    filename = './useRecord/' + ID + '/record.db'
    con = sqlite3.connect(filename)
    cur = con.cursor()
    cur.execute("INSERT INTO user values(?,?,?,?,date('now'))", (FromL, ToL, origin, result))
    cur.close()
    con.commit()
    con.close()
    return 0
