from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import themed as tk
import sqlite3

#Databasse
conn = sqlite3.connect('enrollment_database.db')

#cursor
c = conn.cursor()

Campus_data = [
					('Adelaide Campus','Wakefield st. Adelaide','Australia'),
					('Sydney Campus','Mountain st. Sydney','Australia')
				]

Director_data = [
					('Ervin Gonzales','0449112424'),
					('Md Rakibul Islam','0449272424'),
					('Gurpreet Singh Aulakh','0449116824')
				]

Officer_data = [
					('Meg Hernandez','0415628916'),
					('Mia Deborja','0418358916'),
					('Yasmin Geronimo','0413628266'),
					('Toni Sarcida','0411428916'),
					('Noelle Espiritu','0415148916')
				]

Course_data = [
					("Master's of Information Systems",'Wakefield Building'),
					("Master's of Professional Accousys_confignting",'Wakefield Building'),
					('Global Project Management','Ultimo Building'),
					("Bachelor's Sports Management",'Ultimo Building')
				]

Class_data = [
					('G1','Systems Analysis and Design',"Monday 8:00am - 11:00am",'40'),
					('G2','Cybersecurity',"Teusday 11:00am - 2:00pm",'40'),
					('G3','Foundation of Information Systems',"Wednesday 2:00pm - 5:00pm",'40'),
					('M7','Database Modelling and Design',"Thursday 5:00pm - 8:00pm",'40'),
					('M8','Taxation and Income Accounting',"Friday 6:00pm - 9:00pm",'40'),
					('M9','Corporate Accounting',"Monday 8:00am - 11:00am",'40'),
					('M10','Sole Proprietorship and Partnerships',"Thursday11:00am - 2:00pm",'40'),
					('M11','Project Execution and Control',"Teusday 11:00am - 2:00pm",'40'),
					('M12','Coaching and Training',"Friday 6:00pm - 9:00pm",'40'),
					('M13','Team Building and Management',"Wednesday 2:00pm - 5:00pm",'40'),
					('M14','Systems Analysis and Design',"Monday 8:00am - 11:00am",'40'),
					('M15','Cybersecurity',"Teusday 11:00am - 2:00pm",'40'),
					('M16','Foundation of Information Systems',"Wednesday 2:00pm - 5:00pm",'40'),
					('A1','Database Modelling and Design',"Thursday 5:00pm - 8:00pm",'40'),
					('A2','Taxation and Income Accounting',"Friday 6:00pm - 9:00pm",'40'),
					('A3','Corporate Accounting',"Monday 8:00am - 11:00am",'40'),
					('A4','Sole Proprietorship and Partnerships',"Thursday11:00am - 2:00pm",'40'),
					('A5','Project Execution and Control',"Teusday 11:00am - 2:00pm",'40'),
					('A6','Coaching and Training',"Friday 6:00pm - 9:00pm",'40'),
					('A7','Team Building and Management',"Wednesday 2:00pm - 5:00pm",'40'),
				]

Student_data = [
					('Dias Yasmin','Password','0449128919','dias.yasmin@gmail.com','Sydney,Paramatta'),
					('Nicole Flores','123456','0412465091','nicoleflores@hotmail.com','Manila,Philippines'),
					('Annie Espiritu','password','0489451623','annie_espiritu@yahoo.com','Melbourne,Victoria'),
					('Jacob Torres','password','0489413512','JacobTorres@gmail.com','Chicago,USA'),
					('Andrew Munar','password','0489451262','andrew.munar@gmail.com','Manila,Philippines'),
					('Wilfrid Sanluis','password','0489153162','wilfrid.sanluis@hotmail.com','Manila,Philippines'),
					('Matthew Bitalac','password','0489575623','matthew_bitalac@yahoo.com','New York, USA'),
					('John Sanluis','password','0489451315','john.sanluis@gmail.com','Perth,Western Australia'),
					('Stephanie Infante','password','0414151153','stephanie_infante@gmail.com','Manila,Philippines'),
					('Triston Adamson','password','0488698031','Triston_adam@yahoo.com','Manila,Philippines'),
					('Moen Roldan','password','0486236723','Rolda.moen@gmail.com','Adelaide,South Australia'),
					('Christian Quintero','password','0481415703','QuinteroCC@hotmail.com','Brisbane,Queensland'),
					('Tenebris Martel','password','0489252625','DarknessMartel@gmail.com','Adelaide,South Australia'),
					('Aldwyn Gonzales','password','0425891957','aldwyn.jan.gonzales@yahoo.com','Manila,Philippines'),
					('Alyssa Asumpsion','password','0413589185','AlyA@hotmail.com','Sydney,Paramatta')
				]


#Database commands
c.execute("""CREATE TABLE Campus (
    Campus_name varchar(30) not null, 
    Campus_address varchar(30) not null,
    Campus_country varchar(30) not null
    )""")

c.executemany("""INSERT INTO Campus values(?,?,?)""", Campus_data)

c.execute("""CREATE TABLE Program_Director (
    Director_name varchar(30) not null,
    Director_contact int not null
    )""")

c.executemany(""" INSERT INTO Program_Director values(?,?)""", Director_data)

c.execute("""CREATE TABLE Student_Enrolment_Officer (
    Officer_name varchar(30) not null,
    Officer_contact int not null
    )""")

c.executemany("""INSERT INTO Student_Enrolment_Officer values(?,?)""", Officer_data)
    

c.execute("""CREATE TABLE Course (
    Course_name varchar(60) not null,
    Course_building varchar(30) not null
    )""")

c.executemany("""INSERT INTO Course values(?,?)""", Course_data)


c.execute("""CREATE TABLE Class (
    Class_room varchar(30) not null,
    Class_subject char(100) not null,
    Class_time varchar(200) not null,
    Class_slot int(3)
    )""")

c.executemany("""INSERT INTO Class values(?,?,?,?)""", Class_data)

c.execute("""CREATE TABLE Student (
    Student_name varchar(30) not null,
    Student_pass varchar(16) not null,
    Student_contact integer not null,
    Student_email varchar(60) not null,
    Student_address varchar(100) not null
    )""")

c.executemany("""INSERT INTO Student values(?,?,?,?,?)""", Student_data)




#commit changes
conn.commit()


#Button Commands

class Enrollee:

	def __init__ (self):
		#Login Widget
		self.widget = tk.ThemedTK()
		self.widget.get_themes()
		self.widget.set_theme("radiance")
		self.widget.title('ABC University')
		self.widget.iconbitmap('C:/Users/MaryAnn/Desktop/Projects/Student Enrolment System/abc.ico')

		self.Portal = ttk.Frame(self.widget,padx=50 ,pady=50)
		self.Name = ttk.Label(self.Portal, text="Online Student Enrollment System")
		self.Studid = ttk.Entry(self.Portal)
		self.Studpass = ttk.Entry(self.Portal, show="*")
		self.Portal.grid(row=0, column=0,padx=10 ,pady=10)
		self.Name.grid(row=0, column=0)
		self.Studid.grid(row=2, column=0)
		self.Studid.insert(0,"Student ID")
		self.Studpass.grid(row=4, column=0)
		self.Studpass.insert(1,"Password")

		self.Loginbutton = ttk.Button(self.Portal,text="Login",command=self.login)
		newstudent = Freshman()
		self.Regbutton = ttk.Button(self.Portal,text="Register",command=newstudent.register)
		self.Forgotpass = ttk.Button(self.Portal,text="Forgot Password",command=self.forgot)
		self.Loginbutton.grid(row=5, column=0)
		self.Regbutton.grid(row=6, column=0)
		self.Forgotpass.grid(row=7, column=0)

		#Login Temporary Credentials
		self.Stuid = str("Student ID")
		self.Stupass = str("Password")
	

	def login(self):
		if self.Studid.get() == self.Stuid and self.Studpass.get() == self.Stupass:
			self.Welcome = Label(self.Portal, text="Welcome!").grid(row=9, column=0)
			self.Studid.delete(0, END)
			self.Studpass.delete(0, END)
			#New window subject selection
			success = Process()
			success.selection()

	def forgot(self):
		self.response = messagebox.askokcancel("Password Recovery", "Please enter your contact details to recover your password")
		#New window password recovery
		if self.response == 1:
			self.recovery = Toplevel()
			self.recovery.title("Password Recovery")
			self.recovery.iconbitmap('C:/Users/MaryAnn/Desktop/Projects/Student Enrolment System/abc.ico')
			self.detailsform = LabelFrame(self.recovery,padx=40,pady=40)
			self.detailsform.grid(row=0,column=0,padx=25,pady=25)
			self.detailformheader = Label(self.detailsform, text="Student Contact Details Form")
			self.recoveryemail = Entry(self.detailsform)
			self.recoverycontact = Entry(self.detailsform)
			self.detailformheader.grid(row=0, column=0)
			self.recoveryemail.insert(0,"Student Email")
			self.recoveryemail.grid(row=8, column=0)
			self.recoverycontact.insert(0,"Contact Number")
			self.recoverycontact.grid(row=10, column=0)
			self.Confirmationbutton = Button(self.detailsform, text="Confirm Details")
			self.Confirmationbutton.grid(row=14, column=0,pady=10)

		#New window subject selection

class Process:

	def __init__(self):
		pass

	def selection(self):
		self.subselect = Toplevel()
		self.subselect.title("Subject Selection")
		self.subselect.iconbitmap('C:/Users/MaryAnn/Desktop/Projects/Student Enrolment System/abc.ico')
		self.mainframe = LabelFrame(self.subselect,padx=10,pady=10)
		self.subframe = LabelFrame(self.mainframe,padx=20,pady=50)
		self.cartframe = LabelFrame(self.mainframe,padx=20, pady=50)
		#subject selectionn display grid
		self.mainframe.grid(row=0,column=0,padx=5,pady=5)
		self.subframe.grid(row=0, column=0,padx=10,pady=10)
		self.cartframe.grid(row=0, column=1, padx=10,pady=10)
		self.Name1 = Label(self.subframe, text="Available Subjects")
		self.Name1.grid(row=1, column=0)
		self.Name2 = Label(self.cartframe, text ="Selected Subject")
		self.Name2.grid(row=1, column=0)
		self.subject_cost = Label(self.cartframe, text="3200 AUD per unit")
		self.subject_cost.grid(row=3, column=0)
		
		#Database commands
		self.conn = sqlite3.connect('enrollment_database.db')
		#cursor
		self.c = conn.cursor()

		#Subject List box
		self.c.execute("""SELECT Class_room, Class_subject, Class_time FROM Class""")
		self.schedules = self.c.fetchall()
		self.subject_list = Listbox(self.subframe, width=70, height=20)
		self.subject_list.grid(row=2, column=0,padx=10, pady=10)
		for self.schedule in self.schedules:
			self.subject_list.insert(END, self.schedule)

		#self.added = Label(self.cartframe, text='')
		self.cart = []
		self.cart_list = Listbox(self.cartframe, width=70, height=20)
		self.cart_list.grid(row=2,column=0,padx=10,pady=10)
		
		#Add selection to cart button
		self.addsubjectbutton = Button(self.subframe, text="Add", command=self.add)
		self.addsubjectbutton.grid(row=6, column=0, padx=5,pady=5)
		#Remove selection from cart button
		self.removesubjectbutton = Button(self.cartframe, text="Remove", command=self.remove)
		self.removesubjectbutton.grid(row=6, column=0, padx=5,pady=5)
		#Complete subject selection button
		self.enrollbutton = Button(self.subframe,text="Complete Enrollment",command=self.payment)
		self.enrollbutton.grid(row=7, column=0, padx=10,pady=10)
		#clear selection button
		self.clearselect = Button(self.cartframe,text="Clear All Selections", command=self.clear)
		self.clearselect.grid(row=7,column=0, padx=5,pady=5)

	def add(self):
		self.cart.append(self.subject_list.get(ANCHOR))
		for self.item in self.cart:
			self.cart_list.insert(END, self.item)
		self.cart.pop(0)

	def remove(self):
		self.cart_list.delete(ANCHOR)
		

	def clear(self):
		self.clearresp = messagebox.askokcancel("Student Enrollment System", "Clear selected Subjects?")
		if self.clearresp == 1:
			self.cart_list.delete(0, END)
			self.cart.clear()

	def payment(self):
		self.paysection = Toplevel()
		self.paysection.title("Tuition Fee Payment")
		self.paysection.iconbitmap('C:/Users/MaryAnn/Desktop/Projects/Student Enrolment System/abc.ico')
		self.mainpay = LabelFrame(self.paysection,padx=10,pady=10)
		self.mainpay.grid(row=0,column=0,padx=5,pady=5)
		self.Accountinfo = Label(self.mainpay, text="Account Details")
		self.BSBno = Entry(self.mainpay,width=50)
		self.Accountno = Entry(self.mainpay,width=50)
		self.Amount = Entry(self.mainpay,width=50)
		self.Accountinfo.grid(row=0, column=0,padx=5,pady=5)
		self.BSBno.insert(0,"BSB")
		self.BSBno.grid(row=8, column=0,padx=5,pady=5)
		self.Accountno.insert(0,"Account Number")
		self.Accountno.grid(row=10, column=0,padx=5,pady=5)
		self.Amount.insert(0,"Amount")
		self.Amount.grid(row=12, column=0,padx=5,pady=5)
		self.Confirmation = Button(self.mainpay, text="Confirm Details", command=self.confirmed)
		self.Confirmation.grid(row=14, column=0,padx=5,pady=5)
		self.subselect.destroy()

	def confirmed(self):
		self.paid = messagebox.askokcancel("Payment Authentication", "Payment had been confirmed")
		self.paysection.destroy()

class Freshman:
	def __init__(self):
		pass

	def register(self):
		#New window registration form
		self.reg = Toplevel()
		self.reg.title("New Student Registration")
		self.reg.iconbitmap('C:/Users/MaryAnn/Desktop/Projects/Student Enrolment System/abc.ico')
		self.mainframe = LabelFrame(self.reg,padx=10,pady=10)
		self.personalinfro = LabelFrame(self.mainframe,padx=20,pady=50)
		#Completion Button
		self.compbutton = Button(self.mainframe,text="Complete Registration",command=self.submit)
		self.compbutton.grid(row=5, column=0)
		#Registration Display
		self.mainframe.grid(row=0,column=0,padx=5,pady=5)
		self.personalinfro.grid(row=0, column=0,padx=10,pady=10)
		#Personal information entries
		self.Studinfo = Label(self.personalinfro, text="Student Information",width=50)
		self.StudName = Entry(self.personalinfro,width=50)
		self.Studpass = Entry(self.personalinfro, show="*",width=50)
		self.Studcont = Entry(self.personalinfro,width=50)
		self.Studem = Entry(self.personalinfro,width=50)
		self.Studad = Entry(self.personalinfro,width=50)
		self.Studinfo.grid(row=0, column=0,padx=5,pady=5)
		self.StudName.insert(0,"Full Name")
		self.StudName.grid(row=2, column=0,padx=5,pady=5)
		self.Studpass.insert(0,"Password")
		self.Studpass.grid(row=4, column=0,padx=5,pady=5)
		self.Studcont.insert(0,"Contact Number")
		self.Studcont.grid(row=6, column=0,padx=5,pady=5)
		self.Studem.insert(0,"Email")
		self.Studem.grid(row=8, column=0,padx=5,pady=5)
		self.Studad.insert(0,"Postal Address")
		self.Studad.grid(row=10, column=0)

	def submit(self):
		#Database
		self.conn = sqlite3.connect('enrollment_database.db')
		#cursor
		self.c = conn.cursor()
		#Insert commands
		self.c.execute("INSERT INTO Student VALUES (:StudName, :Studpass, :Studcont, :Studem, :Studad)",
			{
				'StudName': self.StudName.get(),
				'Studpass': self.Studpass.get(),
				'Studcont': self.Studcont.get(),
				'Studem': self.Studem.get(),
				'Studad': self.Studad.get()
			})

		#commit changes
		self.conn.commit()
		#close db connection 
		self.conn.close()

		#Delete entries
		self.StudName.delete(0, END)
		self.Studpass.delete(0, END)
		self.Studcont.delete(0, END)
		self.Studem.delete(0, END)
		self.Studad.delete(0, END)
		self.reg.destroy()
		complete = Process()
		complete.selection()
		
gui = Enrollee()
gui.widget.mainloop()


