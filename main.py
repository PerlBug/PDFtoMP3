#main project file. contains most of the GUI code.

from tkinter import filedialog
from tkinter import *


root = Tk()
root.geometry("300x150")

def openFile(event):
    filedialog.askopenfilename(filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))


topFrame = Frame(root)
topFrame.pack()

pathLabel = Label(topFrame, text="PDF Directory")
pathEntry = Entry(topFrame)
pathIcon = PhotoImage(file="gui/open.png")
pathIconLabel = Label(topFrame, image= pathIcon)
pathIconLabel.bind("<Button-1>", openFile)

pathLabel.grid(row=0, column=0)
pathEntry.grid(row=0, column=1)
pathIconLabel.grid(row=0, column=2)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

exitButton = Button(bottomFrame, text="Quit", command=root.destroy)
exitButton.pack()




root.mainloop()