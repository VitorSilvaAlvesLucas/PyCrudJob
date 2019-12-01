#/- Imports ---------------------/#
try:
    from tkinter import *
    from io import open
    from tkinter import messagebox
    from sys import exit
    from os import system
    from getpass import getuser
    import sqlite3
except Exception as error_imports:
     messagebox.showerror("Error",error_imports)
#/------------------------------/#
#/- Creating the bank -----------------------------------------------------------------/#
try:
    user = getuser()
    connect = sqlite3.connect("/home/{}/bank.db".format(user),timeout=10)
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT NOT NULL,
        jobrole TEXT NOT NULL,
        salary TEXT NOT NULL)
    """)
    connect.commit()
except Exception as error_createdb:
    messagebox.showerror("Error",error_createdb)
#/-------------------------------------------------------------------------------------/#
#/- Graphic Interface ---------------------------------------------------------------------------------------------------------------------------/#
class Root():
    def __init__(self,window):
        #/- Window -----------------------------------------------------------------------------------------------------------------------------/#
        self.window = window
        self.window.protocol("WM_DELETE_WINDOW", lambda:self.exitx())
        #/- Code ID Widgets --------------------------------------------------------------------------------------------------------------------/#
        lb_code = Label(self.window,text="Code ID                                                        ",font=("Arial",11)).grid(row=0,column=0)
        self.ent_code = Entry(self.window,width=35)
        self.ent_code.grid(row=1,column=0)
        #/--------------------------------------------------------------------------------------------------------------------------------------/#
        #/- Firstname Widgets ------------------------------------------------------------------------------------------------------------------/#
        lb_fname = Label(self.window,text="Firstname                                                     ",font=("Arial",11)).grid(row=2,column=0)
        self.ent_fname = Entry(self.window,width=35)
        self.ent_fname.grid(row=3,column=0)
        #/--------------------------------------------------------------------------------------------------------------------------------------/#
        #/- Lastname Widgets ------------------------------------------------------------------------------------------------------------------/#
        lb_lname = Label(self.window,text="Lastname                                                     ",font=("Arial",11)).grid(row=4,column=0)
        self.ent_lname = Entry(self.window,width=35)
        self.ent_lname.grid(row=5,column=0)
        #/-------------------------------------------------------------------------------------------------------------------------------------/#
        #/- Email Widgets ------------------------------------------------------------------------------------------------------------------------/#
        lb_email = Label(self.window,text="E-mail                                                          ",font=("Arial",11)).grid(row=6,column=0)
        self.ent_email = Entry(self.window,width=35)
        self.ent_email.grid(row=7,column=0)
        #/----------------------------------------------------------------------------------------------------------------------------------------/#
        #/- Phone Widgets -----------------------------------------------------------------------------------------------------------------------/#
        lb_phone = Label(self.window,text="Phone                                                          ",font=("Arial",11)).grid(row=8,column=0)
        self.ent_phone = Entry(self.window,width=35)
        self.ent_phone.grid(row=9,column=0)
        #/- Job Role Widgets ----------------------------------------------------------------------------------------------------------------------/#
        lb_jobrole = Label(self.window,text="Job Role                                                      ",font=("Arial",11)).grid(row=10,column=0)
        self.ent_jobrole = Entry(self.window,width=35)
        self.ent_jobrole.grid(row=11,column=0)
        #/-----------------------------------------------------------------------------------------------------------------------------------------/#
        #/- Salary ---------------------------------------------------------------------------------------------------------------------------------/#
        lb_salary = Label(self.window,text="Salary                                                          ",font=("Arial",11)).grid(row=12,column=0)
        self.ent_salary = Entry(self.window,width=35)
        self.ent_salary.grid(row=13,column=0)
        #/------------------------------------------------------------------------------------------------------------------------------------------/#
        #/-Buttons ---------------------------------------------------------------------------------------------------------------------------------/#
        bt_search = Button(self.window,text="Search",font=("Arial",11),command=self.search).grid(row=14,column=0,sticky=W,padx=5,pady=10)
        bt_new = Button(self.window,text="New",font=("Arial",11),command=self.new).grid(row=14,column=0,stick=W,padx=79)
        bt_update = Button(self.window,text="Update",font=("Arial",11),command=self.update).grid(row=14,column=0,stick=E,padx=75)
        bt_delete = Button(self.window,text="Delete",font=("Arial",11),command=self.delete).grid(row=14,column=0,stick=E,padx=5)
        #/------------------------------------------------------------------------------------------------------------------------------------------/#
        #/- Listbox ------------------------------------------------------------------------/#
        self.listbox = Listbox(self.window,width=40,bd=3,bg="#E6E6E6",font=("Arial Black",12),fg="green")
        self.listbox.grid(row=0,column=1,rowspan=15,sticky=N+S)
        #/----------------------------------------------------------------------------------/#
        #/- MenuBar -------------------------------------------------------------------/#
        menubar = Menu(self.window)
        menubar.add_command(label="Reset-Database",command=lambda:self.resetdatabase())
        menubar.add_command(label="Backup",command=lambda:self.backupdatabase())
        menubar.add_command(label="Help",command=lambda:self.help())
        menubar["fg"] = "green"
        self.window.config(menu=menubar)
        #/-----------------------------------------------------------------------------/#
    #/- Search -----------------------------------------/#
    def search(self):
        try:
            self.get_code = self.ent_code.get()
            self.listbox.delete(0, "end")
            self.search_fname()
            self.search_lname()
            self.search_email()
            self.search_phone()
            self.search_jobrole()
            self.search_salary()
        except Exception as error_search:
            messagebox.showwarning("Warning",error_search)
    #/--------------------------------------------------/#
    #/- Search Fname -----------------------------------------/#
    def search_fname(self):
        try:
            cursor.execute("""
                SELECT fname FROM users
                WHERE id=?;
            """, (self.get_code))
            sfname = cursor.fetchone()
            self.listbox.insert(1, sfname)
            connect.commit()
        except Exception as error_search_fname:
            messagebox.showwarning("Warning",error_search_fname)
    #/--------------------------------------------------------/#
    #/- Search Lname -----------------------------------------/#
    def search_lname(self):
        try:
            cursor.execute("""
                SELECT lname FROM users
                WHERE id=?;
            """, (self.get_code))
            lfname = cursor.fetchone()
            self.listbox.insert(1, lfname)
            connect.commit()
        except Exception as error_search_lname:
            messagebox.showwarning("Warning",error_search_lname)
    #/--------------------------------------------------------/#
    #/- Search E-mail -----------------------------------------/#
    def search_email(self):
        try:
            cursor.execute("""
                SELECT email FROM users
                WHERE id=?;
            """, (self.get_code))
            semail = cursor.fetchone()
            self.listbox.insert(2, semail)
            connect.commit()
        except Exception as error_search_email:
            messagebox.showwarning("Warning",error_search_email)
    #/--------------------------------------------------------/#
    #/- Search Phone -----------------------------------------/#
    def search_phone(self):
        try:
            cursor.execute("""
                SELECT phone FROM users
                WHERE id=?;
            """, (self.get_code))
            sphone = cursor.fetchone()
            self.listbox.insert(3, sphone)
            connect.commit()
        except Exception as error_search_phone:
            messagebox.showwarning("Warning",error_search_phone)
    #/--------------------------------------------------------/#
    #/- Search JobRole -------------------------------------/#
    def search_jobrole(self):
        try:
            cursor.execute("""
                SELECT jobrole FROM users
                WHERE id=?;
            """, (self.get_code))
            sjobrole = cursor.fetchone()
            self.listbox.insert(4, sjobrole)
            connect.commit()
        except Exception as error_search_job:
            messagebox.showwarning("Warning",error_search_job)
    #/------------------------------------------------------/#
    #/- Search Salary ------------------------------------------/#
    def search_salary(self):
        try:
            cursor.execute("""
                SELECT salary FROM users
                WHERE id=?;
            """, (self.get_code))
            ssalary = cursor.fetchone()
            self.listbox.insert(5, ssalary)
            connect.commit()
        except Exception as error_search_salary:
            messagebox.showwarning("Warning",error_search_salary)
    #/---------------------------------------------------------/#
    #/- New -----------------------------------------------------------------/#
    def new(self):
        try:
            gfname = self.ent_fname.get()
            glname = self.ent_lname.get()
            gemail = self.ent_email.get()
            gphone = self.ent_phone.get()
            gjobrole = self.ent_jobrole.get()
            gsalary = self.ent_salary.get()
            cursor.execute("""
                INSERT INTO users(fname, lname, email, phone, jobrole, salary)
                VALUES(?,?,?,?,?,?);
            """, (gfname,glname,gemail,gphone,gjobrole,gsalary))
            connect.commit()
        except Exception as error_new:
            messagebox.showwarning("Warning",error_new)
    #/-----------------------------------------------------------------------/#
    #/- Update ------------------------------------------------------------------------------------------------/#
    def update(self):
        try:
            gid = self.ent_code.get()
            gfname = self.ent_fname.get()
            glname = self.ent_lname.get()
            gemail = self.ent_email.get()
            gphone = self.ent_phone.get()
            gjobrole = self.ent_jobrole.get()
            gsalary = self.ent_salary.get()
            cursor.execute("""
                UPDATE users SET fname = ?, lname = ?, email = ?, phone = ?, jobrole = ?, salary = ? WHERE id = ?
            """, (gfname,glname,gemail,gphone,gjobrole,gsalary,gid))
            connect.commit()
        except Exception as error_update:
            messagebox.showwarning("Warning",error_update)
    #/---------------------------------------------------------------------------------------------------------/#]
    #/- Delete -----------------------------------------/#
    def delete(self):
        try:
            cursor.execute("""
                DELETE FROM users
                WHERE id = ?
            """, (self.ent_code.get()))
            connect.commit()
        except Exception as error_delete:
            messagebox.showwarning("Warning",error_delete)
    #/--------------------------------------------------/#
    #/- Reset DB -----------------------------------/#
    def resetdatabase(self):
        system("rm -rf /home/{}/bank.db".format(user))
        exit()
    #/----------------------------------------------/#
    #/- Backup DB -----------------------------/#
    def backupdatabase(self):
        with open("bank_backup.sql","w") as file:
            for line in connect.iterdump():
                file.write("{}\n".format(line))
    #/-----------------------------------------/#
    def help(self):
        messagebox.showinfo("Help","Access: https://www.github.com/VitorSilvaAlvesLucas/PyCrudJob-v1.0/")
    #/- Exit X ----------------------------------------/#
    def exitx(self):
        try:
            connect.close()
            exit()
        except Exception as error_exitx:
            messagebox.showwarning("Warning",error_exitx)
    #/-------------------------------------------------/#
#/-------------------------------------------------------------------------------------------------------------------------------/#
#/- Instances -------------------------------------/#
try:
    instance_tk = Tk()
    Root(instance_tk)
    instance_tk.title("PyCrudJob")
    instance_tk.geometry("+100+100")
    instance_tk.resizable(FALSE, FALSE)
    instance_tk.mainloop()
except Exception as error_instances:
    messagebox.showwarning("Warning",error_instances)
#/-------------------------------------------------/#
