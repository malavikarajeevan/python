from tkinter import *
root=Tk()
toolbar=Frame(root,bg="blue")
btn1=Button(toolbar,text="crop")
btn1.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(fill="x",side=TOP)
statusbar=Label(root,text="this is status bar",anchor=W,bg="blue",fg="white")
statusbar.pack(fill="x",side=BOTTOM)
root.mainloop()