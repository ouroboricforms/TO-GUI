from tkinter import *

def doNothing():
    print("hello")

root = Tk()
root.minsize(width=800, height=600)

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="Now...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

tournamentMenu = Menu(menu)
menu.add_cascade(label="Tournament", menu=tournamentMenu)
tournamentMenu.add_command(label="copy", command=doNothing)

playersMenu = Menu(menu)
menu.add_cascade(label="Players", menu=playersMenu)

pairingsMenu = Menu(menu)
menu.add_cascade(label="Pairings", menu=pairingsMenu)

standingsMenu = Menu(menu)
menu.add_cascade(label="Standings", menu=standingsMenu)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)

currentTournamentsMenu = Menu(menu)
menu.add_cascade(label="Current Tournaments", menu=currentTournamentsMenu)

# ***** toolbar *****

toolbar = Frame(root, bg="grey")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


root.mainloop()
