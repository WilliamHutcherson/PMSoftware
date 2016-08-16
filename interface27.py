from Tkconstants import RIGHT, X
from Tkinter import *
import Tkinter
import ttk
import manageFunc27
import datetime

class App(Tk):

    def __init__(self):
        Tkinter.Tk.__init__(self)

        

        leftPane = Frame(self, width=300, height=500, relief=SUNKEN, bd=5, bg="#ccccb3")
        leftPane.grid(row=0, column=0)
        leftPane.grid_columnconfigure(0,minsize=300)

        leftLabel = Label(leftPane, text="Task Pool:", bg="#ccccb3", font='bold')
        leftLabel.grid(row=0, column=0, sticky='w')

        addButton = Button(leftPane, text="Create New Task", command=self.makeNew)
        addButton.grid(row=0, column=0, sticky='e')

        self.taskBox = Listbox(leftPane, height=27, width=50, relief=SUNKEN, bg="#ccccb3")
        self.taskBox.grid(row=1, column=0, sticky='w')

        self.selected = self.taskBox.curselection

        claimButton = Button(leftPane, text="Claim A Task", command=self.makeClaim)
        claimButton.grid(row=2, column=0, pady=2)

        midPane = Frame(self, width=300, height=500, relief=SUNKEN, bd=5, bg="#ccccb3")
        midPane.grid(row=0, column=1)
        midPane.grid_columnconfigure(0,minsize=300)

        midLabel = Label(midPane, text="Owned Tasks:", bg="#ccccb3", font='bold')
        midLabel.grid(row=0, column=0, sticky='w')

        self.ownedBox = Listbox(midPane, height=27, width=50, relief=SUNKEN, bg="#ccccb3")
        self.ownedBox.grid(row=1, column=0, sticky='w')

        self.finished = self.ownedBox.curselection

        finishButton = Button(midPane, text="Complete Task", command=self.finishTask)
        finishButton.grid(row=2, column=0, pady=2)

        rightPane = Frame(self, width=300, height=500, relief=SUNKEN, bd=5, bg="#ccccb3")
        rightPane.grid(row=0, column=2)
        rightPane.grid_columnconfigure(0,minsize=300)

        rightLabel = Label(rightPane, text="Completed Tasks:", bg="#ccccb3", font='bold')
        rightLabel.grid(row=0, column=0, sticky='w')

        self.finishedBox = Listbox(rightPane, height=29, width=50, relief=SUNKEN, bg="#ccccb3")
        self.finishedBox.grid(row=1, column=0, sticky='w')

        

    def makeNew(self):
        self.top = Tk()
        self.top.title("Add New Task")
        newLabel = Label(self.top, text="Please enter a description:")
        newLabel.pack(side=TOP)

        self.descText = Text(self.top, height=5, width=40)
        self.descText.pack(side=LEFT)

        newButton = Button(self.top, text="Create Task", command=self.addTask)
        newButton.pack(side=BOTTOM)

    def makeClaim(self):
        self.top = Tk()
        self.top.title("Claim A Task")

        getSelected = self.taskBox.get(self.selected()[0])
        
        self.owned = StringVar()
        
        claimLabel = Label(self.top, text="Select Claim User")
        claimLabel.pack(side=TOP)

        self.userList = ttk.Combobox(self.top, values="User1 User2 User3", textvariable=self.owned)
        self.userList.pack(side=LEFT)

        self.claim = Button(self.top, text="Claim", command=lambda:self.claimTheTask(getSelected))
        self.claim.pack(side=BOTTOM)

    def addTask(self):
        desc = self.descText.get("1.0", END)
        manageFunc27.insertTask(desc)
        self.top.destroy()
        self.updateListBox()


    def claimTheTask(self, getSelected):
        taskSel = getSelected[0]
        owner = self.userList.get()
        manageFunc27.updateOwner(taskSel, owner)
        self.top.destroy()
        self.updateOwnedBox()
        self.updateListBox()

    def finishTask(self):
        getFinished = self.ownedBox.get(self.finished()[0])
        finishID = getFinished[0]
        date = datetime.datetime.now()
        date = date.strftime('%d/%m/%y')
        manageFunc27.completeTask(date, finishID)
        self.updateFinishedBox()
        self.updateOwnedBox()

    def popListBox(self):
        rows = manageFunc27.readNewTasks()
        for row in rows:
            self.taskBox.insert(END, row)

    def popOwnedBox(self):
        ownedRows = manageFunc27.readOwnedTasks()
        if ownedRows != None:
            for row in ownedRows:
                self.ownedBox.insert(END, row)

    def popFinishBox(self):
        finishedRows = manageFunc27.readCompleted()
        if finishedRows != None:
            for row in finishedRows:
                self.finishedBox.insert(END, row)

    def updateListBox(self):
        self.taskBox.delete(0, END)
        lastRow = manageFunc27.readNewTasks()
        for row in lastRow:
            self.taskBox.insert(END, row)

    def updateOwnedBox(self):
        self.ownedBox.delete(0, END)
        thisRow = manageFunc27.readOwnedTasks()
        for row in thisRow:
                self.ownedBox.insert(END, row)

    def updateFinishedBox(self):
        self.finishedBox.delete(0, END)
        finishedRow = manageFunc27.readCompleted()
        for row in finishedRow:
                self.finishedBox.insert(END, row)




ap = App()
ap.title("Task Management")
ap.popListBox()
ap.popOwnedBox()
ap.popFinishBox()


ap.mainloop()

