#/- Imports ---------------------/#
try:
    from tkinter import *
    from tkinter import messagebox
    from sys import argv
    from os import system
    import sqlite3
except Exception as error_imports:
     print(error_imports)
#/------------------------------/#
#/- Creating the bank -----------------------------------------------------------------/#
connect = sqlite3.connect("bank.db")
cursor = connect.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    jobrole TEXT NOT NULL,
    salary TEXT NOT NULL)
""")
connect.commit()
#/------------------------------------------------------------------------------------/#
#/- Graphic Interface --------------------------------------------------------------------------------------------------------/#
class Root():
    def __init__(self,window):
        #/- Window -----------------------------------------------------------------------------------------------------------/#
        self.window = window
        #/- Code ID Widgets --------------------------------------------------------------------------------------------------/#
        lb_code = Label(self.window,text="Code ID                                                        ",font=("Arial",11)).grid(row=0,column=0)
        self.ent_code = Entry(self.window,width=35)
        self.ent_code.grid(row=1,column=0)
        #/--------------------------------------------------------------------------------------------------------------------/#
        #/- Firstname Widgets ------------------------------------------------------------------------------------------------/#
        lb_fname = Label(self.window,text="Firstname                                                     ",font=("Arial",11)).grid(row=2,column=0)
        self.ent_fname = Entry(self.window,width=35)
        self.ent_fname.grid(row=3,column=0)
        #/--------------------------------------------------------------------------------------------------------------------/#
        #/- Lastname Widgets ------------------------------------------------------------------------------------------------/#
        lb_lname = Label(self.window,text="Lastname                                                     ",font=("Arial",11)).grid(row=4,column=0)
        self.ent_lname = Entry(self.window,width=35)
        self.ent_lname.grid(row=5,column=0)
        #/-------------------------------------------------------------------------------------------------------------------/#
        #/- Email Widgets ------------------------------------------------------------------------------------------------------/#
        lb_email = Label(self.window,text="E-mail                                                          ",font=("Arial",11)).grid(row=6,column=0)
        self.ent_email = Entry(self.window,width=35)
        self.ent_email.grid(row=7,column=0)
        #/----------------------------------------------------------------------------------------------------------------------/#
        #/- Phone Widgets -----------------------------------------------------------------------------------------------------/#
        lb_phone = Label(self.window,text="Phone                                                          ",font=("Arial",11)).grid(row=8,column=0)
        self.ent_phone = Entry(self.window,width=35)
        self.ent_phone.grid(row=9,column=0)
        #/- Job Role Widgets --------------------------------------------------------------------------------------------------/#
        lb_jobrole = Label(self.window,text="Job Role                                                      ",font=("Arial",11)).grid(row=10,column=0)
        self.ent_jobrole = Entry(self.window,width=35)
        self.ent_jobrole.grid(row=11,column=0)
        #/---------------------------------------------------------------------------------------------------------------------/#
        #/- Salary --------------------------------------------------------------------------------------------------------------/#
        lb_salary = Label(self.window,text="Salary                                                          ",font=("Arial",11)).grid(row=12,column=0)
        self.ent_salary = Entry(self.window,width=35)
        self.ent_salary.grid(row=13,column=0)
        #/-----------------------------------------------------------------------------------------------------------------------/#
        #/-Buttons --------------------------------------------------------------------------------------------------------------/#
        bt_search = Button(self.window,text="Search",font=("Arial",11)).grid(row=14,column=0,sticky=W,padx=5,pady=10)
        bt_new = Button(self.window,text="New",font=("Arial",11),command=self.new).grid(row=14,column=0,stick=W,padx=79)
        bt_update = Button(self.window,text="Update",font=("Arial",11)).grid(row=14,column=0,stick=E,padx=75)
        bt_delete = Button(self.window,text="Delete",font=("Arial",11)).grid(row=14,column=0,stick=E,padx=5)
        #/-----------------------------------------------------------------------------------------------------------------------/#
    def new(self):
        gfname = self.ent_fname.get()
        glname = self.ent_lname.get()
        gemail = self.ent_email.get()
        gphone = self.ent_phone.get()
        gjobrole = self.ent_jobrole.get()
        gsalary = self.ent_salary.get()
        cursor.execute("""
            INSERT INTO users(fname, lname, email, phone, jobrole, salary)
            VALUES("{}","{}","{}","{}","{}","{}")
        """.format(gfname,glname,gemail,gphone,gjobrole,gsalary))

        connect.commit()
#/-------------------------------------------------------------------------------------------------------------------------------/#
#/- Instances -----------------------/#
try:
    instance_tk = Tk()
    Root(instance_tk)
    instance_tk.title("PyCrudJob")
    instance_tk.resizable(FALSE, FALSE)
    instance_tk.mainloop()
except Exception as error_instances:
    print(error_instances)
#/-----------------------------------/#
