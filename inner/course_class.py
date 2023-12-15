from tkinter import *
import inner.allAction as allAction

class course:
    def __init__(self,sno,root1):
        self.r = root1
        self.sno=sno
        self.root1 = Toplevel(self.r)
        self.root1.title(sno)
        self.root1.resizable(0, 0)  # 禁止调整宽高
        self.sw = self.root1.winfo_screenwidth()  # 得到屏幕宽度
        self.sh = self.root1.winfo_screenheight()
        self.ww = 950
        self.wh = 450
        self.x = (self.sw - self.ww) / 2
        self.y = (self.sh - self.wh) / 2
        self.root1.geometry("%dx%d+%d+%d" % (self.ww, self.wh, self.x, self.y))  # 调整窗口位置和大小
        self.student_label = Label(self.root1, text="学生详细信息：")
        self.course_label = Label(self.root1, text="可选课程")
        self.score_label = Label(self.root1, text="已修课程成绩")
        self.choose_course_label = Label(self.root1, text="已选课程")
        self.course_entry_label = Label(self.root1, text="请输入课程号：")
        self.student_text = Text(self.root1, height=10, width=50)
        self.course_text = Text(self.root1, height=10, width=50)
        self.score_text = Text(self.root1, height=10, width=50)
        self.choose_course_text = Text(self.root1, height=10, width=50)
        self.course_entry = Entry(self.root1, width=5)
        self.course_button = Button(self.root1, text="选课", command=self.choose_course)
        self.course_button2 = Button(self.root1, text="退课", command=self.delete_course)
        self.course_button3 = Button(self.root1, text="退出",command=self.transfer)
    def ini(self):
        self.student_label.grid(row=0, column=0)
        self.student_text.grid(row=1, column=0)
        self.course_label.grid(row=0, column=1)
        self.course_text.grid(row=1, column=1)
        self.score_label.grid(row=3, column=0)
        self.score_text.grid(row=4, column=0)
        self.choose_course_label.grid(row=3, column=1)
        self.choose_course_text.grid(row=4, column=1)
        self.course_entry_label.grid(row=0, column=3)
        self.course_entry.grid(row=1, column=3)
        self.course_button.grid(row=1, column=4)
        self.course_button2.grid(row=3, column=4)
        self.course_button3.grid(row=4, column=4)
    #退出
    def transfer(self):
        if self.r.state() == "withdrawn":
            self.r.deiconify()
            self.root1.destroy()
        else:
            self.r.withdraw()

    # 选课
    def choose_course(self):
        course_number = self.course_entry.get()
        allAction.insert_choose_course(self.sno, course_number, 0)
        self.update_ui()

    # 退课
    def delete_course(self):
        course_number = self.course_entry.get()
        allAction.delete_choose_course(course_number, self.sno)
        self.update_ui()

    # 更新ui
    def update_ui(self):
        self.student_text.delete(1.0, END)
        self.course_text.delete(1.0, END)
        self.score_text.delete(1.0, END)
        self.choose_course_text.delete(1.0, END)
        allAction.display_student(self.student_text, self.sno)
        allAction.display_course(self.course_text, self.sno)
        allAction.display_score(self.score_text, self.sno)
        allAction.display_choose_course(self.choose_course_text, self.sno)

    def start(self):
        self.ini()
        self.update_ui()
        self.root1.mainloop()


if __name__=='__main__':
    root = Tk()
    c=course('5',root)
    c.start()