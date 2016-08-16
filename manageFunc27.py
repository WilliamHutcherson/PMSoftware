import sqlite3

conn = sqlite3.connect('projectTasks.db')
c = conn.cursor()

def createTable():
    c.execute("DROP TABLE IF EXISTS Tasks")
    c.execute("CREATE TABLE IF NOT EXISTS Tasks (ID INTEGER PRIMARY KEY AUTOINCREMENT, Description TEXT, Owner TEXT, Status TEXT, DateComplete TEXT)")

def insertTask(Description):
    c.execute("INSERT INTO Tasks (Description, Owner, Status, DateComplete) VALUES ('{}', 'None', 'None', 'None')".format(Description))
    conn.commit()

def updateOwner(id, owner):
    sql = "UPDATE Tasks SET Owner = '{}' WHERE ID = {}".format(owner, id)
    c.execute(sql)
    conn.commit()

def completeTask(date, id):
    sql = 'UPDATE Tasks SET Status = "Done", DateComplete = "{}" WHERE ID = {}'.format(date, id)
    c.execute(sql)
    conn.commit()
    readCompleted()

def deleteTask(id):
    sql = "DELETE FROM Tasks WHERE ID = {}".format(id)
    c.execute(sql)
    conn.commit()

def getTaskID(desc):
    sql = 'SELECT ID FROM Tasks WHERE Description = "{}"'.format(desc)
    c.execute(sql)
    i = c.fetchall()
    for a in i:
        return int(a)

def readNewTasks():
    sql = 'SELECT ID, Description FROM Tasks WHERE Owner = "None"'
    c.execute(sql)
    t = c.fetchall()
    newList = []
    for rec in t:
        newList.append(rec)
    return newList

def readOwnedTasks():
    sql = 'SELECT ID, Description, Owner FROM Tasks WHERE Owner != "None" AND DateComplete = "None"'
    c.execute(sql)
    o = c.fetchall()
    ownedList = []
    for rec in o:
        ownedList.append(rec)
    return ownedList

def readCompleted():
    sql = 'SELECT Description, Owner, DateComplete FROM Tasks WHERE Status = "Done"'
    d = c.execute(sql)
    finishedList = []
    for rec in d:
        finishedList.append(rec)
    return finishedList

def readAll():
    sql = "SELECT * FROM Tasks"
    c.execute(sql)
    testing = c.fetchall()
    print testing
