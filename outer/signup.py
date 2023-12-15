import tkinter as tk
from tkinter import messagebox
import pymysql
class signup_user:
    def __init__(self,root):
        self.r=root
        self.root1=tk.Toplevel(self.r)
        self.root1.title("学生注册")
        self.root1.resizable(0, 0)  # 禁止调整宽高
        self.sw = self.root1.winfo_screenwidth()  # 得到屏幕宽度
        self.sh = self.root1.winfo_screenheight()
        self.ww = 370
        self.wh = 250
        self.x = (self.sw - self.ww) / 2
        self.y = (self.sh - self.wh) / 2
        self.root1.geometry("%dx%d+%d+%d" % (self.ww, self.wh, self.x,self.y))  # 调整窗口位置和大小

    def ini(self):
        self.varName = tk.StringVar()
        self.varName.set('s')
        self.varName2 = tk.StringVar()
        self.varName2.set('')
        self.varPwd = tk.StringVar()
        self.varPwd.set('')
        self.varPwd2 = tk.StringVar()
        self.varPwd2.set('')

        labelName = tk.Label(self.root1, text='用户名：', justify=tk.RIGHT, width=80)
        labelName2 = tk.Label(self.root1, text='姓  名：', justify=tk.RIGHT, width=80)
        labelPwd = tk.Label(self.root1, text='密  码：', justify=tk.RIGHT, width=80)
        labelPwd2 = tk.Label(self.root1, text='重复密码：', justify=tk.RIGHT, width=80)
        self.entryName = tk.Entry(self.root1, width=10, textvariable=self.varName)
        self.entryName2 = tk.Entry(self.root1, width=10, textvariable=self.varName2)
        self.entryPwd = tk.Entry(self.root1, show='*', width=10, textvariable=self.varPwd)
        self.entryPwd2 = tk.Entry(self.root1, show='*', width=10, textvariable=self.varPwd2)
        f1 = tk.Label(self.root1, text='密码最少为2位', justify=tk.RIGHT, width=80)
        f2 = tk.Label(self.root1, text='以s开头且最多6位', justify=tk.RIGHT, width=80)
        f1.config(foreground="red", font=("Helvetica", 10))
        f2.config(foreground="red", font=("Helvetica", 10))
        buttonregister = tk.Button(self.root1, text='注册', command=self.register)
        buttonquit = tk.Button(self.root1, text="退出", command=self.transfer)

        labelName.place(x=80, y=30, width=80, height=20)
        labelName2.place(x=80, y=70, width=80, height=20)
        labelPwd.place(x=80, y=110, width=80, height=20)
        labelPwd2.place(x=80, y=150, width=80, height=20)

        self.entryName.place(x=140, y=30, width=110, height=20)
        self.entryName2.place(x=140, y=70, width=110, height=20)
        f1.place(x=140, y=130, width=110, height=20)
        f2.place(x=140, y=50, width=110, height=20)
        self.entryPwd.place(x=140, y=110, width=110, height=20)
        self.entryPwd2.place(x=140, y=150, width=110, height=20)

        buttonregister.place(x=200, y=180, width=50, height=20)
        buttonquit.place(x=140, y=180, width=50, height=20)

    def transfer(self):
        if self.r.state() == "withdrawn":
            self.r.deiconify()
            self.root1.destroy()
        else:
            self.r.withdraw()

    def start(self):
        self.ini()
        self.root1.mainloop()

    def delete(self):
        self.varName.set("s")
        self.varName2.set("")
        self.varPwd.set("")
        self.varPwd2.set("")

    def register(self):
        # 获取用户输入的用户名和密码
        username = self.entryName.get()
        username2 = self.entryName.get()
        password = self.entryPwd.get()
        password2 = self.entryPwd2.get()

        if not username or not password or not password2 or not username2:
            messagebox.showerror("错误", "姓名或用户名或密码不能为空")
            return
        if  len(password)<2:
            messagebox.showinfo("提示", "密码至少2位")
            self.delete()
            return
        if  len(username)>6:
            messagebox.showinfo("提示", "名称最多为六位")
            return

        # 数据库中的用户信息
        db = pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            database='student',
            password='123456',
            autocommit=True)
        cursor = db.cursor()
        sql = "SELECT S.logn FROM S where S.logn='%s'" % username
        cursor.execute(sql)
        result = cursor.fetchall()

        # 判断密码是否一致
        if password2 != password:
            messagebox.showerror("错误", "密码不一致")
            return

        # 判断用户名是否存在
        if len(result)!=0:
            messagebox.showinfo("提示", "用户名已存在")
            return
        else:
            sql="insert into  S(sname,logn,pswd) values('%s','%s','%s')" % (username2,username,password)
            cursor.execute(sql)
        # 注册成功，弹出提示框
        messagebox.showinfo("成功", "注册成功")
        self.delete()
        db.close()
if __name__=="__main__":
    root=tk.Tk()
    s=signup_user(root)
    s.start()




