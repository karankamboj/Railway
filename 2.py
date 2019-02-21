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
        #Exit Button
        self.backb1=Button(self.master,text="Exit!",font="20",command=self.exitfxn)
        self.backb1.place(x=900,y=50)
        #Back Button
        self.logoutbutton=Button(self.master,text="Logout",font="20",command=self.logoutfxn)
        self.logoutbutton.place(x=900,y=120)
        self.logoutbutton.lower() #hide it because not in use now

        #Calling Login Screen
        self.mainfxn()

    def mainfxn(self):
        #Main Heading for GUI
        self.heading=Label(self.master,text="Railway Ticket Book Machine",font="forte 20 bold underline")
        self.heading.place(x=280,y=30)
        self.loginheading=Label(self.master,text="Please Login",font="10")
        self.loginheading.place(x=410,y=120)
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
        self.mainregisterbutton=Button(self.master,text="Register",font="20",command=self.registerfxn)
        self.mainregisterbutton.place(x=500,y=400)

    def loginbtn(self):
        if(self.f7.get()=="admin" and self.f8.get()=="admin"):
            self.adminpage()
            return

        else:
            A=self.f7.get()
            B=self.f8.get()
            templist=(A,B)
            fetchlist=list(c.execute("select * from logindetails"))
            if(templist in fetchlist):
                tkinter.messagebox.showinfo("Succes","Login Successfull")
                self.userpage()
            else:
                tkinter.messagebox.showinfo("Error","Wrong username or password!")

    def userpage(self):
        self.loginheading.lower() #Hiding Login Label
        #hiding register button
        self.mainregisterbutton.lower()
        #Show Logout logoutbutton
        self.logoutbutton.lift()
        #Hiding
        self.l8.lower()
        self.l9.lower()
        self.f7.lower()
        self.f8.lower()
        self.b3.lower()
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

        return

    def adminpage(self):
        self.loginheading.lower() #Hiding Login Label
        #hiding register button
        self.mainregisterbutton.lower()

        self.logoutbutton.lift() #Showing Logout Button
        #Hiding old things
        self.l8.lower()
        self.l9.lower()
        self.f7.lower()
        self.f8.lower()
        self.b3.lower()
        self.l1a=Label(self.master,text="Time",font="20 ")
        self.l2a=Label(self.master,text="Train No",font="20 ")
        self.l3a=Label(self.master,text="Ticket",font="20 ")
        self.l4a=Label(self.master,text="Source",font="20 ")
        self.l5a=Label(self.master,text="Destination",font="20 ")
        self.l1a.place(x=200,y=150)
        self.l2a.place(x=200,y=200)
        self.l3a.place(x=200,y=250)
        self.l4a.place(x=200,y=300)
        self.l5a.place(x=200,y=350)
        self.f1a=Entry(self.master)
        self.f2a=Entry(self.master)
        self.f3a=Entry(self.master)
        self.f4a=Entry(self.master)
        self.f5a=Entry(self.master)
        self.f1a.place(x=400,y=150)
        self.f2a.place(x=400,y=200)
        self.f3a.place(x=400,y=250)
        self.f4a.place(x=400,y=300)
        self.f5a.place(x=400,y=350)
        self.b1a=Button(text="Add Train!",font="20",command=self.insertdata)
        self.b1a.place(x=330,y=420)


    def submitclick(self):
        if(self.variable1.get()=="Select" or self.variable2.get()=="Select" or self.f3.get()=="k"):
            tkinter.messagebox.showinfo("Error","Please Fill all The Details!")
        else:

            #Option for Train
            cmnd="SELECT Trainno,Time,Ticket from trains where Source=? and Destination=?"
            c.execute(cmnd,(self.variable1.get(),self.variable2.get()))
            clist=list(c)
            for i in range(0,len(clist)):
                clist[i]=list(clist[i])
            for i in range(0,len(clist)):
                clist[i][0]="Train No :"+str(clist[i][0])
                clist[i][1]="Time :"+str(clist[i][1])
                clist[i][2]="Ticekt :"+str(clist[i][2])
            if(len(clist)==0):
                tkinter.messagebox.showinfo("Error","No Trains found for this Route!")
                return
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

            #show all trains info
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

    def logoutfxn(self):
        self.mainregisterbutton.lift() #Showing Register Button
        self.loginheading.lift() #Show Please Login
        try:
            self.f4.lower()
            self.f5.lower()
            self.f6.lower()
            self.l4.lower()
            self.l5.lower()
            self.l6.lower()
            self.l7.lower()
            self.b2.lower()
            self.d2.lower()
        except:
            pass
        #Hiding Elements of user page
        try:
            self.l1.lower()
            self.l2.lower()
            self.l3.lower()
            self.f1.lower()
            self.f2.lower()
            self.f3.lower()
            self.b1.lower()

        except:
            pass

        try:
            self.l1a.lower()
            self.l2a.lower()
            self.l3a.lower()
            self.l4a.lower()
            self.l5a.lower()
            self.f1a.lower()
            self.f2a.lower()
            self.f3a.lower()
            self.f4a.lower()
            self.f5a.lower()
            self.b1a.lower()
        except:
            pass

        #Hiding Logout logoutbutton
        self.logoutbutton.lower()
        #Showing Elements of Main Page
        self.l8.lift()
        self.l9.lift()
        self.f7.lift()
        self.f8.lift()
        self.b3.lift()

    def insertdata(self):
        A=self.f1a.get()
        B=self.f2a.get()
        C=self.f3a.get()
        D=self.f4a.get()
        E=self.f5a.get()
        c.execute("INSERT INTO trains VALUES (?,?,?,?,?)",(A,B,C,D,E))
        tkinter.messagebox.showinfo("Succes","New Train Added")
        clist=c.execute("select * from Trains")


    def exitfxn(self):
        conn.commit()
        root.destroy()

    def registerfxn(self):
        registerwindow=Toplevel()
        self.registerwindow=registerwindow
        canvas1=Canvas(registerwindow,bg='red',width=700,height=500)
        canvas1.pack()

	    #heading
        self.heading=Label(registerwindow,text="Railway Ticket Book Machine",font="forte 20 bold underline")
        self.heading.place(x=150,y=30)
        #creating
        self.regl1=Label(registerwindow,text="Name",font="20")
        self.regl2=Label(registerwindow,text="Age",font="20")
        self.regl3=Label(registerwindow,text="Address",font="20")
        self.regl4=Label(registerwindow,text="Account No",font="20")
        self.regl5=Label(registerwindow,text="Username",font="20")
        self.regl6=Label(registerwindow,text="Password",font="20")
        self.regf1=Entry(registerwindow)
        self.regf2=Entry(registerwindow)
        self.regf3=Entry(registerwindow)
        self.regf4=Entry(registerwindow)
        self.regf5=Entry(registerwindow)
        self.regf6=Entry(registerwindow,show='*')
        self.regbutton=Button(registerwindow,text="Register",font="20",command=self.registercomplete)
        #Setting the location
        self.regl1.place(x=150,y=100)
        self.regl2.place(x=150,y=150)
        self.regl3.place(x=150,y=200)
        self.regl4.place(x=150,y=250)
        self.regl5.place(x=150,y=300)
        self.regl6.place(x=150,y=350)

        self.regf1.place(x=400,y=100)
        self.regf2.place(x=400,y=150)
        self.regf3.place(x=400,y=200)
        self.regf4.place(x=400,y=250)
        self.regf5.place(x=400,y=300)
        self.regf6.place(x=400,y=350)
        self.regbutton.place(x=300,y=400)

    def registercomplete(self):
        tkinter.messagebox.showinfo("Success","Registeration Succesful!")
        A=self.regf5.get() #get username from feild
        B=self.regf6.get() #
        c.execute("insert into logindetails values(?,?)",[A,B])
        self.registerwindow.destroy()


root=Tk()
root.title("Railway Ticket System")
image = Image.open('k1.jpg')
photo_image = ImageTk.PhotoImage(image)
label = Label(root,image = photo_image)
label.pack()
b=Karan(root)
root.mainloop()
