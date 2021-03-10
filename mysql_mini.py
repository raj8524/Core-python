from tkinter import*
import tkinter
from tkinter import messagebox
import pymysql

''' GUI   '''
windo = tkinter.Tk()
windo.geometry("700x500")
L1=Label(windo,text=" Enter device model number : ",font=('arial',30),fg='blue')
L1.grid(row=0,column=0)
E1=Entry(windo,bd=5,width=50)
E1.grid(row=0,column=1)

L2=Label(windo,text=" enter device serial number : ",font=('arial',30),fg='blue')
L2.grid(row=1,column=0)
E2=Entry(windo,bd=5,width=50)
E2.grid(row=1,column=1)

L3=Label(windo,text=" pare or production : ",font=('arial',30),fg='blue')
L3.grid(row=2,column=0)
E3=Entry(windo,bd=5,width=50)
E3.grid(row=2,column=1)

def mybuttonEvent (selection):
    print("Enter device model number  : ",E1.get())
    print("enter device serial number : ", E2.get())
    print("spare or production  : ", E3.get())
    id = E1.get()
    name = E2.get()
    address = E3.get()
    if selection in ('Insert'):


        con = pymysql.connect("localhost","root","Ankita@1","test") # connect to database
        cur = con.cursor()
        # cur.execute("select version()")
        # data = cur.fetchone()
        # print(" mysql version",data)
        # cur.execute("DROP TABLE IF EXISTS student")
        query= "create table if not exists student (id int(10) Not null,\
               name varchar(10),address varchar(30));"
        cur.execute(query)
        con.commit()
        # try:
        #     cur.execute(query)
        #     con.commit()
        # except Error as e:
        #     print("Error occured at database table creation ", e)
        #     con.rollback()
        #     con.close()
        insQuery = "insert into student (id,name,address) values ('%s','%s','%s') "% (id, name, address)

        # cur.execute("insert into student (id,name,address) values(id,name,address);")
        # con.commit()
        # con.close()
        # insQuery="insert into student (id,name,address) values (?,?,?)"

        try:
            cur.execute(insQuery)
            con.commit()
            print("student saved to DB",)
            con.close()

        except Error as e:
            print("Error occured at database table creation", e)
            con.rollback()
            con.close()
    elif selection in ('Update'):
        try:
            query="update student set name='%s'"% (name)+",address='%s'"% (address)+" where id ='%s'"% (id)
            con = pymysql.connect("localhost", "root", "Ankita@1", "test")  # connect to database
            cur = con.cursor()
            cur.execute(query)
            con.commit()
            con.close()
            print("student updated successfully..",id)
        except Error as e:
            print("Error occured at database table Updation ", e)
            con.rollback()
            con.close()
    elif selection in ('Delete'):
        try:
            query="delete from student where id ='%s'"% (id)
            con = pymysql.connect("localhost", "root", "Ankita@1", "test")  # connect to database
            cur = con.cursor()
            cur.execute(query)
            con.commit()
            con.close()
            print("student deleted successfully..",id)
        except Error as e:
            print("Error occured at database table deletion ", e)
            con.rollback()
            con.close()
    elif selection in ('Select'):
        try:
            query="Select * from student where id ='%s'"% (id)
            con = pymysql.connect("localhost", "root", "Ankita@1", "test")  # connect to database
            cur = con.cursor()
            cur.execute(query)
            rows= cur.fetchall()
            address1 =''
            name1 = ''
            for row in rows:
                name1= row[1]
                address1 = row[2]
            E2.delete(0,END)
            E3.delete(0,END)

            E2.insert(0,name1)
            E3.insert(0,address1)


            con.close()
            print("student fetch successfully..",id)
        except Error as e:
            print("Error occured at database table fetching ", e)

            con.close()



''' Adding buttons '''

Binsert = tkinter.Button(text='Insert',fg='blue', bg='orange',font=('arial',20,'bold'),
                         command=lambda: mybuttonEvent('Insert'))
Binsert.grid(row=5,column=0)
BDelete = tkinter.Button(text='Delete',fg='black', bg='orange',font=('arial',20,'bold'),command=lambda: mybuttonEvent('Delete'))
BDelete.grid(row=5,column=1)
Bupdate = tkinter.Button(text='update',fg='red', bg='white',font=('arial',20,'bold'),command=lambda: mybuttonEvent('Update'))
Bupdate.grid(row=9,column=0)
Bselect = tkinter.Button(text='select',fg='blue', bg='yellow',font=('arial',20,'bold'),command=lambda: mybuttonEvent('Select'))
Bselect.grid(row=9,column=1)

mainloop()


