import socket
import format as f
import time
import transOP
import func_timeout
from func_timeout import func_set_timeout, FunctionTimedOut

import Login as login
import API as ap

@func_set_timeout(20)
def receive(conn):
    return conn.recv(1024)
#modify
# 创建服务器端套接字
sk = socket.socket()
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
# host = 服务器内网ip
port = 80
# 端口

sk.bind((host, port))
# 监听链接
sk.listen(5)
#conn, addr = sk.accept()
while True:
    try:
        # 接收客户端信息
        conn, addr = sk.accept()
        while True:
            try:
                ret = conn.recv(1024)
                qur = ret.decode('utf-8')
                time.sleep(1)
                k = qur.split(":")
                # 登陆
                if k[0] == "登陆":
                    print("这是登陆")
                    flag, user = login.Login(k[1], k[2])
                    userID = user
                    s = str(flag)
                    conn.send(bytes(s, encoding='utf-8'))
                # 注册
                elif k[0] == "注册":
                    print("这是注册")
                    flag = login.register(k[1], k[2])
                    s = str(flag)
                    conn.send(bytes(s, encoding='utf-8'))
                # 翻译
                elif k[0] == "翻译":
                    print("这是翻译")
                    From_lan, To_lan, Origin, result = ap.trans(k[3], f.getCode(k[1]),f.getCode(k[2]))
                    s = transOP.addHistoryRecord(userID, f.getDictKey_2(To_lan), f.getDictKey_2(From_lan), Origin, result)
                    st = "原语言:" + f.getDictKey_2(From_lan) + "+目标语言:" + f.getDictKey_2(To_lan) + "+翻译原文:" + Origin + "+翻译结果:" + result
                    print(st)
                    conn.send(bytes(st, encoding='utf-8'))
                # 查询历史
                elif k[0] == "查记录":
                    st = "这是查询历史记录"
                    print("这是查询历史记录")
                    l = transOP.getHistoryRecord(userID)
                    print(l)
                    conn.send(bytes(str(l), encoding='utf-8'))
                else:
                    break
            except ConnectionResetError:
                print("客户端 %s:%s异常断开连接" % addr)
                break
            except UnicodeDecodeError:
                print("对方断开连接");
                break
            except KeyboardInterrupt:
                print("服务器关闭")
                break
    except func_timeout.dafunc.FunctionTimedOut:
        print("连接超时")
conn.close()

