from tkinter import *
import inner.allAction as allAction
from tkinter import messagebox
import pymysql
class Teacher:
    def __init__(self,tname,root):
        self.tname=tname
        self.r = root
        self.root1 = Toplevel(self.r)
        self.root1.title(tname)
        self.root1.resizable(0, 0)  # 禁止调整宽高
        self.sw = self.root1.winfo_screenwidth()  # 得到屏幕宽度
        self.sh = self.root1.winfo_screenheight()
        self.ww = 455
        self.wh = 420
        self.x = (self.sw - self.ww) / 2
        self.y = (self.sh - self.wh) / 2
        self.root1.geometry("%dx%d+%d+%d" % (self.ww, self.wh, self.x, self.y))  # 调整窗口位置和大小
        self.flag=None   #用于选中课程
        self.v = StringVar()
        self.v.set('')
        self.v2 = StringVar()
        self.v2.set('')
        Label(self.root1, text="请选择课程名：").grid(row=1, column=0)
        Label(self.root1, text="已选修此课程的学生：").grid(row=1, column=1)

        self.student_text = Text(self.root1, width=20, height=16)
        self.lb = Listbox(self.root1, width=20, height=12)

        Label(self.root1,text="学号：").grid(row=3,column=1)
        Label(self.root1, text="成绩：").grid(row=5, column=1)
        self.student_id_entry = Entry(self.root1, width=15,textvariable=self.v)
        self.student_grade_entry = Entry(self.root1, width=15,textvariable=self.v2)
        self.student_button = Button(self.root1, text="查询", command=self.find_score)
        self.quit_button = Button(self.root1, text="退出", command=self.transfer)
        self.score_button =Button(self.root1, text="输入成绩", command=self.change_score)

    def ini(self):
        f = Label(self.root1, text='请\n查\n询\n后\n打\n分\n\n<-', width=80, bg="tan", font=('Arial', 20))
        f.place(x=290, y=25, width=110, height=355)

        self.student_text.grid(row=2, column=1)
        self.lb.grid(row=2, column=0)
        for item in allAction.find_teacher_course(self.tname):
            self.lb.insert(END, item)

        self.student_id_entry.grid(row=4, column=1)
        self.student_grade_entry.grid(row=6, column=1)
        # 查询
        self.student_button.place(x=20, y=260, width=110, height=30)
        # 输入成绩
        self.score_button.place(x=160, y=350, width=110, height=30)
        #退出
        self.quit_button.place(x=20, y=300, width=110, height=30)

    def transfer(self):
        if self.r.state() == "withdrawn":
            self.r.deiconify()
            self.root1.destroy()
        else:
            self.r.withdraw()

    # 查询选了该老师该课的学生成绩
    def find_score(self):
        try:
            self.flag =  self.lb.selection_get()
            cname = self.lb.selection_get()
            self.student_text.delete(1.0, END)
            allAction.find_student_score(self.student_text, cname, self.tname)
        except Exception:
            messagebox.showinfo("提示", "请选择课程")
            self.delete()

    #修改成绩
    def change_score(self):
        db = pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            database='student',
            password='123456',
            autocommit=True)
        cursor = db.cursor()
        try:
            sql = "select cno from C where cname='%s'"%self.flag
            cursor.execute(sql)
            result = cursor.fetchall()
            cno=result[0][0]
        except Exception:
            messagebox.showinfo("提示", "请选择课程")
            self.delete()
            return
        sno = self.student_id_entry.get()
        grade = self.student_grade_entry.get()

        try:
            sql = "select * from SC where sno='%s' and cno='%s'"%(sno,cno)
            cursor.execute(sql)
            result=cursor.fetchall()
            if len(result)==0 or len(grade)==0:
                a=0/0
        except Exception:
            messagebox.showerror("错误", "输入有误")
            return
        if not grade.isdigit():
            messagebox.showerror("错误", "请输入数字")
            return
        allAction.change_score(int(sno),int(cno),int(grade))
        self.delete()
        self.find_score()

    def start(self):
        self.ini()
        self.root1.mainloop()

    def delete(self):
        self.v.set("")
        self.v2.set("")


if __name__=='__main__':
    root = Tk()
    c=Teacher('刘红',root)
    c.start()