from tkinter import *
from tkinter import messagebox
import signup,teacher_login
import inner.course_class as course_class
import pymysql
def judge():
    logn=entryName.get()
    password=entryPwd.get()
    db = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        database='student',
        password='123456',
        autocommit=True)
    cursor = db.cursor()

    if logn=='' or password=='':
        messagebox.showinfo(title='提示', message='用户名或密码不能为空')
        return

    sql1 = "SELECT S.logn FROM S where S.logn='%s'" % (logn)
    sql2 = "SELECT S.pswd FROM S where S.logn='%s'and S.pswd='%s'" % (logn,password)
    cursor.execute(sql1)
    result1 = cursor.fetchall()
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    db.close()
    if len(result1)==0:
        messagebox.showerror(title='提示', message="用户不存在")
        return
    elif len(result2)==0:
        messagebox.showerror(title='提示', message="密码错误")
        return
    elif len(result1)==0 and len(result2)==0:
        messagebox.showerror(title='提示', message="用户名或密码错误")
        return
    return result1

def start():

    result=judge()
    db = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        database='student',
        password='123456',
        autocommit=True)
    cursor = db.cursor()
    try:
        sql = "select sno from S where logn='%s'"%result[0][0]
        cursor.execute(sql)
        result1=cursor.fetchall()
        sno=result1[0][0]
    except Exception:
        pass

    try:
        if len(result)!=0:
            root.withdraw()
            if result[0][0][0]=='S' or result[0][0][0]=='s':
                c=course_class.course(sno,root)
                cancel()
                c.start()

    except Exception:
        cancel()

def cancel():
    # 清空用户输入的用户名和密码
    varName.set('')
    varPwd.set('')

def enroll():
    root.withdraw()     #隐藏窗口
    e=signup.signup_user(root)
    e.start()

def tlogin():
    root.withdraw()     #隐藏窗口
    e=teacher_login.tlogin(root)
    e.ini()

root = Tk()                  #创建窗口
root.title("用户登录")
root.resizable(0, 0)             #禁止调整宽高
sw=root.winfo_screenwidth()     #得到屏幕宽度
sh=root.winfo_screenheight()
ww=370
wh=280
x=(sw-ww)/2
y=(sh-wh)/2
root.geometry("%dx%d+%d+%d" %(ww, wh, x, y))  #指定窗口大小及在屏幕上的位置

f = Label(root, text='Welcome', justify=RIGHT, width=80,bg="#ADD8E6", font=('Arial', 20))
f.place(x=0, y=12, width=370, height=50)

varName = StringVar()
varName.set('')
varPwd = StringVar()
varPwd.set('')

#登录界面中的各个组件设计
labelName = Label(root, text='用户名：', justify=RIGHT, width=80)
labelPwd = Label(root, text='密  码：', justify=RIGHT, width=80)
entryName = Entry(root, width=80, textvariable=varName)
entryPwd = Entry(root, show='*', width=80, textvariable=varPwd)
buttonOk = Button(root, text='登录',  command=start)
buttonCancel = Button(root, text='重置', command=cancel)
buttonenroll = Button(root, text='注册', command=enroll)
buttontlogin = Button(root, text='教师登录', command=tlogin)


#设定登录界面中各个组件的排放位置
labelName.place(x=80, y=90, width=80, height=20)
labelPwd.place(x=80, y=130, width=80, height=20)
entryName.place(x=140, y=90, width=110, height=20)
entryPwd.place(x=140, y=130, width=110, height=20)
buttonOk.place(x=90, y=180, width=50, height=20)
buttonCancel.place(x=150, y=180, width=50, height=20)
buttonenroll.place(x=210, y=180, width=50, height=20)
buttontlogin.place(x=90, y=210, width=170, height=20)

root.mainloop()