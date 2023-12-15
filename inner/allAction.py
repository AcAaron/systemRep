from tkinter import messagebox
import pymysql
from tkinter import *

#选课
def insert_choose_course(sno,cno,grade):
    db = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        database='student',
        password='123456',
        autocommit=True)
    cursor = db.cursor()
    sql = "select sno from S where sno = '%s'"%sno
    cursor.execute(sql)
    r=cursor.fetchall()
    sno=r[0][0]
    try:
        sql = "insert into SC (sno, cno, grade) values (%s, %s, %s)"
        values = (sno, cno, grade)
        cursor.execute(sql, values)
    except Exception:
        messagebox.showerror(title='提示', message="课程不存在")
        return
    db.close()

#退课
def delete_choose_course(cno,sno):
    db = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        database='student',
        password='123456',
        autocommit=True)
    cursor = db.cursor()
    try:
        sql = "delete from SC where cno = %sand sno = %s"
        values = (cno,sno)
        cursor.execute(sql,values)
    except Exception:
        messagebox.showerror(title='提示', message="课程不存在")
        return
    db.close()

#打印学生信息
def display_student(text,sno):
    db = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        database='student',
        password='123456',
        autocommit=True)
    cursor = db.cursor()
    sql = "SELECT * FROM S where S.sno='%s'"%sno
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        text.insert(END,'%s %4s %4s %4s %4s'%tuple(row[0:5]))
        text.insert(END,'\n')
    db.close()

#显示可选课程
def display_course(text,sno):
    db = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        database='student',
        password='123456',
        autocommit=True)
    cursor = db.cursor()
    sql = "select * from C where cno not in " \
          "(select SC.cno from  SC where SC.sno='%s')"%sno
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        text.insert(END,row)
        text.insert(END,'\n')
    db.close()

#显示已选课程
def display_choose_course(text,sno):
    db = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        database='student',
        password='123456',
        autocommit=True)
    cursor = db.cursor()
    sql = "select C.cno,C.cname,C.CREDI,C.CDEPT,C.tname from  S,SC,C where S.sno=SC.sno and C.cno=SC.cno and S.sno='%s'" % sno
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        text.insert(END,row)
        text.insert(END,'\n')
    db.close()

#显示学生成绩
def display_score(text,sno):
    db = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        database='student',
        password='123456',
        autocommit=True)
    cursor = db.cursor()
    sql = "select C.cno,C.cname,grade from  S,SC,C where S.sno=SC.sno and C.cno=SC.cno and S.sno='%s'"%sno
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        text.insert(END,row)
        text.insert(END,'\n')
    db.close()

#老师所上的课程
def find_teacher_course(name):
    db = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        database='student',
        password='123456',
        autocommit=True)
    cursor = db.cursor()
    sql = "SELECT cname FROM C where tname='%s'" % name
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result

#查询选了该老师该课的学生
def find_student_score(text,cname,tname):
    db = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        database='student',
        password='123456',
        autocommit=True)
    cursor = db.cursor()
    sql = "select S.sno,S.sname,SC.grade from  S,SC,C where S.sno=SC.sno and C.cno=SC.cno and C.cname='%s' and C.tname='%s'"%(cname,tname)
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        text.insert(END,row)
        text.insert(END,'\n')
    db.close()

#老师修改成绩
def change_score(sno,cno,grade):
    db = pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        database='student',
        password='123456',
        autocommit=True)
    cursor = db.cursor()

    sql = "update SC set grade='%s' where sno = '%s' and cno = '%s'" % (grade, sno,cno)
    cursor.execute(sql)
    messagebox.showinfo(title='提示', message="修改成功")
    db.close()