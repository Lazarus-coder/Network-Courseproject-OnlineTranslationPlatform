#-*- coding:utf-8 -*-
import socket
import sys
import tkinter
from tkinter import *
from tkinter import messagebox, END
from tkinter import ttk
from func_timeout import func_set_timeout


import time
import func_timeout
# 创建客户端套接字
@func_set_timeout(10)
def receive(conn):
    return conn.recv(1024)


# 检查是否有网络连接
def isConnected():
    import requests
    try:
        html = requests.get("https://www.aliyun.com/", timeout=2)
    except:
        return False
    return True

def start():
    try:
        sk = socket.socket()
        # 尝试连接服务器
        sk.connect(('8.137.97.130', 80))
        while True:
            # 信息发送
            loginPanel(sk)

        # 关闭客户端套接字
    except func_timeout.dafunc.FunctionTimedOut:
        print("连接超时")

def loginPanel(socket):
    root = tkinter.Tk()
    root.title('计网翻译项目')
    # 定义窗口大小
    root['height'] = 300
    root['width'] = 400

    # 在窗口上创建标签组件
    labelName = tkinter.Label(root, text='用户名:', justify=tkinter.RIGHT, anchor='e', width=80)
    labelName.place(x=50, y=50, width=80, height=30)

    # 创建字符串变量和文本框组件，同时设置关联的变量
    varName = tkinter.StringVar(root, value='')
    entryName = tkinter.Entry(root, width=80, textvariable=varName)
    entryName.place(x=175, y=50, width=150, height=30)

    # 在窗口上创建标签组件
    labelPwd = tkinter.Label(root, text='密码:', justify=tkinter.RIGHT, anchor='e', width=80)
    labelPwd.place(x=50, y=100, width=80, height=30)

    # 创建密码文本框
    varPwd = tkinter.StringVar(root, value='')
    entryPwd = tkinter.Entry(root, width=80, textvariable=varPwd)
    entryPwd.place(x=175, y=100, width=150, height=30)



    # 登录按钮事件处理函数
    def login():

        print("1")
        name = entryName.get()
        pwd = entryPwd.get()
        message = "登陆:" + name + ":" + pwd
        socket.send(bytes(message, encoding='utf-8'))
        ret = socket.recv(1024)
        jud=ret.decode('utf-8')
        if jud=='0':
            messagebox.showinfo(title='恭喜！', message='登录成功！')
            root.destroy()
            FuncPanel(socket)
        elif jud=='1':
            messagebox.showinfo(title='失败！', message='未输入账号密码！')
        else:
            messagebox.showinfo(title='失败！', message='账号密码不存在！')
    # 创建按钮组件，同时设置按钮事件处理函数
    buttonOk = tkinter.Button(root, text='登录', command=login)
    buttonOk.place(x=150, y=160, width=50, height=20)

    # 取消按钮的事件处理函数
    def cancle():
        root.destroy()
        RegisterPanel(socket)

    def JieShu():
        sys.exit(0)
        # 销毁root窗口
        root.destroy()

    # 创建按钮组件，同时设置按钮事件处理函数
    buttonCancle = tkinter.Button(root, text='注册', command=cancle)
    buttonCancle.place(x=250, y=160, width=50, height=20)
    root.protocol("WM_DELETE_WINDOW", JieShu)
    root.mainloop()

def RegisterPanel(socket):
    root = tkinter.Tk()
    root.title('计网翻译项目')
    # 定义窗口大小
    root['height'] = 300
    root['width'] = 400

    # 在窗口上创建标签组件
    labelName = tkinter.Label(root, text='用户名:', justify=tkinter.RIGHT, anchor='e', width=80)
    labelName.place(x=50, y=50, width=80, height=30)

    # 创建字符串变量和文本框组件，同时设置关联的变量
    varName = tkinter.StringVar(root, value='')
    entryName = tkinter.Entry(root, width=80, textvariable=varName)
    entryName.place(x=175, y=50, width=150, height=30)

    # 在窗口上创建标签组件
    labelPwd = tkinter.Label(root, text='密码:', justify=tkinter.RIGHT, anchor='e', width=80)
    labelPwd.place(x=50, y=100, width=80, height=30)

    # 创建密码文本框
    varPwd = tkinter.StringVar(root, value='')
    entryPwd = tkinter.Entry(root, width=80, textvariable=varPwd)
    entryPwd.place(x=175, y=100, width=150, height=30)


    # 登录按钮事件处理函数
    def regist():

        print("1")
        name = entryName.get()
        pwd = entryPwd.get()
        message = "注册:" + name + ":" + pwd
        socket.send(bytes(message, encoding='utf-8'))
        ret = socket.recv(1024)
        jud=ret.decode('utf-8')
        if jud=='0':
            messagebox.showinfo(title='恭喜！', message='注册成功！')
        elif jud=='1':
            messagebox.showinfo(title='失败！', message='未输入账号密码！')
        else:
            messagebox.showinfo(title='失败！', message='账号密码不存在')
        loginPanel(socket)

    def JieShu():
        sys.exit(0)
        # 销毁root窗口
        root.destroy()

    def retu():
        root.destroy()
        loginPanel(socket)

    # 创建按钮组件，同时设置按钮事件处理函数
    buttonCancle = tkinter.Button(root, text='注册', command=regist)
    buttonCancle.place(x=150, y=160, width=50, height=20)
    buttonr = tkinter.Button(root, text='返回', command=retu)
    buttonr.place(x=250, y=160, width=50, height=20)

    root.protocol("WM_DELETE_WINDOW", JieShu)
    root.mainloop()

def FuncPanel(socket):
    win = Tk()
    win.title('翻译')
    # 设置窗口大小
    width = 500
    heigh = 500
    screenwidth = win.winfo_screenwidth()
    screenheight = win.winfo_screenheight()
    win.geometry('%dx%d+%d+%d' % (width, heigh, (screenwidth - width) / 2, (screenheight - heigh) / 2))
    win.resizable(True, True)

    '''# 第一个语言输入框
    inp1 = Entry(root)
    inp1.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)

    # 第二个语言输入框
    inp2 = Entry(root)
    inp2.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.1)'''
    ddb_default1 = ttk.Combobox(win)
    ddb_default1['value'] = (
    '自动检测', '阿拉伯语', '阿尔巴尼亚语', '阿拉贡语', '艾马拉语', '奥塞梯语', '奥里亚语', '波兰语', '巴什基尔语',
    '白俄罗斯语', '保加利亚语', '本巴语', '俾路支语', '博杰普尔语', '楚瓦什语', '丹麦语', '掸语', '低地德语', '俄语',
    '法语', '梵语', '法罗语', '盖尔语', '高棉语', '古吉拉特语', '瓜拉尼语', '韩语', '哈卡钦语', '豪萨语', '吉尔吉斯语',
    '加泰罗尼亚语', '卡拜尔语', '卡舒比语', '科西嘉语', '克林贡语', '克什米尔语', '拉丁语', '拉特加莱语', '林加拉语',
    '卢森尼亚语', '罗曼什语', '马来语', '马拉加斯语', '马绍尔语', '毛里求斯克里奥尔语', '马耳他语', '挪威语',
    '南非荷兰语', '葡萄牙语', '普什图语', '齐切瓦语', '日语', '萨丁尼亚语', '塞尔维亚语', '世界语', '斯洛文尼亚语',
    '索马里语', '泰语', '泰米尔语', '泰卢固语', '乌克兰语', '文达语', '西班牙语', '匈牙利语', '希利盖农语', '新挪威语',
    '修纳语', '巽他语', '英语', '意大利语', '因特语', '伊博语', '亚美尼亚语', '中文(简体)', '中文(粤语)', '祖鲁语',
    '爱尔兰语', '阿尔及利亚阿拉伯语', '阿姆哈拉语', '阿塞拜疆语', '爱沙尼亚语', '奥罗莫语', '波斯语', '巴斯克语',
    '柏柏尔语', '北方萨米语', '比林语', '冰岛语', '聪加语', '德语', '德顿语', '菲律宾语', '弗留利语', '刚果语',
    '格陵兰语', '古希腊语', '荷兰语', '海地语', '加利西亚语', '捷克语', '卡纳达语', '康瓦尔语', '克里克语',
    '克罗地亚语', '孔卡尼语', '老挝语', '拉脱维亚语', '卢干达语', '卢旺达语', '罗姆语', '缅甸语', '马拉雅拉姆语',
    '迈蒂利语', '毛利语', '苗语', '那不勒斯语', '南索托语', '旁遮普语', '契维语', '瑞典语', '萨摩亚语', '桑海语',
    '书面挪威语', '斯瓦希里语', '土耳其语', '他加禄语', '突尼斯阿拉伯语', '瓦隆语', '沃洛夫语', '希伯来语',
    '西弗里斯语', '下索布语', '西非书面语', '宿务语', '印地语', '越南语', '亚齐语', '伊多语', '伊努克提图特语',
    '中文(繁体)', '扎扎其语', '爪哇语', '奥克语', '阿肯语', '阿萨姆语', '阿斯图里亚斯语', '奥杰布瓦语', '布列塔尼语',
    '巴西葡萄牙语', '邦板牙语', '北索托语', '比斯拉马语', '波斯尼亚语', '鞑靼语', '迪维希语', '芬兰语', '富拉尼语',
    '高地索布语', '格鲁吉亚语', '古英语', '胡帕语', '黑山语', '加拿大法语', '卡努里语', '科萨语', '克里米亚鞑靼语',
    '克丘亚语', '库尔德语', '罗马尼亚语', '林堡语', '卢森堡语', '立陶宛语', '逻辑语', '马拉地语', '马其顿语',
    '曼克斯语', '孟加拉语', '南恩德贝莱语', '尼泊尔语', '帕皮阿门托语', '切罗基语', '塞尔维亚-克罗地亚语', '僧伽罗语',
    '斯洛伐克语', '塞尔维亚语（西里尔）', '塔吉克语', '提格利尼亚语', '土库曼语', '威尔士语', '乌尔都语', '希腊语',
    '西里西亚语', '夏威夷语', '信德语', '叙利亚语', '印尼语', '意第绪语', '印古什语', '约鲁巴语', '伊朗语',
    '中文(文言文)', '中古法语')
    ddb_default1.current(0)
    ddb_default1.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)

    ddb_default2 = ttk.Combobox(win)
    ddb_default2['value'] = (
    '阿拉伯语', '阿尔巴尼亚语', '阿拉贡语', '艾马拉语', '奥塞梯语', '奥里亚语', '波兰语', '巴什基尔语', '白俄罗斯语',
    '保加利亚语', '本巴语', '俾路支语', '博杰普尔语', '楚瓦什语', '丹麦语', '掸语', '低地德语', '俄语', '法语', '梵语',
    '法罗语', '盖尔语', '高棉语', '古吉拉特语', '瓜拉尼语', '韩语', '哈卡钦语', '豪萨语', '吉尔吉斯语', '加泰罗尼亚语',
    '卡拜尔语', '卡舒比语', '科西嘉语', '克林贡语', '克什米尔语', '拉丁语', '拉特加莱语', '林加拉语', '卢森尼亚语',
    '罗曼什语', '马来语', '马拉加斯语', '马绍尔语', '毛里求斯克里奥尔语', '马耳他语', '挪威语', '南非荷兰语',
    '葡萄牙语', '普什图语', '齐切瓦语', '日语', '萨丁尼亚语', '塞尔维亚语', '世界语', '斯洛文尼亚语', '索马里语',
    '泰语', '泰米尔语', '泰卢固语', '乌克兰语', '文达语', '西班牙语', '匈牙利语', '希利盖农语', '新挪威语', '修纳语',
    '巽他语', '英语', '意大利语', '因特语', '伊博语', '亚美尼亚语', '中文(简体)', '中文(粤语)', '祖鲁语', '爱尔兰语',
    '阿尔及利亚阿拉伯语', '阿姆哈拉语', '阿塞拜疆语', '爱沙尼亚语', '奥罗莫语', '波斯语', '巴斯克语', '柏柏尔语',
    '北方萨米语', '比林语', '冰岛语', '聪加语', '德语', '德顿语', '菲律宾语', '弗留利语', '刚果语', '格陵兰语',
    '古希腊语', '荷兰语', '海地语', '加利西亚语', '捷克语', '卡纳达语', '康瓦尔语', '克里克语', '克罗地亚语',
    '孔卡尼语', '老挝语', '拉脱维亚语', '卢干达语', '卢旺达语', '罗姆语', '缅甸语', '马拉雅拉姆语', '迈蒂利语',
    '毛利语', '苗语', '那不勒斯语', '南索托语', '旁遮普语', '契维语', '瑞典语', '萨摩亚语', '桑海语', '书面挪威语',
    '斯瓦希里语', '土耳其语', '他加禄语', '突尼斯阿拉伯语', '瓦隆语', '沃洛夫语', '希伯来语', '西弗里斯语', '下索布语',
    '西非书面语', '宿务语', '印地语', '越南语', '亚齐语', '伊多语', '伊努克提图特语', '中文(繁体)', '扎扎其语',
    '爪哇语', '奥克语', '阿肯语', '阿萨姆语', '阿斯图里亚斯语', '奥杰布瓦语', '布列塔尼语', '巴西葡萄牙语', '邦板牙语',
    '北索托语', '比斯拉马语', '波斯尼亚语', '鞑靼语', '迪维希语', '芬兰语', '富拉尼语', '高地索布语', '格鲁吉亚语',
    '古英语', '胡帕语', '黑山语', '加拿大法语', '卡努里语', '科萨语', '克里米亚鞑靼语', '克丘亚语', '库尔德语',
    '罗马尼亚语', '林堡语', '卢森堡语', '立陶宛语', '逻辑语', '马拉地语', '马其顿语', '曼克斯语', '孟加拉语',
    '南恩德贝莱语', '尼泊尔语', '帕皮阿门托语', '切罗基语', '塞尔维亚-克罗地亚语', '僧伽罗语', '斯洛伐克语',
    '塞尔维亚语（西里尔）', '塔吉克语', '提格利尼亚语', '土库曼语', '威尔士语', '乌尔都语', '希腊语', '西里西亚语',
    '夏威夷语', '信德语', '叙利亚语', '印尼语', '意第绪语', '印古什语', '约鲁巴语', '伊朗语', '中文(文言文)',
    '中古法语')
    ddb_default2.current(0)
    ddb_default2.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.1)

    # 文字提示
    lb2 = Label(win, text="Source Language")
    lb2.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.05)

    # 输入需要翻译的文本
    inp3 = Entry(win)
    inp3.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.15)

    def translate_to():
        txt.delete('1.0', tkinter.END)
        fromL = str(ddb_default1.get())
        toL = str(ddb_default2.get())
        OriginL = inp3.get()
        if OriginL=='':
            messagebox.showinfo("内容为空，输点什么")

        else:
            send_mess = "翻译:" + fromL + ":" + toL + ":" + OriginL
            socket.send(bytes(send_mess, encoding='utf-8'))
            ret = socket.recv(1024)
            print(ret.decode('utf-8'))
            arr=ret.decode('utf-8').split("+")
            a=arr[3].split(':')

            txt.insert(END, a[1])
            inp3.delete(0, END)

    def show():
        txt.delete('1.0', tkinter.END)
        send_mess = "查记录:"
        socket.send(bytes(send_mess, encoding='utf-8'))
        ret = socket.recv(1024)
        txt.insert(END, ret.decode('utf-8'))

    def identify():
        txt.delete('1.0', tkinter.END)
        fromL = str(ddb_default1.get())
        toL = str(ddb_default2.get())
        OriginL = inp3.get()
        if OriginL=='':
            messagebox.showinfo("内容为空，输点什么")
        else:
            send_mess = "翻译:" + fromL + ":" + toL + ":" + OriginL
            socket.send(bytes(send_mess, encoding='utf-8'))
            ret = socket.recv(1024)
            print(ret.decode('utf-8'))
            arr = ret.decode('utf-8').split("+")
            a = arr[0].split(':')

            txt.insert(END, a[1])
            inp3.delete(0, END)

    # 翻译按钮
    btn1 = Button(win, text='Translate', command=translate_to)
    btn1.place(relx=0.05, rely=0.5, relwidth=0.25, relheight=0.1)
    btn2 = Button(win, text='History Record', command=show)
    btn2.place(relx=0.4, rely=0.5, relwidth=0.25, relheight=0.1)
    btn3 = Button(win, text='identify language', command=identify)
    btn3.place(relx=0.7, rely=0.5, relwidth=0.3, relheight=0.1)

    # 翻译的结果
    txt = Text(win)
    txt.place(rely=0.7, relheight=0.2)
    win.mainloop()
    # 信息发送


if __name__ == '__main__':
    while isConnected()==True:
        while isConnected() == False:
            print("无网络连接")
            time.sleep(5)
        time.sleep(5)
        start()
    print("无网络连接")