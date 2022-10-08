#GUI - Graphical User Interface

#Libraries
###############
# 1. Tkinter
# 2. PyQt
# 3. Turtle

import tkinter as ttk
app = ttk.Tk()
app.title("my app")
app.geometry('600x400')

ttk.Label(app,text ='A Simple Text Label').place(x=50,y=50)
ttk.Label(app,text ='ragini joshi').place(x=80,y=80)


app.mainloop()
