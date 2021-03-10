import mysql.connector
from tkinter import *
import tkinter.messagebox
from mysql.connector import Error
# class for front END UI
class product:
    def __init__(self,root):
        ## create object reference
        p=database()
        p.conn()

        self.root=root
        self.root.title("WAREHOUSE INVENTORY")
        self.root.geometry("1200x800")
        self.root.config(bg="yellow")
        pID=StringVar()
        pName=StringVar()
        pPrice=StringVar()
        pQty=StringVar()
        pCompany=StringVar()
        pContact=StringVar()
        ''' Lets call databse methods to perform databse operation'''
        # fucnction to close
        def close():
            print("product : close method called")
            close=tkinter.messagebox.askyesno("Warehouse inventory","Do you want to close ?")
            if close>0:
                root.destroy()
                print("product : close method finished\n")
        # function to clear
        def clear():
            print("product: clear method called")
            self.txtpID.delete(0,END)
            self.txtpName.delete(0, END)
            self.txtpPrice.delete(0, END)
            self.txtpQty.delete(0, END)
            self.txtpCompany.delete(0, END)
            self.txtpContact.delete(0, END)
            print("product: clear method finished\n")
        # function to save product details in DB
        def insert():
            print("product: Insert method called")
            if (len(pID.get())!=0):
                p.insert(pID.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get())
                productList.delete(0,END)
                productList(END,pID.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get())
                showInProductList() # to show table
            else:
                tkinter.messagebox.askyesno("Warehouse inventory"," Enter product ID")

        ## show product table
        def showInProductList():
            print("product: Insert method called")
            productList.delete(0,END)
            for row in p.show():
                productList.insert(END,row,str(""))
            print("product: showInProductList method finished\n")
        ## add to scroll bar
        def prodctRec(event):## to be called from scrollbar
            print("product: prodctRec method called")
            global pd
            searchpd=productList.curselection()[0]
            pd=productList.get(searchpd)
            self.txtpID.delete(0,END)
            self.txtpID.insert(END,pd[0])
            self.txtpName.delete(0,END)
            self.txtpName.insert(END,pd[1])
            self.txtpPrice.delete(0,END)
            self.txtpPrice.insert(END,pd[2])
            self.txtpQty.delete(0, END)
            self.txtpQty.insert(END,pd[3])
            self.txtpCompany.delete(0,END)
            self.txtpCompany.insert(END,pd[4])
            self.txtpContact.delete(0,END)
            self.txtpContact.insert(END,pd[5])
            print("product: prodctRec method finished\n"
            # delete func data from record
        def delete():
            print("product : delete method called")
            if (len(pID.get())!=0):
                p.delete(pd[0])
                clear()
                showInProductList()
                print("product: delete method finished\n"
                      
              ''' search from database table'''

        def search():
            print("product : delete method called")
            productList.delete(0,END)
            for row in p.search(pID.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get()):
                productList.insert(END,row,str(""))
                print("product: search method finished\n"

        def update():
            print("product : update method called")
            if (len(pID.get())!=0):
                print("pd[0]",pd[p])
                p.delete(pd[p])
            if (len(pID.get())!=0):
                p.insert(pID.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get())
                productList.delete(0,END)
            productList.insert(END,(pID.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get()))
            print("product: search method finished\n"

                      ''' create the frame'''
        MainFrame= Frame(self.root,bg="red")
        MainFrame.grid()
        HeadFrame=Frame(MainFrame,bd=1,padx=50,pady=10,bg='white',relief=RIDGE)
        HeadFrame.pack(side=TOP)
        self.ITitle=Label(HeadFrame,font=('aerial',50,'bold'),fg='red',text='Warehouse Inventory sales purchase')
        self.ITitle.grid()
        OperationFrame=Frame(MainFrame,bd=2,width=1300,height=60,padx=50,pady=20,bg='white',relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)
        BodyFrame= Frame(MainFrame,bd=2,width=1290,height=400,padx=30,pady=20,bg='white',relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)
        LeftBodyframe=LabelFrame(BodyFrame,bd=2,width=600,height=380,padx=20,pady=10,bg='yellow',
                            relief=RIDGE,font=('arial',15,'bold'),text='Pdoduct Item details')
        LeftBodyframe.pack(side=LEFT)
        RightBodyframe = LabelFrame(BodyFrame, bd=2, width=600, height=380, padx=20, pady=10, bg='yellow',
                                   relief=RIDGE, font=('arial', 15, 'bold'), text='Pdoduct Item details')
        RightBodyframe.pack(side=RIGHT)
        ''' Add the widgets to LeftBodyFrame'''
        self.labelpID=Label(LeftBodyframe,font=('arial',15,'bold'),text="Product Id : ",padx=2, pady=2,bg='white',fg='blue')
        self.labelpID.grid(row=0,column=0,sticky=W)
        self.txtpID= Entry(LeftBodyframe,font=('arial',15,'bold'),
         textvariable=pID,width=30)
        self.txtpID.grid(row=0,column=1,sticky=W)

        self.labelpName = Label(LeftBodyframe, font=('arial', 15, 'bold'), text="Product Name : ", padx=2, pady=2,bg='white',
                              fg='blue')
        self.labelpName.grid(row=1, column=0, sticky=W)
        self.txtpName = Entry(LeftBodyframe, font=('arial', 15, 'bold'),
                            textvariable=pName, width=30)
        self.txtpName.grid(row=1, column=1, sticky=W)
        self.labelpPrice = Label(LeftBodyframe, font=('arial', 15, 'bold'), text="Product price : ", padx=2, pady=2,bg='white',
                                fg='blue')
        self.labelpPrice.grid(row=2, column=0, sticky=W)

        self.txtpPrice = Entry(LeftBodyframe, font=('arial', 15, 'bold'),
                            textvariable=pPrice, width=30)
        self.txtpPrice.grid(row=2, column=1, sticky=W)

        self.labelpQty = Label(LeftBodyframe, font=('arial', 15, 'bold'), text="Product Quantity : ", padx=2, pady=2,bg='white',
                                fg='blue')
        self.labelpQty.grid(row=3, column=0, sticky=W)
        self.txtpQty = Entry(LeftBodyframe, font=('arial', 15, 'bold'),
                            textvariable=pQty, width=30)
        self.txtpQty.grid(row=3, column=1, sticky=W)
        self.labelpComapany = Label(LeftBodyframe, font=('arial', 15, 'bold'), text="Mfg. Company : ", padx=2, pady=2,bg='white',
                               fg='blue')
        self.labelpComapany.grid(row=4, column=0, sticky=W)
        self.txtpCompany = Entry(LeftBodyframe, font=('arial', 15, 'bold'),
                            textvariable=pCompany, width=30)
        self.txtpCompany.grid(row=4, column=1, sticky=W)
        self.labelpContact = Label(LeftBodyframe, font=('arial', 15, 'bold'), text="Company Contcat : ", padx=2, pady=2,bg='white',
                               fg='blue')
        self.labelpContact.grid(row=5, column=0, sticky=W)
        self.txtpContact = Entry(LeftBodyframe, font=('arial', 15, 'bold'),
                            textvariable=pContact, width=30)
        self.txtpContact.grid(row=5, column=1, sticky=W)

        self.labelpC1=Label(LeftBodyframe,padx=2,pady=2)
        self.labelpC1.grid(row=6,column=0,sticky=W)
        self.labelpC1 = Label(LeftBodyframe, padx=2, pady=2)
        self.labelpC1.grid(row=7, column=0, sticky=W)
        self.labelpC1 = Label(LeftBodyframe, padx=2, pady=2)
        self.labelpC1.grid(row=8, column=0, sticky=W)
        self.labelpC1 = Label(LeftBodyframe, padx=2, pady=2)
        self.labelpC1.grid(row=9, column=0, sticky=W)

        ''' add Scroll bar'''
        scroll=Scrollbar(RightBodyframe)
        scroll.grid(row=0,column=1,sticky='ns')
        productList=Listbox(RightBodyframe, width=40, height=16,font=('arial',12,'bold'),
                                                        yscrollcommand=scroll.set)
        ## called created prodctRec func
        productList.bind('<<ListboxSelect>>',prodctRec)

        productList.grid(row=0,column=0,padx=8)
        scroll.config(command=productList.yview)

        '''Add the buttons to operation Frame'''
        self.buttonSave=Button(OperationFrame,text='Save',font=('arial',18,
           'bold'),height=1,width=10,bd=4,command=insert)
        self.buttonSave.grid(row=0,column=0)

        self.buttonShowData = Button(OperationFrame, text='Show', font=('arial', 18,
                                                                    'bold'), height=1, width=10, bd=4,command=showInProductList)
        self.buttonShowData.grid(row=0, column=1)

        self.buttonClear = Button(OperationFrame, text='Clear', font=('arial', 18,
                                                                    'bold'), height=1, width=10, bd=4,command=clear)
        self.buttonClear.grid(row=0, column=2)

        self.buttonDelete = Button(OperationFrame, text='Delete', font=('arial', 18,
                                                                    'bold'), height=1, width=10, bd=4,command=delete)
        self.buttonDelete.grid(row=0, column=3)

        self.buttonSearch = Button(OperationFrame, text='Search', font=('arial', 18,
                                                                    'bold'), height=1, width=10, bd=4,command=search)
        self.buttonSearch.grid(row=0, column=4)

        self.buttonupdate = Button(OperationFrame, text='update', font=('arial', 18,
                                                                    'bold'), height=1, width=10, bd=4,command=update)
        self.buttonupdate.grid(row=0, column=5)

        self.buttonclose = Button(OperationFrame, text='close', font=('arial', 18,
                                                                    'bold'), height=1, width=10, bd=4)
        self.buttonclose.grid(row=0, column=6)


    ''' DB connecting'''
class database:
    def conn(self):
        print("Database : connection method called")
        con=mysql.connector.connect(host='localhost',database='warehouse',
                  user='root', password='root')
        mycursor=con.cursor()
        mycursor.execute("DROP TABLE IF EXISTS product")
        # query="create table product(pid int(5) primary key,pname varchar(10),price int(5),\
        #          qty int(5),company varchar(10),contact int(10))"
        mycursor.execute("create table product(pid int(5) primary key,pname varchar(10),price int(5),qty int(5),company varchar(10),contact int(10))")

        con.commit()
        con.close()
        print("Database : connection method finished \n")

    def insert(self,pid,name,price,qty,company,contact):
        print("Database : insert method called")
        con=mysql.connector.connect('warehouse')
        cur=con.cursor()
        query="insert into product values(?,?,?,?,?,?)"
        cur.execute(query,(pid,name,price,qty,company,contact))
        con.commit()
        con.close()
        print("Database : Insert method finished \n")
    def show(self):
        print("Database : show method called")
        con = mysql.connector.connect('warehouse')
        cur = con.cursor()
        query="select * from product"
        cur.execute(query)
        rows=cur.fetchall()
        con.close()
        print("Datebase : show method finished\n")
        return rows
    def delete(selfself,pid):
        print("Database : delete method called",pid)
        con = mysql.connector.connect('warehouse')
        cur = con.cursor()
        cur.execute("delete from product where pid=?",(pid,))
        con.commit()
        con.close()
        print(pid,"Datebase : delete method finished\n")

    def search(self,pid="",price="",qty="",company="",contact=""):
        print("Database : delete method called", pid)
        con = mysql.connector.connect('warehouse')
        cur = con.cursor()
        cur.execute("select * from product where pid=? or pname=? or price=? or \
                    qty=? or compant=? contact=?")
        row=cur.fetchall()
        con.close()
        print(pid, "Datebase : search method finished\n")
        return row
    def update(self,pid="",price="",qty="",company="",contact=""):
        print("Database : update method called", pid)
        con = mysql.connector.connect('warehouse')
        cur = con.cursor()
        cur.execute("update product set pid=? or pname=? or price=? or \
                            qty=? or compant=? contact=? where pid=?",(pid,name,price,qty,company,
                                                contact,pid))
        con.commit()
        con.close()
        print(pid, "Datebase : update method finished\n")

if __name__ =='__main__':
    root=Tk()
    applicationtion=product(root)
    root.mainloop()

#
# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='warehouse',
#                                          user='root',
#                                          password='root')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)
#
# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")
