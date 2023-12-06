# from tkinter import Tk
# root=Tk()
# root.mainloop()

""""LABEL"""
# from tkinter import*
# root=Tk()
# Label(root,text="hello team").pack()
# root.mainloop()
""""button"""
# from tkinter import *
# root=Tk()
# button=Button(root,text="login",bg="red",fg="white")
# button.pack()
# root.mainloop()

"""FRAME"""
# from tkinter import *
# root=Tk()
# frame=Frame(root)
# frame.pack()
# button=Button(root,text="login",bg="red",fg="white")
# button.pack()
# root.mainloop()




"""FILL"""
# from tkinter import *
# root=Tk()
# frame=Frame(root)
# frame.pack()
# button1=Button(frame,text="login",bg="red",fg="white")
# Button.pack(fill=X,side="bottom")
# button2=Button(frame,text="login",bg="red",fg="white")
# Button.pack(fill=Y,side="left")

# root.mainloop()

"""grid"""
# from tkinter import *
# root=Tk()
# l1=Label(root,text="username")
# e1=Entry(root)
# l2=Label(root,text="password")
# e2=Entry(root)
# bt=Button(root,text="login")
# l1.grid(row=0,column=0)
# e1.grid(row=0,column=1)
# l2.grid(row=1,column=0)
# e2.grid(row=1,column=1)
# bt.grid(row=2,column=1)
# root.mainloop()

"""eg pgm"""

# from tkinter import *
# root=Tk()
# l1=Label(root,text="username")
# e1=Entry(root)
# l2=Label(root,text="mobaile")
# e2=Entry(root)
# l3=Label(root,text="email")
# e3=Entry(root)
# l4=Label(root,text="age")
# e4=Entry(root)
# l5=Label(root,text="password")
# e5=Entry(root)
# l6=Label(root,text="confirmation")
# e6=Entry(root)
# bt=Button(root,text="login")
# bt=Button(root,text="login")
# l1.grid(row=0,column=0)
# e1.grid(row=0,column=1)
# l2.grid(row=1,column=0)
# e2.grid(row=1,column=1)
# l3.grid(row=2,column=0)
# e3.grid(row=2,column=1)
# l4.grid(row=3,column=0)
# e4.grid(row=3,column=1)
# l5.grid(row=4,column=0)
# e5.grid(row=4,column=1)
# l6.grid(row=5,column=0)
# e6.grid(row=5,column=1)
# bt.grid(row=7,column=0)
# bt.grid(row=7,column=1)
# root.mainloop()


"""event"""
# from tkinter import *
# root=Tk()
# def asd():
#     print("hello")
# Button(root,text="ok",command=asd).pack()
# root.mainloop()



# from tkinter import *
# from tkinter import messagebox
# root=Tk()
# def asd():
#     # messagebox.showinfo("delet","are you sure to delet?")
#     # messagebox.showwarning("delet","are you sure to delet?")
#     # messagebox.askokcancel("delet","are you sure to delet?")
#     # messagebox.askquestion("delet","are you sure to delet?")
#     # messagebox.askretrycancel("delet","are you sure to delet?")
#     messagebox.askyesno("delet","are you sure to delet?")
    
# Button(root, text="ok",command=asd).pack()
# root.mainloop()


""""using class"""
# from tkinter import *
# class myclass:
#     def __init__(self,rootone):
#         frame=Frame(rootone)
#         frame.pack()
#         self.okbtn=Button(frame,text="ok",command=self.oks)
#         self.okbtn.pack()
#         self.quitbtn=Button(frame,text="oks",command=frame.quit)
#         self.quitbtn.pack()
#     def oks(self):
#         print("hello team")
# root=Tk()
# obj=myclass(root)
# root.mainloop()


""""eg pgm"""
# from tkinter import *
# root= Tk()
# l1=Label(root,text="enter first name")
# e1=Entry(root)
# l2=Label(root,text="enter second name")
# e2=Entry(root)
# # l3=Label(root,text="result")
# # e3=Entry(root)
# bt=Button(root,text="add")
# def exit():
#     exit()
# button=Button(root,text="exit",command=root.quit)
# l3=Label(root,text="result")
# l1.grid(row=0,column=0)
# e1.grid(row=0,column=1)
# l2.grid(row=1,column=0)
# e2.grid(row=1,column=1)
# # l3.grid(row=2,column=0)
# # e3.grid(row=2,column=1)
# bt.grid(row=2,column=0)
# button.grid(row=2,column=1)
# l3.grid(row=2,column=0)


# root.mainloop()

        


# from tkinter import *
# root =Tk()
# Frame=Frame(root)
# Frame.pack()
# l1=Label(Frame,text="enter first number")
# l1.pack()
# e1=Entry(Frame)
# e1.pack()
# l2=Label(Frame,text="enter second number")
# l2.pack()
# e2=Entry(Frame)
# e2.pack()
# frr=Frame(root)
# frr.pack()
# bt1=Button(frr,text="add")
# bt1.grid(row=0,column=0)
# bt2=Button(frr,text="add")
# bt2.grid(row=0,column=1)
# fm=Frame(root)
# fm.pack()
# l3=Label

""""calculator"""

# from tkinter import *
# def add():
#     num1=float(e1.get())
#     num2=float(e2.get())
#     res.set(num1+num2)
# def mul():
#     num1=float(e1.get())
#     num2=float(e2.get())
#     res.set(num1*num2)
# def div():
#     num1=float(e1.get())
#     num2=float(e2.get())
#     res.set(num1/num2)
    
    
# app=Tk()
# app.title("calculator")
# l1=Label(app,text="enter first number")
# l1.pack()
# e1=Entry(app)
# e1.pack()
# l2=Label(app,text="enter second number")
# l1.pack()
# e2=Entry(app)
# e2.pack()
# btn=Button(app,text="sum",command=add)
# btn.pack()
# btn1=Button(app,text="mul",command=mul)
# btn1.pack()
# btn2=Button(app,text="div",command=div)
# btn2.pack()
# res=StringVar()
# res.set("result")
# l3=Label(app,textvariable=res)
# l3.pack()
# app.mainloop()


"""bmicalculator"""
from tkinter import *
def bmi():
    num1=float(e1.get())
    num2=float(e2.get())
    
    

app= Tk()
app.title("bmi calculator")
l1=Label(app,text="enter the age")
l1.pack()
e1=Entry()
e1.pack()
l2=Label(app,text="enter the hight")
e2=Entry()
e2.pack()
l3=Label(app,text="enter the weight")
l3.pack()
e3=Entry()
e3.pack()







        
        
        
        
        
        
        
        
        
        
