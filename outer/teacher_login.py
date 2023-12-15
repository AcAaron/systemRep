import tkinter as tk
from tkinter import ttk
import inner.teacher_class as teacher_class
import pymysql

class tlogin:
    def __init__(self, root):
        self.r = root
        self.root1 = tk.Tk()
        self.root1.title("教师登录")
        self.root1.resizable(0, 0)  # 禁止调整宽高
        self.sw = self.root1.winfo_screenwidth()  # 得到屏幕宽度
        self.sh = self.root1.winfo_screenheight()
        self.ww = 350
        self.wh = 150
        self.x = (self.sw - self.ww) / 2
        self.y = (self.sh - self.wh) / 2
        self.root1.geometry("%dx%d+%d+%d" % (self.ww, self.wh, self.x, self.y))  # 调整窗口位置和大小
        self.com = ttk.Combobox(self.root1, state="readonly")



    def transfer(self):
        if self.r.state() == "withdrawn":
            self.r.deiconify()
            self.root1.destroy()
        else:
            self.r.withdraw()

    def start(self,rname):
        self.root1.destroy()
        t = teacher_class.Teacher(rname,self.r)
        t.start()

    def ini(self):
        db = pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            database='student',
            password='123456',
            autocommit=True)
        cursor = db.cursor()
        sql="select distinct tname from c"
        cursor.execute(sql)
        self.com["value"] = cursor.fetchall()
        self.com.place(x=110, y=30, width=130, height=20)
        f2 = tk.Label(self.root1, text='选择账号->', justify=tk.RIGHT, width=80)
        f2.config(foreground="blue", font=("Helvetica", 10))
        f2.place(x=0, y=30, width=100, height=20)
        self.com.bind("<<ComboboxSelected>>", lambda event: self.start(self.com.get()))
        buttonquit = tk.Button(self.root1, text="退出", command=self.transfer)
        buttonquit.place(x=150, y=100, width=50, height=20)


