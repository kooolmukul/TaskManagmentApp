from tkinter import *
import tkinter.ttk as ttk
import database

window = Tk()
tree = ttk.Treeview(window)
#------------------------------ ButtonFunction-----------------

def addTask():
    database.insert(taskVar.get(), assignVar.get())
    ViewList()

def ViewList():
    rowid = 0
    tree.delete(*tree.get_children())
    for row in database.view():
        tree.insert("",rowid,text='',values= row)
        rowid+=1

# -------------------------Labels -------------------------------

l1 = Label(window,text="Task")
l1.grid(row=0, column=0)

l2 = Label(window,text="AssignedTo")
l2.grid(row=0, column=2)

l3 = Label(window,text="Status")
l3.grid(row=0, column=4)

#------------------------optionMenu -------------------------
taskVar = StringVar()
taskVar.set('task1')

taskMenu = OptionMenu(window, taskVar, 'Garbage','Cleaning','Task3')
taskMenu.grid(row=0,column=1)

assignVar = StringVar()
assignVar.set('person1')

assignMenu = OptionMenu(window, assignVar, 'Harshit','Pratik','Sandeep')
assignMenu.grid(row=0,column=3)

statusVar = StringVar()
statusVar.set('Pending')

statusMenu = OptionMenu(window, statusVar, 'Pending','Completed')
statusMenu.grid(row=0,column=5)

#----------------------------------TreeView--------------------------

treeColumns = ('id','task','assignTo','status')
tree['columns'] = treeColumns
tree['show'] = 'headings'
tree.column('id', width=25)
tree.column('task', width=100)
tree.column('assignTo', width=100)
tree.column('status', width=70)

for column in treeColumns:
    print('i')
    tree.heading(column, text = column.capitalize())

ViewList()

tree.grid(row=2,column=0, rowspan=4,columnspan = 5)

#----------------------------------button---------------------------------------

addBtn = Button(window,text = 'Add task', width= 12, command = addTask)
addBtn.grid(row=2, column=5)

updateBtn = Button(window,text = 'Update task', width= 12)
updateBtn.grid(row=3, column=5)

deleteBtn = Button(window,text = 'Delete task', width= 12)
deleteBtn.grid(row=4, column=5)

searchBtn = Button(window,text = 'Search task', width= 12)
searchBtn.grid(row=5, column=5)




window.mainloop()
