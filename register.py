from tkinter import*
from tkinter import ttk,messagebox
#pip install pillow
from PIL import Image,ImageTk
#pip install pymysql
import pymysql
#import sqlite3
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0") 
        self.root.config(bg="white") 
        ##================== Bg Image=====================
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
           
        ##==================Left Image=====================
        self.left=ImageTk.PhotoImage(file="images/side.png")
        let=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
          
        #=============== Register Frame ==================
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500) 
        
        title=Label(frame1,text="REGISTER HERE",font=("time new roman", 20,"bold"),bg="white",fg="green").place(x=50,y=30) 
        
         
        #=================== Row1================= 
        #self.var_fname=StringVar()
        
        f_name=Label(frame1,text="First Name",font=("time new roman", 15,"bold"),bg="white",fg="gray").place(x=50,y=100) 
        self.txt_f_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_f_name.place(x=50,y=130,width=250)   
           
        l_name=Label(frame1,text="Last Name",font=("time new roman", 15,"bold"),bg="white",fg="gray").place(x=370,y=100) 
        self.txt_l_name=Entry(frame1,font=("times new roman", 15),bg="lightgray")
        self.txt_l_name.place(x=370,y=130,width=250)   
        
        
        #=============== Row 2======================
        contact=Label(frame1,text="Contact No.",font=("time new roman", 15,"bold"),bg="white",fg="gray").place(x=50,y=170) 
        self.txt_contact=Entry(frame1,font=("times new roman", 15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)   
         
        email=Label(frame1,text="Email",font=("time new roman", 15,"bold"),bg="white",fg="gray").place(x=370,y=170) 
        self.txt_email=Entry(frame1,font=("times new roman", 15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)   
        
         
        #================== Row 3=================   
        question=Label(frame1,text="Security Question",font=("time new roman", 15,"bold"),bg="white",fg="gray").place(x=50,y=240) 
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman", 13),state='readonly',justify=CENTER)   
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name") 
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        #self.comb_quest.set("Select") 
        
        answer=Label(frame1,text="Answer",font=("time new roman", 15,"bold"),bg="white",fg="gray").place(x=370,y=240) 
        self.txt_answer=Entry(frame1,font=("times new roman", 15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)   
          
           
        #=============== Row 4======================
        password=Label(frame1,text="Password",font=("time new roman", 15,"bold"),bg="white",fg="gray").place(x=50,y=310) 
        self.txt_password=Entry(frame1,font=("times new roman", 15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)   
         
        c_password=Label(frame1,text="Confirm Password",font=("time new roman", 15,"bold"),bg="white",fg="gray").place(x=370,y=310) 
        self.txt_c_password=Entry(frame1,font=("times new roman", 15),bg="lightgray")
        self.txt_c_password.place(x=370,y=340,width=250)   
               
        
        #=============== Terms and Condition============
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Condition",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)   
        
        
        #================ Button===============
        self.btn_img=ImageTk.PhotoImage(file="images/register.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420) 
        
        
        #============== Login Button ==============
        btn_login=Button(self.root,text="Sign In",font=("times new roman",16),bd=0,cursor="hand2",command=self.login_window).place(x=200,y=480,width=180,height=35) 
         
         
    
    
    def login_window(self):
        self.root.destroy()
        os.system("python login.py")
         
         
         
    #================= Clear Details======================     
    def clear(self):
        self.txt_f_name.delete(0,END) 
        self.txt_l_name.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_c_password.delete(0,END)
        self.cmb_quest.current(0)   
        
         
         
    #=============== Save Data to the database==================          
    def register_data(self ):
        if self.txt_f_name.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_c_password.get()=="" :
            messagebox.showerror("Error","All Fields are Required!!",parent=self.root)
        elif self.txt_password.get()!= self.txt_c_password.get():
            messagebox.showerror("Error","Password & Confrim Password should be same !!",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our terms & condition !!",parent=self.root)
        else:
            try:
               con=pymysql.connect(host="localhost",user="root",password="",database="rms")
               cur=con.cursor()
               cur.execute("select * from register where email=%s",(self.txt_email.get(),))
               row=cur.fetchone()
            #  print(row)
               if row!=None:
                   messagebox.showerror("Error","User already exists,Please try with another email !!",parent=self.root)
               else:
                cur.execute("insert into register(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                           (self.txt_f_name.get(),
                            self.txt_l_name.get(),
                            self.txt_contact.get(),
                            self.txt_email.get(),
                            self.cmb_quest.get(),
                            self.txt_answer.get(),
                            self.txt_password.get()
                            ))
               con.commit()
               con.close()
               messagebox.showerror("Success","Record Added Successfully !!",parent=self.root)
               self.clear()
               self.login_window()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
    
    
           
root=Tk()
obj=Register(root)
root.mainloop()