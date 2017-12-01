#main project file. contains most of the GUI code.

from tkinter import *

root = Tk()
root.geometry("250x150")


topFrame = Frame(root)
topFrame.pack()

label_1 = Label(topFrame, text="PDF Directory")
entry_1 = Entry(topFrame)

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

exitButton = Button(bottomFrame, text="Quit", command=root.destroy)
exitButton.pack()




root.mainloop()