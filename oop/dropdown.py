from tkinter import *
root =Tk()
mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="new file")
submenu.add_command(label="open file")
submenu.add_command(label="open folder")
submenu.add_separator()
submenu.add_command(label="save")
newmenu=Menu(mymenu)
mymenu.add_cascade(label="edit",menu=newmenu)
newmenu.add_command(label="new file")
newmenu.add_command(label="open file")
newmenu.add_command(label="open folder")
newmenu.add_separator()
newmenu.add_command(label="save")


newmenu.add_command(label="undo")
newmenu1=Menu(mymenu)
mymenu.add_cascade(label="view",menu=newmenu1)
newmenu1.add_command(label="side bar")
newmenu1.add_command(label="toolbar")
newmenu1.add_command(label="menu bar")
newmenu1.add_separator()
newmenu1.add_command(label="save")
newmenu2=mymenu(mymenu)





root.mainloop()

