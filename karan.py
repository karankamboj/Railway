from tkinter import *
from turtle import *
import sqlite3
import tkinter.messagebox
from PIL import ImageTk,Image
from random import randint
conn=sqlite3.connect("db.db")
c=conn.cursor()
class Karan:
    def __init__(self,master):
        self.master=master
        self.mainfxn()
    def mainfxn(self):
        #Main Heading for GUI
        self.heading=Label(self.master,text="Railway Ticket Book Machine",font="forte 20 bold underline")
        self.heading.place(x=280,y=30)

        self.l8=Label(self.master,text="Username",font="20")
        self.l8.place(x=300,y=200)
        self.l9=Label(self.master,text="Password",font="20")
        self.l9.place(x=300,y=300)
        self.f7=Entry(self.master)
        self.f7.place(x=500,y=200)
        self.f8=Entry(self.master,show="*")
        self.f8.place(x=500,y=300)
        self.b3=Button(self.master,text="Login",font="20",command=self.loginbtn)
        self.b3.place(x=400,y=400)

    def loginbtn(self):
        if(self.f7.get()!="karan" and self.f8!="karan"):
            tkinter.messagebox.showinfo("Error","Incorrect Login or Password!")
            return
        #Hiding
        self.l8.lower()
        self.l9.lower()
        self.f7.lower()
        self.f8.lower()
        self.b3.lower()

        #Command to make new window open
        '''win=Toplevel()
        self.master=win '''


        #Labels for GUI
        self.l1=Label(self.master,text="Source",font=" 20")
        self.l1.place(x=80,y=150)
        self.l2=Label(self.master,text="Destination",font=" 20")
        self.l2.place(x=80,y=210)
        self.l3=Label(self.master,text="Date of Journey",font=" 20")
        self.l3.place(x=80,y=270)
        #GUI Fields and OptionMenu
        self.variable1=StringVar(self.master)
        self.variable1.set("Select")
        self.f1=OptionMenu(self.master,self.variable1,"Kurukshetra","Chandigarh","Delhi","Sirsa")
        self.f1.place(x=380,y=150)
        self.variable2= StringVar(self.master)
        self.variable2.set("Select")
        self.f2=OptionMenu(self.master,self.variable2,"Kurukshetra","Chandigarh","Delhi","Sirsa")
        self.f2.place(x=380,y=210)
        self.f3=Entry(self.master)
        self.f3.place(x=380,y=270)

        #Button
        self.b1=Button(self.master,text="Find Trains",font=" 20 ",command=self.submitclick)
        self.b1.place(x=380,y=330)

    def submitclick(self):
        if(self.variable1.get()=="Select" or self.variable2.get()=="Select" or self.f3.get()=="k"):
            tkinter.messagebox.showinfo("Error","Please Fill all The Details!")
        else:
            #Lables
            self.l4=Label(self.master,text="Name",font="20") #Name
            self.l4.place(x=580,y=150)
            self.l5=Label(self.master,text="Age",font="20") #age
            self.l5.place(x=580,y=210)
            self.l6=Label(self.master,text="Phone No",font="20") #phone no
            self.l6.place(x=580,y=270)
            self.l7=Label(self.master,text="Select the train",font="20") #phone no
            self.l7.place(x=580,y=330)
            #Fields
            self.f4=Entry(self.master) #Name
            self.f4.place(x=750,y=150)
            self.f5=Entry(self.master) #age
            self.f5.place(x=750,y=210)
            self.f6=Entry(self.master) #phone no
            self.f6.place(x=750,y=270)
            #Option for Train
            cmnd="SELECT Trainno,Time,Ticket from trains where Source=? and Destination=?"
            c.execute(cmnd,(self.variable1.get(),self.variable2.get()))
            clist=list(c)
            print(clist)
            for i in range(0,len(clist)):
                clist[i]=list(clist[i])
            for i in range(0,len(clist)):
                clist[i][0]="Train No :"+str(clist[i][0])
                clist[i][1]="Time :"+str(clist[i][1])
                clist[i][2]="Ticekt :"+str(clist[i][2])

            self.var3=StringVar(self.master)
            self.var3.set("Select")
            self.d2=OptionMenu(self.master,self.var3,*clist)
            self.d2.place(x=750,y=330)

            #Book Button
            self.b2=Button(self.master,text="Book Train!",font=" 20 ",command=self.bookfxn)
            self.b2.place(x=750,y=400)
    def bookfxn(self):
        if(self.var3.get()=="Select" or self.f4.get()=="" or self.f5.get()=="" or self.f6.get()==""):
            tkinter.messagebox.showinfo("Error","Please Fill all The Details!")
        else:
            tkinter.messagebox.showinfo("Ticket Booked!","Issued Ticket No : "+str(randint(1,500)))
            self.f4.lower()
            self.f5.lower()
            self.f6.lower()
            self.l4.lower()
            self.l5.lower()
            self.l6.lower()
            self.l7.lower()
            self.b2.lower()
            self.d2.lower()



root=Tk()
root.title("Railway Ticket System")
image = Image.open('k1.jpg')
photo_image = ImageTk.PhotoImage(image)
label = Label(root,image = photo_image)
label.pack()
b=Karan(root)
#root.bind("<enter>",command=loginbtn)
root.mainloop()
