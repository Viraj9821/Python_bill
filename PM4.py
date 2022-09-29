from tkinter import *
import base64
from PIL import ImageTk
from tkinter.messagebox import *
from tkinter import messagebox
from getpass import *
from sqlite3 import * 
from tkinter.scrolledtext import *

import os
from datetime import *
from tkinter import ttk
#from pic2str import explode
from PIL import Image,ImageTk
from tkcalendar import Calendar
#import calendar


#-----------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------------
def f5():
	signup_window.withdraw()
	root.deiconify()
def g1():
	n = 0
	#Generate Button All Inputs taken
	#The reason you are getting this error is that you are trying to convert a space character to an integer, which is totally impossible and restricted.And that's why you are getting this error.
	while n < 1:
		if len(Quantity.get()) == 0 or len(Price.get()) == 0 or len(Quantity1.get()) == 0 or len(Price1.get()) == 0 or len(Quantity2.get()) == 0 or len(Price2.get()) == 0 or len(Quantity3.get()) == 0 or len(Price3.get()) == 0 or len(Quantity4.get()) == 0 or len(Price4.get()) == 0:
			showerror('Invalid','Fill Each box')
			
			newbill_window.focus()
		else:
		
			combo0 = combo_box1.get()
			quant0 = int(float(Quantity.get()))
			price0 = int(float(Price.get()))
			print(combo0,quant0,price0)
	

			combo1 = combo_box2.get()
			quant1 = int(float(Quantity1.get()))
			price1 = int(float(Price1.get()))
			print(combo1,quant1,price1)

			combo2 = combo_box3.get()
			quant2 = int(float(Quantity2.get()))
			price2 = int(float(Price2.get()))
			print(combo2,quant2,price2)

			combo3 = combo_box4.get()
			quant3 = int(float(Quantity3.get()))
			price3 =int(float(Price3.get()))
			print(combo3,quant3,price3)

			combo4 = combo_box3.get()
			quant4 = int(float(Quantity4.get()))
			price4 = int(float(Price4.get()))
			print(combo4,quant4,price4)

			Sgst = Label(Frame_login2,text="SGST 18 %", font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=630,y=650)
			Cgst = Label(Frame_login2,text="CGST 18 %", font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=630,y=750)
	
			total0 = quant0 *  price0 
			total1 = quant1 *  price1 
			total2 = quant2 *  price2
			total3 = quant3 *  price3 
			total4 = quant4 *  price4
			Total = total0 + total1 + total2 + total3 + total4
			sgst = Total * 18 / 100
			cgst = Total * 18 / 100
	
	
			Total = Label(Frame_login2,text=total0, font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=850,y=240)
			Total1 = Label(Frame_login2,text=total1, font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=850,y=310)
			Total2 = Label(Frame_login2,text=total2, font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=850,y=380)
			Total3 = Label(Frame_login2,text=total3, font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=850,y=440)
			Total4 = Label(Frame_login2,text=total4, font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=850,y=510)

	
			Sgst = Label(Frame_login2,text=sgst, font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=830,y=650)
			Cgst = Label(Frame_login2,text=cgst, font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=830,y=750)
			n = n + 1
def f6():
	#Invoice Page
	signup_window.deiconify()
	newbill_window.withdraw()
	#combo_box.set("Search")
	Quantity.delete(0,END)
	#Total.delete(0,END)
	Price.delete(0,END)

	Quantity1.delete(0,END)
	Total1.delete(0,END)
	Price1.delete(0,END)
	Quantity2.delete(0,END)
	Total2.delete(0,END)
	Price2.delete(0,END)

#---------------------------------------------------------------------------------------------------------------------------------------------
				#OTP

def f19():
	
	root.withdraw()			
	otp.deiconify()

#---------------------------------------------------------------------------------------------------------------------------------------------
			#register dont have as account

def f21():
	root.withdraw()			
	register.deiconify()

#---------------------------------------------------------------------------------------------------------------------------------------------
			#Admin Control Button

def Admin_f1() :
	
	Admin_Login.deiconify()	
	signup_window.withdraw()	

#---------------------------------------------------------------------------------------------------------------------------------------------	

def f1():
	#Quantity.delete(0,END)
	

	con = None
	try:
		con = connect("entries1.db")
		print("database created / open ")
		cursor = con.cursor()
		
		
		r1 = txt_usr.get()
		r2 = txt_pass.get()
		query = f"SELECT email from users WHERE email='{r1}' AND pass = '{r2}';"
		cursor.execute(query)
		if cursor.fetchone():  # An empty result evaluates to False.
    		
		
			print("Success")
			txt_usr.delete(0,END)
			txt_pass.delete(0,END)
			
			
			
			root.withdraw()			
			signup_window.deiconify()


		

		else:
			print("Failure")
			txt_usr.delete(0,END)
			txt_pass.delete(0,END)
	except Exception as e:
		print("issue :",e)

	finally:
		if con is not None:
			con.close()
			print("closed")


def f3():		

	signup_window.withdraw()				
	newbill_window.deiconify()

def ff1():
	'''root.withdraw()			
	signup_window.deiconify()'''	
	try:
		con = connect("entries1.db")
		print("database created / open ")
		cursor = con.cursor()
		sql = "create table if not exists users (firstname text, lastname text, email text primary key,gender text, contact int, DOB text, prev text, pass text )"
		cursor.execute(sql)
		print("table created ")
		sql1 = "select * from users where  email ='Admin' "
		cursor.execute(sql1)
		data = cursor.fetchall()
		print(data)
		info1=""
		
		for d in data:
			#info1 = info1 + "email1 = " + str(d[2])+"\n\n"
			
			info1 =  str(d[2])
		print(info1)
		r21 = "Admin"
		if info1 == r21 :
			showinfo('sucess','Default User Exists!')
			
		else:
			e33 = "Admin"	
			p33 = "123456"
			p44 = "Admin"
			cursor.execute("""INSERT INTO users(email, prev, pass)VALUES (?,?,?)""", (e33, p44, p33))
			con.commit()
			showinfo('Sucess','Default User Created!\n Username:Admin\nPassword:123456')
			
			
		
			

	except Exception as e:
		showerror('failure',e)
		print("Error")

	finally:
		if con is not None:
			con.close()
			print("closed")		
		
#------------------------------------------------------------------------------------------------------------------------------------------
def f2():
	print("B")
root = Tk()
root.title("Login System")
root.geometry("1199x600+250+150")
root.resizable(False,False)
root.focus()
root.configure(bg='grey') 


				# frame Login 


Frame_login = Frame(root,bg="white")
Frame_login.place(x=150,y=150,height=340,width=500)
#myButton.place(relx=0.2, rely=0.2, relwidth=0.4, relheight=0.7)
title = Label(Frame_login,text="Login Here", font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=70,y=30)
		
desc = Label(Frame_login,text="Admin Login Area ", font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

name = Button(root,text="Developed by Viraj Mhatre",command=ff1,font=("times new roman",13,"bold"),bg="grey",fg="black").place(x=980,y=560)		

lbl_usr = Label(Frame_login,text="Username", font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
txt_usr = Entry(Frame_login,font=("times new roman",15),bg="lightgray")
txt_usr.place(x=90,y=170,width=350,height=35)
#txt_usr.focus()
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
lbl_pass = Label(Frame_login,text="Password", font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
txt_pass = Entry(Frame_login,font=("times new roman",15),bg="lightgray",show="*")
txt_pass.place(x=90,y=240,width=350,height=35)

#forget = Button(Frame_login,text="Forget Password?",command=f19,bg="white",bd=0,fg="#d77337",font=("times new roman",12)).place(x=90,y=280)
forget = Button(Frame_login,text="Forget Password?",command=f19,bg="white",bd=0,fg="#d77337",font=("times new roman",12)).place(x=320,y=280)
#signup= Button(Frame_login,text="Don't have a account?Sign up",command=f21,bg="white",bd=0,fg="#d77337",font=("times new roman",12)).place(x=290,y=280)
Login_btn = Button(root,command = f1,cursor="hand2",text="Login",bg="#d77337",fg="white",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------	
			#Animation
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)
############# Main program ###############

canvas=Canvas(root,bg="white")

canvas.pack(fill=BOTH, expand=1)
canvas.place(x=1,y=1,width=1200)
text_var="Hello, Click on #Developed by Viraj Mhatre# to Register as Default Admin !!!!"
text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',20,'bold'),fill='black',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = x2-x1
height = y2-y1
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()


#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
	#signup Menu

signup_window=Toplevel(root)
signup_window.title("S.M.S.")

signup_window.geometry("1199x600+250+150")
signup_window.resizable(False,False)

#signup_window.configure(background="light grey")
signup_window.configure(bg='grey') 

signup_window.withdraw()

Frame_signup = Frame(signup_window,bg="white")
Frame_signup.place(x=350,y=50,height=500,width=500)
title = Label(Frame_signup,text="Welcome", font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=170,y=30)

New_btn = Button(Frame_signup,command = f3,cursor="hand2",text="Generate New Invoice",bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=140,width=260,height=40)

View_btn = Button(Frame_signup,command = f1,cursor="hand2",text="View Older Invoice",bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=200,width=260,height=40)
			
Ba_btn = Button(Frame_signup,command = f1,cursor="hand2",text="Business Analysis",bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=260,width=260,height=40)

Admin_btn = Button(Frame_signup,command = Admin_f1,cursor="hand2",text="Admin Control",bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=320,width=260,height=40)
		
NA1_btn = Button(Frame_signup,command = f1,cursor="hand2",text="NA1",bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=380,width=260,height=40)

Logout_btn = Button(signup_window,command = f5,cursor="hand2",text="Logout",bg="#d77337",fg="white",font=("times new roman",20)).place(x=510,y=530,width=160,height=40)
			
			
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
				#Generate New

		
newbill_window=Toplevel(root)
newbill_window.title("Invoice Page")
newbill_window.geometry("1535x1000+150+1")
newbill_window.resizable(False,False)
#newbill_window.configure(background="light grey")
newbill_window.configure(bg='grey')

Frame_login2 = Frame(newbill_window,bg="white")
Frame_login2.place(x=170,y=5,height=980,width=1200)
Back_Gen = Button(newbill_window,text="Back",bg="#d77337",fg="white",command=f6,font=("times new roman",20)).place(x=0,y=300,width=170,height=40)
Exit_Gen =Button(newbill_window,text="Exit",bg="#d77337",fg="white",font=("times new roman",20)).place(x=0,y=400,width=170,height=40)
Add_Gen =Button(newbill_window,text="Add",bg="#d77337",fg="white",font=("times new roman",20)).place(x=0,y=500,width=170,height=40)
Rem_Gen =Button(newbill_window,text="Remove",bg="#d77337",fg="white",font=("times new roman",20)).place(x=0,y=600,width=170,height=40)
Generate = Button(newbill_window,text="Generate",bg="#d77337",fg="white",command=g1,font=("times new roman",20)).place(x=650,y=960,width=170,height=40)
#myButton.place(relx=0.2, rely=0.2, relwidth=0.4, relheight=0.7)
Clear_Gen = Button(newbill_window,text="Preview",bg="#d77337",fg="white",command=f6,font=("times new roman",20)).place(x=1370,y=300,width=162,height=40)
Preview_Gen =Button(newbill_window,text="Help",bg="#d77337",fg="white",font=("times new roman",20)).place(x=1370,y=400,width=162,height=40)
Help_Gen =Button(newbill_window,text="Clear",bg="#d77337",fg="white",font=("times new roman",20)).place(x=1370,y=500,width=162,height=40)
View_Gen =Button(newbill_window,text="View",bg="#d77337",fg="white",font=("times new roman",20)).place(x=1370,y=600,width=162,height=40)
title = Label(Frame_login2,text="Invoice ", font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=500,y=5)
date = Label(Frame_login2,text="Date :",font=("Impact",15,"bold"),fg="#d77337",bg="white").place(x=950,y=25)
Invoice = Label(Frame_login2,text="Invoice no :",font=("Impact",15,"bold"),fg="#d77337",bg="white").place(x=950,y=55)
gst = Label(Frame_login2,text="GST No :",font=("Impact",15,"bold"),fg="#d77337",bg="white").place(x=950,y=85)

Number1 = Label(Frame_login2,text="1.",font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=70,y=225)
Number2 = Label(Frame_login2,text="2.",font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=70,y=290)
Number3 = Label(Frame_login2,text="3.",font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=70,y=355)
Number4 = Label(Frame_login2,text="4.",font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=70,y=420)
Number5 = Label(Frame_login2,text="5.",font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=70,y=485)

Item_name = Label(Frame_login2,text="Item Name",font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=120,y=180)
Quantity = Label(Frame_login2,text="Quantity",font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=370,y=180)
Unit = Label(Frame_login2,text="Price Per Unit",font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=570,y=180)
Total = Label(Frame_login2,text="Total",font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=850,y=180)
da = datetime.now().date()
txt_date = Label(Frame_login2,text=da,font=("Impact",15,"bold"),fg="#d77337",bg="white").place(x=1010,y=25)


#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
				#input1
  		#Combo box

lst = ['C' , 'C++', 'Java', 
          'Python', 'Ruby', 'Sql',
          'JS', 'Html']

def search(event):
	value = event.widget.get()
	if value == ' ' :
		combo_box1['values'] = lst
	

	else:
		data = []
		for item in lst:
			if value.lower() in item.lower():
				data.append(item)
		
		combo_box1['values'] = data
	




combo_box1 = ttk.Combobox(Frame_login2,value=lst,width=20)
combo_box1.set("Search")
combo_box1.place(x=120,y=240)
combo_box1.bind(' <KeyRelease>',search)


Quantity = Entry(Frame_login2,bd=3,width=8,bg="lightgray")
Quantity.place(x=400,y=240)

Price = Entry(Frame_login2,bd=3,width=8,bg="lightgray")
Price.place(x=650,y=240)

#Total = Entry(Frame_login2,bd=3,width=8,bg="lightgray")
#Total.place(x=850,y=180)
#txt_date.config(state= DISABLED)
newbill_window.withdraw()
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
				#input2
lst = ['C' , 'C++', 'Java', 
          'Python', 'Ruby', 'Sql',
          'JS', 'Html']

def search(event):
	value = event.widget.get()
	if value == ' ' :
		combo_box2['values'] = lst
	

	else:
		data = []
		for item in lst:
			if value.lower() in item.lower():
				data.append(item)
		
		combo_box2['values'] = data
	



combo_box2 = ttk.Combobox(Frame_login2,value=lst,width=20)
combo_box2.set("Search")
combo_box2.place(x=120,y=310)
combo_box2.bind(' <KeyRelease>',search)


Quantity1 = Entry(Frame_login2,bd=3,width=8)
Quantity1.place(x=400,y=310)

Price1 = Entry(Frame_login2,bd=3,width=8)
Price1.place(x=650,y=310)

#Total1 = Entry(Frame_login2,bd=3,width=8)
#Total1.place(x=850,y=250)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
				#input3
lst = ['C' , 'C++', 'Java', 
          'Python', 'Ruby', 'Sql',
          'JS', 'Html']

def search(event):
	value = event.widget.get()
	if value == ' ' :
		combo_box3['values'] = lst
	

	else:
		data = []
		for item in lst:
			if value.lower() in item.lower():
				data.append(item)
		
		combo_box3['values'] = data
	



combo_box3 = ttk.Combobox(Frame_login2,value=lst,width=20)
combo_box3.set("Search")
combo_box3.place(x=120,y=380)
combo_box3.bind(' <KeyRelease>',search)


Quantity2 = Entry(Frame_login2,bd=3,width=8)
Quantity2.place(x=400,y=380)

Price2 = Entry(Frame_login2,bd=3,width=8)
Price2.place(x=650,y=380)

#Total2 = Entry(Frame_login2,bd=3,width=8)
#Total2.place(x=850,y=390)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
				#input4
lst = ['C' , 'C++', 'Java', 
          'Python', 'Ruby', 'Sql',
          'JS', 'Html']

def search(event):
	value = event.widget.get()
	if value == ' ' :
		combo_box4['values'] = lst
	

	else:
		data = []
		for item in lst:
			if value.lower() in item.lower():
				data.append(item)
		
		combo_box4['values'] = data
	



combo_box4 = ttk.Combobox(Frame_login2,value=lst,width=20)
combo_box4.set("Search")
combo_box4.place(x=120,y=450)
combo_box4.bind(' <KeyRelease>',search)


Quantity3 = Entry(Frame_login2,bd=3,width=8)
Quantity3.place(x=400,y=450)

Price3 = Entry(Frame_login2,bd=3,width=8)
Price3.place(x=650,y=450)

#Total3 = Entry(Frame_login2,bd=3,width=6)
#Total3.place(x=850,y=390)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
				#input5
lst = ['C' , 'C++', 'Java', 
          'Python', 'Ruby', 'Sql',
          'JS', 'Html']

def search(event):
	value = event.widget.get()
	if value == ' ' :
		combo_box5['values'] = lst
	

	else:
		data = []
		for item in lst:
			if value.lower() in item.lower():
				data.append(item)
		
		combo_box5['values'] = data
	



combo_box5 = ttk.Combobox(Frame_login2,value=lst,width=20)
combo_box5.set("Search")
combo_box5.place(x=120,y=510)
combo_box5.bind(' <KeyRelease>',search)


Quantity4 = Entry(Frame_login2,bd=3,width=8)
Quantity4.place(x=400,y=510)

Price4 = Entry(Frame_login2,bd=3,width=8)
Price4.place(x=650,y=510)

#Total4 = Entry(Frame_login2,bd=3,width=6)
#Total4.place(x=850,y=520)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
				#Admin Login Access
def AL2():
	
	Admin_Login.withdraw()
	signup_window.deiconify()
def AL1():

	
			
	#Admin_Login.withdraw()
	#Admin.deiconify()
	
	#print(t1)
	#print(t2)#
	con = None
	try:
		con = connect("entries1.db")
		print("database created / open ")
		cursor = con.cursor()
		
		
		t1 = Admin_Login_txt_usr.get()
		t2 = Admin_Login_txt_pass.get()
		query = f"SELECT email from users WHERE email='{t1}' AND pass = '{t2}' AND prev = 'Admin';"
		cursor.execute(query)
		if cursor.fetchone():  # An empty result evaluates to False.
    		
		
			print("Success")
			Admin_Login_txt_usr.delete(0,END)
			Admin_Login_txt_pass.delete(0,END)
			
			
			
			Admin_Login.withdraw()
			Admin.deiconify()


		

		else:
			showerror("Restricted","Admin Access Only")
			Admin_Login_txt_usr.delete(0,END)
			Admin_Login_txt_pass.delete(0,END)
	except Exception as e:
		print("issue :",e)

	finally:
		if con is not None:
			con.close()
			print("closed")
	
Admin_Login=Toplevel(root)
Admin_Login.title("Admin Login")
Admin_Login.geometry("1199x600+250+150")
Admin_Login.resizable(False,False)
Admin_Login.configure(bg='grey') 
Admin_Login.withdraw()
	
Frame_login5 = Frame(Admin_Login,bg="white")
Frame_login5.place(x=350,y=70,height=350,width=500)
title = Label(Frame_login5,text="Admin Login", font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=120,y=30)
#-----------------------------------------------------------------------------------------------------------------------------------------------
			#Animation

#-----------------------------------------------------------------------------------------------------------------------------------------------
Admin_Login_lbl_usr = Label(Frame_login5,text="Username", font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
Admin_Login_txt_usr = Entry(Frame_login5,font=("times new roman",15),bg="lightgray")
Admin_Login_txt_usr.place(x=90,y=170,width=350,height=35)

Admin_Login_lbl_pass = Label(Frame_login5,text="Password", font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
Admin_Login_txt_pass = Entry(Frame_login5,font=("times new roman",15),bg="lightgray",show="*")
Admin_Login_txt_pass.place(x=90,y=240,width=350,height=35)

Admin_Login_Login_btn = Button(Admin_Login,command = AL1,cursor="hand2",text="Login",bg="#d77337",fg="white",font=("times new roman",20)).place(x=435,y=400,width=160,height=40)
Admin_Login_Back_btn = Button(Admin_Login,command = AL2,cursor="hand2",text="Back",bg="#d77337",fg="white",font=("times new roman",20)).place(x=605,y=400,width=160,height=40)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
				#Admin Controls

def Af6():
	Admin.withdraw()
	Admin_Login.deiconify()	
def Af1():
	Admin.withdraw()
	register.deiconify()
def Af2():
	Admin.withdraw()
	View.deiconify()
	View_st_data.delete(1.0,END)
	info =""
	con = None
	try:
		con = connect('entries1.db')
		cursor = con.cursor()
		sql = "select * from users"
		cursor.execute(sql)	
		data = cursor.fetchall()
		




		for d in data:
			#info = info + "firstname = " + str(d[0]) + "\tlastname = " + str(d[1]) +"\t\temail =" + str(d[2])+"\n\n"
			info = info + "firstname = " + str(d[0]) + "\tlastname = " + str(d[1]) +"\t\temail =" + str(d[2])+"\t\tgender =" + str(d[3])+"\t\tcontact =" + str(d[4])+"\t\tdob =" + str(d[5])+"\t\tprev =" + str(d[6])+"\n\n"
		print(info)
		View_st_data.insert(INSERT,info) 
	except Exception as e :
		showerror("failure",e)
	finally:
		if con is not None:
			con.close()
	
def Af4():	
	Admin.withdraw()
	Delete.deiconify()


Admin=Toplevel(root)
Admin.title("Admin")
Admin.geometry("1199x600+250+150")
Admin.resizable(False,False)
Admin.configure(bg='grey') 
Admin.withdraw()
	
Frame_login5 = Frame(Admin,bg="white")
Frame_login5.place(x=350,y=50,height=500,width=500)
title = Label(Frame_login5,text="Admin Controls", font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=100,y=30)
Register_user = Button(Frame_login5,command = Af1,cursor="hand2",text="Register New User",bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=140,width=260,height=40)
View_user = Button(Frame_login5,command = Af2,cursor="hand2",text="View Existing User",bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=200,width=260,height=40)
Update_user = Button(Frame_login5,cursor="hand2",text="Update Existing User",bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=260,width=260,height=40)
Delete_user = Button(Frame_login5,cursor="hand2",command = Af4,text="Delete Existing User",bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=320,width=260,height=40)
Ba_btn1 = Button(Frame_login5,cursor="hand2",text="Business Analysis",bg="#d77337",fg="white",font=("times new roman",20)).place(x=120,y=380,width=260,height=40)


Admin_back = Button(Admin,command = Af6,cursor="hand2",text="Back",bg="#d77337",fg="white",font=("times new roman",20)).place(x=510,y=530,width=160,height=40)

#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------			
				#Delete Window

def Df2():
	Delete.withdraw()
	Admin.deiconify()	

def Df1():
	
	con = None
	try:
		con = connect("entries1.db")
	
		cursor = con.cursor()
		sql = "delete from users where  email ='%s' "
		email_get = Delete_entry.get()

		cursor.execute(sql % (email_get))
	
		if cursor.rowcount > 0:
			showinfo('sucess','record deleted')
			Delete_entry.delete(0,END)
			con.commit()
		else:
			showerror('invalid','record does not exists')
			Delete_entry.delete(0,END)
	except Exception as e:
		showerror('invalid','Please enter rno')
		con.rollback()
	finally:
		if con is not None:	
			con.close()
			print("closed")

Delete=Toplevel(root)
Delete.title("Admin")
Delete.geometry("1199x600+250+150")
Delete.resizable(False,False)
Delete.configure(bg='grey') 
Delete.withdraw()
Frame_login6 = Frame(Delete,bg="white")
Frame_login6.place(x=350,y=50,height=500,width=500)
title = Label(Frame_login6,text="Enter Email", font=("Impact",20,"bold"),fg="#d77337",bg="white").place(x=10,y=30)
Delete_entry = Entry(Frame_login6,bd=3,width=15,bg="lightgray",font=("times new roman",20))
Delete_entry.place(x=170,y=30)
Delete_user = Button(Frame_login6,cursor="hand2",command = Df1,text="Delete User",bg="#d77337",fg="white",font=("times new roman",20))
Delete_user.place(x=90,y=140,width=150,height=40)
Back_Delete_user = Button(Frame_login6,cursor="hand2",command = Df2,text="Back",bg="#d77337",fg="white",font=("times new roman",20))
Back_Delete_user.place(x=270,y=140,width=150,height=40)
#-------------------------------------------------------------------------------------------------------------------------------------------
			#dont have a account button
def f23():
	if  len(Firstname.get()) == 0:
		showerror('Invalid','Enter Firstname')
		Firstname.delete(0,END)

	elif  (not Firstname.get().isalpha()):
		showerror('Invalid','Only Alphabets')
		Firstname.delete(0,END)	

	elif  len(Lastname.get()) == 0:
		showerror('Invalid','Enter Lastname')
		Lastname.delete(0,END)

	elif ( not Lastname.get().isalpha()):
		showerror('Invalid','Only Alphabets')
		Lastname.delete(0,END)	


	
	elif len(EmailId21.get()) == 0:
		showerror('Invalid','Enter Email')
		EmailId21.delete(0,END)

	elif  (Contact.get().isalpha()):
		showerror('Invalid','Numbers Only ')
		Contact.delete(0,END)

	elif  len(Contact.get()) == 0:
		showerror('Invalid','Enter Contact')
		Contact.delete
	
	elif  len(pass11.get()) == 0:
		showerror('Invalid','Enter Password')
		pass11.delete(0,END)

	elif  len(pass13.get()) == 0:
		showerror('Invalid','Enter Password')
		pass13.delete(0,END)
	
	elif pass11.get() != pass13.get():
		showerror('Invalid','Password Mismatched')
		pass11.delete(0,END)
		pass13.delete(0,END)
		
		
	
	
	
	else:
	
		res = k.get()
		if res == 1:
			
			msg = "Male"
		else :
			
			msg = "Female"


		
		res1 = k1.get()
		if res1 == 11:
			
			msg1 = "Admin"
		else :
			
			msg1 = "User"
		print(msg1)	
	
		f = Firstname.get()
		l = Lastname.get()
		e1 = EmailId21.get()
		c = Contact.get()
		p = pass13.get()
		
		da2 = cal.get_date()
		print("Selected Date is: " + cal.get_date())

		con = None
		try:
			con = connect("entries1.db")
			print("database created / open ")
			cursor = con.cursor()
			sql = "create table if not exists users (firstname text, lastname text, email text primary key,gender text, contact int, DOB text, prev text, pass text )"
			cursor.execute(sql)
			print("table created ")
			cursor.execute("""INSERT INTO users(firstname, lastname, email, gender, contact, DOB, prev, pass)VALUES (?,?,?,?,?,?,?,?)""", (f,l,e1,msg,c,da2,msg1,p))
			con.commit()
			showinfo('Sucess','Registered Successfully!')
			con.commit()
			print ( 'Data entered successfully.' )
			Contact.delete(0,END)
			EmailId21.delete(0,END)
			Lastname.delete(0,END)
			Firstname.delete(0,END)
			pass11.delete(0,END)
			pass13.delete(0,END)
			
		except Exception as e:
			showerror('failure',e)

		finally:
			if con is not None:
				con.close()
				print("closed")

		#register.withdraw()			
		#root.deiconify()
		
		
		
		print(msg)
		print(f)
		print(l)
		print(c)
		print(e1)
		#print(msg1)


#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------			
				#View Window

def Vf1():
	View.withdraw()
	Admin.deiconify()
	




View=Toplevel(root)
View.title("View")
View.geometry("1900x1000+1+1")
View.resizable(False,False)
View.configure(bg='grey') 
View_st_data = ScrolledText(View ,width=150, height=40, font=("Arial",20,"bold"))
View_st_data.pack(pady=10)
View.withdraw()
View_back = Button(View,command = Vf1,cursor="hand2",text="Back",bg="#d77337",fg="white",font=("times new roman",20)).place(x=810,y=970,width=160,height=40)



#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------		

def f24():
	con = None
	try:
		con = connect('entries1.db')
		cursor = con.cursor()
		sql = "select * from users"
		cursor.execute(sql)
		data = cursor.fetchall()
		print(data)
	except Exception as e :
		showerror("failure",e)
	finally:
		if con is not None:
			con.close()
	register.withdraw()			
	Admin.deiconify()
	


register = Toplevel(root)
register.title("Login System")
register.geometry("1299x950+300+30")
register.resizable(False,False)
register.configure(bg='grey')	

register.withdraw()
Frame_login3 = Frame(register,bg="white")
Frame_login3.place(x=230,y=5,height=930,width=850)
Register = Label(Frame_login3,text="Register",font=("times new roman",40,"bold"),fg="#d77337",bg="white").place(x=300,y=5)

firstname = Label(Frame_login3,text="Firstname", font=("Impact",20,"bold"),fg="#d77337",bg="white").place(x=175,y=100)
Firstname = Entry(Frame_login3,bd=3,width=30,bg="lightgray",font=("times new roman",20))
Firstname.place(x=325,y=105,width=250,height=35)

lastname = Label(Frame_login3,text="Lastname", font=("Impact",20,"bold"),fg="#d77337",bg="white").place(x=175,y=180)
Lastname = Entry(Frame_login3,bd=3,width=30,bg="lightgray",font=("times new roman",20))
Lastname.place(x=325,y=185,width=250,height=35)

emailid = Label(Frame_login3,text="Email", font=("Impact",20,"bold"),fg="#d77337",bg="white").place(x=175,y=260)
EmailId21 = Entry(Frame_login3,bd=3,width=30,bg="lightgray",font=("times new roman",20))
EmailId21.place(x=325,y=265,width=250,height=35)




gender = Label(Frame_login3,text="Gender", font=("Impact",20,"bold"),fg="#d77337",bg="white").place(x=175,y=325)
k = IntVar()  #object created of IntVar
Male = Radiobutton(Frame_login3,text="Male",font=('Arial' , 20, 'bold'),variable=k , value =1)
Male.place(x=325,y=325)
Female = Radiobutton(Frame_login3,text="Female",font=('Arial' , 20, 'bold'),variable=k , value =2)
Female.place(x=425,y=325)

contact = Label(Frame_login3,text="Contact", font=("Impact",20,"bold"),fg="#d77337",bg="white").place(x=175,y=400)
Contact = Entry(Frame_login3,bd=3,width=30,bg="lightgray",font=("times new roman",20))
Contact.place(x=325,y=400,width=250,height=35)

privilege = Label(Frame_login3,text="Privilege", font=("Impact",20,"bold"),fg="#d77337",bg="white").place(x=175,y=465)
k1 = IntVar()  #object created of IntVar
Admin11 = Radiobutton(Frame_login3,text="Admin",font=('Arial' , 20, 'bold'),variable=k1 , value =11)
Admin11.place(x=325,y=465)
User11 = Radiobutton(Frame_login3,text="User",font=('Arial' , 20, 'bold'),variable=k1 , value =12)
User11.place(x=450,y=465)


pass10 = Label(Frame_login3,text="Password", font=("Impact",20,"bold"),fg="#d77337",bg="white").place(x=175,y=530)
pass11 = Entry(Frame_login3,bd=3,width=30,bg="lightgray",font=("times new roman",20),show="*")
pass11.place(x=325,y=530,width=250,height=35)


pass12 = Label(Frame_login3,text="Re-enter", font=("Impact",20,"bold"),fg="#d77337",bg="white").place(x=175,y=590)
pass13 = Entry(Frame_login3,bd=3,width=30,bg="lightgray",font=("times new roman",20),show="*")
pass13.place(x=325,y=590,width=250,height=35)


dob = Label(Frame_login3,text="D.O.B", font=("Impact",20,"bold"),fg="#d77337",bg="white").place(x=175,y=660)
cal = Calendar(Frame_login3, selectmode = 'day',year = 2020, month = 5,day = 22)
cal.place(x=325,y=660)

Register_btn=Button(register,text="Register",bg="#d77337",command=f23,fg="white",font=("times new roman",20)).place(x=450,y=910,width=162,height=40)
Back_btn=Button(register ,text="Back",bg="#d77337",fg="white",command=f24,font=("times new roman",20)).place(x=650,y=910,width=162,height=40)



#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
							#Forget Password Button




otp = Toplevel(root)
otp.title("Login System")
otp.geometry("1199x600+250+150")
otp.resizable(False,False)
otp.configure(bg='grey')	

Frame_login4 = Frame(otp,bg="white")
Frame_login4.place(x=150,y=5,height=580,width=850)
otp.withdraw()
Forget  = Label(Frame_login4,text="Forget Password ??",font=("times new roman",40,"bold"),fg="#d77337",bg="white").place(x=210,y=5)
emailid = Label(Frame_login4,text="Email", font=("Impact",20,"bold"),fg="#d77337",bg="white").place(x=175,y=225)
EmailId1 = Entry(Frame_login4,bd=3,width=30,bg="lightgray",font=("times new roman",20))
EmailId1.place(x=325,y=225,width=250,height=35)
Proceed_btn=Button(otp,text="Proceed",bg="#d77337",command=f23,fg="white",font=("times new roman",20)).place(x=380,y=560,width=162,height=40)
Back_btn=Button(otp,text="Back",bg="#d77337",fg="white",command=f24,font=("times new roman",20)).place(x=580,y=560,width=162,height=40)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
				#Terms 


#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
root.mainloop()