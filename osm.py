from tkinter import *
import random,time,ctypes
import subprocess
from PIL import Image,ImageTk

if __name__ != "__main__":
	ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
	window=Tk()
	window.title("ibOS")
	window.geometry("800x600")

	window.resizable(False,False)
	loading=Frame(window,bg="black")
	logo=PhotoImage(file="logo.png")
	bg_logo=PhotoImage(file="logo_bg.png")
	window.iconphoto(True,logo)
	txt=""
	random.seed(time.time())
	counter=0
	cont=False
	user=""
	passw=""
	with open("o","r") as f:
		lines=f.readlines()
	for i,line in enumerate(lines):
		exec(line)
	lbl=Label(
		window,
		text=txt,
		font=("Comic Sans",20,"bold"),
		fg="white",
		bg="black"
		)

	login=Frame(window,bg="#65A83E")
	def scene2():
		texti=""


		l_h=Label(login,text="Enter Your Info:",font=("Comic Sans",20,"bold"),fg="White",bg="#65A83E")
		subm=Button(login,font=("Comic Sans",30,"bold"),text="Login",bg="#467D28",fg="white",activebackground="#2B471C",activeforeground="white")
		user_label=Label(login,text="Username:",bg="#65A83E",font=("Comic Sans",20,"bold"))
		pass_label=Label(login,text="Password:",bg="#65A83E",font=("Comic Sans",20,"bold"))

		username=Entry(login,font=("Comic Sans",15))
		password=Entry(login,show="*",font=("Comic Sans",15,"bold"))

		wa=Label(login,text="",font=("Comic Sans",30,"bold"),fg="white",bg="#2B471C")
		def check_inf():
			
			global texti
			
			u_inf=username.get()
			p_inf=password.get()
			if u_inf == user and p_inf == passw:
				subm.config(state=DISABLED)
				username.config(state=DISABLED)
				password.config(state=DISABLED)
				texti="Welcome! Please wait.."
				wa.config(text=texti)
				wa.place(x=200,y=400)
				window.after(5000,scene3)
				

				
			else:
				texti="Check your login credentials!"
				wa.config(text=texti)
				wa.place(x=200,y=400)

		subm.config(command=check_inf)
		window.after(2000)
		loading.destroy()
		
		if user == '' and passw == '':
			window.after(2000,setup)

		else:
			login.pack(fill='both',expand=True)


			user_label.place(x=100,y=60)
			username.place(x=100,y=100)
			
			pass_label.place(x=100,y=140)
			password.place(x=100,y=180)
			
			subm.place(x=500,y=125)

			l_h.place(x=100,y=0)
	des_del=0
	start_sho=False
	desktop=Frame(window,bg="black")
	shu_fr=Frame(window,bg="black",width=800,height=600)

	app1_run=False

	def shutdown():
		desktop.destroy()
		
		shu_lbl=Label(shu_fr,text="Shutting Down...",font=("Arial",30,"bold"),bg="black",fg="white")
		window.after(5000,quit)
		shu_lbl.place(x=200,y=200)
		shu_fr.place(x=0,y=0)
	def test():
		print("Working!")
	def scene3():
		global login,user_label,username,pass_label,password,subm,l_h,wa
		login.destroy()
		def app1():
			global app1_run
			def app1_m(event):
				app1_frm.x=event.x
				app1_frm.y=event.y
			def app1_st_m(event):
				x=app1_frm.winfo_x()+event.x-app1_frm.x
				y=app1_frm.winfo_y()+event.y-app1_frm.y
				app1_frm.place(x=x,y=y)

			app1_frm=Frame(desktop,width=350,height=250,bg="white")
			app1_frm.bind("<Button-1>",app1_m)
			app1_frm.bind("<B1-Motion>",app1_st_m)
			app1_frm.pack_propagate(False)
			def exit_app1():
				global app1_run
				app1_run=False

				app1_frm.destroy()
			app1_exit=Button(app1_frm,text="X",font=("Arial",20,"bold"),bg="black",fg="red",command=exit_app1)
			app1_exit.pack(anchor="e",side="top")
			if not app1_run:
				print(app1_run)
				app1_frm.place(x=250,y=150)
				app1_run=True
		
		lo_txt=["Loading Desktop...","Please Wait..","Almost there..","Preparing..","Crafting..","Hi :)"]
		lo_lbl=Label(desktop,text="Loading..",font=("Comic Sans",40,"bold"),bg="black",fg="white")
		lo_lbl.pack()
		sta=Frame(desktop,width=200,height=200,bg="white")
		sta.pack_propagate(False)
		app1_but=Button(sta,text="APP1",font=("Arial",10,"bold"),bg="black",fg="white",command=app1)
		shut_but=Button(sta,text="Shutdown",font=("Arial",10),bg="red",fg="white",command=shutdown)
		app1_but.pack(anchor="w",side="top")
		shut_but.pack(anchor="e",side="bottom")
		def sho_st():
			global start_sho
			if start_sho:
				sta.place_forget()
				start_sho=False
			else:
				sta.place(x=0,y=350)
				start_sho=True
		def set_des():
				bg_dsk=Label(desktop,image=bg_logo,bd=0)
				bg_dsk.place(x=0,y=0)
				bg_dsk.lower()
				lo_lbl.destroy()
				taskbar=Frame(desktop,width=800,height=70,bg="gray")
				start_but=Button(desktop,text="▽",font=("Arial",20,"bold"),bg="#27570E",fg="white",command=sho_st)
				
				
				taskbar.place(x=0,y=550)
				start_but.place(x=0,y=550)
		def set_del():
			global des_del
			if des_del < 5:
				lo_tx=random.choice(lo_txt)
				lo_lbl.config(text=lo_tx)
				des_del+=1
				window.after(3000,set_del)
				
			else:
				lo_lbl.destroy()
				set_des()
		set_del()

		desktop.pack(fill="both",expand=True)
		
	def upd():
		global txt,counter,cont
		if counter < 45:
			txt+="█"
			lbl.config(text=txt)
			counter+=1
			window.after(random.randrange(100,1000),upd)
		else:
			txt=""
			lbl.config(text=txt)
			log_lab.destroy()
			scene2()

	loading.pack(fill='both',expand=True)


	def setup():
		def s_c_sub():
			usrn=user_ent.get()
			pswd=pass_ent.get()
			with open("o","r") as f:
				lines=f.readlines()
				print(lines)
			for i,line in enumerate(lines):
				if line == "user=''\n":
					lines[i]=f"user='{usrn}'\n"
				elif line=="passw=''":
					lines[i]=f"passw='{pswd}'"				
			with open("o","w") as f:
				f.writelines(lines)

			def chkup():
				ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
				subprocess.Popen(["python","bios.py"])
				quit()
			window.after(2000,chkup)
			
		login.destroy()
		s_frm=Frame(window,bg="white")
		cr_frm=Frame(s_frm,bg="gray",width=300,height=400)
		w_lbl=Label(s_frm,text="Welcome!",font=("Comic Sans",20,"bold"),fg="black",bg="white")
		user_ent=Entry(cr_frm,font=("Arial",15),bg="black",fg="green")
		user_lbl=Label(cr_frm,font=("Arial",15),text="New username:",fg="black",bg="white")
		pass_ent=Entry(cr_frm,font=("Arial",15),bg="black",fg="green")
		pass_lbl=Label(cr_frm,font=("Arial",15),text="New password:",fg="black",bg="white")
		subm=Button(cr_frm,text="Submit",font=("Arial",30),bg="black",fg="white",command=s_c_sub)
		user_lbl.place(x=0,y=30)
		user_ent.place(x=0,y=70)
		pass_lbl.place(x=0,y=110)
		pass_ent.place(x=0,y=155)
		subm.place(x=40,y=200)
		cr_frm.place(x=0,y=0)
		s_frm.pack(fill="both",expand=True)
		w_lbl.place(x=300,y=0)


	upd()
	log_lab=Label(window,bd=3,image=logo)
	log_lab.place(x=300,y=100)
	lbl.place(x=0,y=500)
	window.mainloop()