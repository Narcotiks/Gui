from tkinter import *
import time

mainWindow = Tk()
time1 = ''
def testy():
    print("Test")

def update_time():
    time1 = time.strftime('%A, %d/%m/%Y    %H:%M:%S')
    print (time1)
    mainWindow.update()

# ******** Main Menu ********
frame = Frame(mainWindow, width=800, height=600)
frame.pack()

menu = Menu(mainWindow)
mainWindow.config(menu=menu)

fileMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Login", command=testy)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=mainWindow.quit)

notifMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Notifications", menu=notifMenu)
notifMenu.add_command(label="Add Notification", command=testy)
notifMenu.add_command(label="View Notifications", command=testy)
notifMenu.add_command(label="Get Order Number", command=testy)

partsMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Parts", menu=partsMenu)
partsMenu.add_command(label="Part List", command=testy)
partsMenu.add_command(label="Manuals", command=testy)

naviMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Navigation", menu=naviMenu)
naviMenu.add_command(label="Display Map", command=testy)

adminMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Admin", menu=adminMenu)

# ******** Status Bar ********

status = Label(mainWindow, text=time1, bd=2, relief=SUNKEN, anchor=W)
status.after(200, update_time)
status.pack(side=BOTTOM, fill=X)



mainWindow.mainloop()