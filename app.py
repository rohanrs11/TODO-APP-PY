"""
Read fileName from Command Line
readData(fileName) -> it return a list containing all lines present in the file otherwise if file doesn't exist raise ValueError
formatString(task) -> dictionary in a perfect manner
formatData(rawData) -> returns a formmated list of todos
showAllTodo() -> print all todos in that file in a formatted way
showAllTodoByStatus(status) -> shows all todo with that status
showTodoByName(name) -> return you the information of that todo
showAllTodoByTime(time) -> will shw all todo at that time
addTodo() -> will allow you to add more todo
deleteTodoByName(name) -> will delete the todo with that name
updateTodoTimeByName(name) -> will update the todo time
deleteTodoByTime(time) -> will remove all todos at that time
"""


# rohan = "ADARSH@12#DONE"
# rohan = "ROHAN S@15#UNDONE"

# a = rohan[:rohan.index('@')]
# b = rohan[rohan.index('@')+ 1: rohan.index('#')]
# c = rohan[rohan.index('#')+ 1:]


# print(formatString("PLAY CRICKET@2:00 PM#DONE\n"))

# readData(todoFileName)
# print(rawData)

from sys import argv, exit
from os.path import exists


def readData(fileName):

    global rawData
    if exists(fileName):
        fileObject = open(fileName, "r")
        rawData = fileObject.readlines()
        fileObject.close()
    else:
        raise FileExistsError("File doesn't exist")


def formatString(task):
    if task[-1] == "\n":
        task = task[:len(task)-1]
    name = task[:task.index('@')]
    time = task[task.index('@') + 1: task.index('#')]
    status = task[task.index('#') + 1:]
    return {
        "name": name,
        "time": time,
        "status": status
    }


def formatData():
    global formattedData
    for each in rawData:
        formattedData.append(formatString(each))


def printTodo(todo):
    """This function will print the name, time, and status of a"""
    print(f"NAME -> {todo['name'].title()}")
    print(f"TIME -> {todo['time'].upper()}")
    print(f"STATUS -> {todo['status'].title()}")


def showAllTodo():
    if len(formattedData) > 0:
        print("All TODOS ARE --->")
        for i in range(len(formattedData)):
            print(f"----- TODO {i+1} -----")
            printTodo(formattedData[i])
    else:
        print("----- NO TODOS AVAILABLE -----")


def showAllTodoByStatus(status):
    cnt = 0
    for each in formattedData:
        if each['status'].lower() == status.lower():
            cnt += 1
            print(f"----- TODO {cnt} -----")
            printTodo(each)
    if cnt == 0:
        print("----- NO TODOS WITH THIS STATUS -----")


def showTodoByName(name):
    cnt = 0
    for each in formattedData:
        if each['name'].lower() == name:
            cnt += 1
            print("--- REQUIRED TODO -----")
            printTodo(each)
    if cnt == 0:
        print("OOPS, NO TODO IS THERE WITH THE NAME PROVIDED.")


def showAllTodoByTime(time):
    cnt = 0
    for each in formattedData:
        if each['time'].lower() == time.lower():
            cnt += 1
            print(f"----- TODO {cnt} -----")
            printTodo(each)
    if cnt == 0:
        print("OOPS, NO TODO IS THERE WITH THE TIME PROVIDED.")


def writeDataIntoFile(listOfData):
    fileObject = open(argv[1], "w")
    for each in listOfData:
        fileObject.write(
            f"{each['name'].upper()}@{each['time'].upper()}#{each['status'].upper()}\n")
    fileObject.close()


def addTodo():
    global formattedData
    name = input("Enter The Name of Todo >>> ").title()
    time = input("Enter The Time of The Todo >>> ").upper()
    status = input("Enter The Status of The Todo >>> ").title()
    todo = {
        "name": name,
        "time": time,
        "status": status
    }
    formattedData.append(todo)
    writeDataIntoFile(formattedData)
    print("----- TODO ADDED SUCCESSFULLY -----")


def updateTodoTimeByName(name):
    global formattedData
    cnt = 0
    for each in formattedData:
        if each['name'].upper() == name.upper():
            cnt += 1
            newTime = input("Enter The New Time >>> ")
            each['time'] = newTime.upper()
            writeDataIntoFile(formattedData)
            print("----- TIME UPDATED SUCCESFULLY -----")
            break
    if cnt == 0:
        print("OOPS, NO TODO WITH THAT NAME EXISTS!!")


def deleteTodoByName(name):
    global formattedData
    cnt = 0
    for each in formattedData:
        if each['name'].upper() == name.upper():
            cnt += 1
            formattedData.remove(each)
            writeDataIntoFile(formattedData)
            print("----- TODO DELETED SUCCESSFULLY -----")
            break
    if cnt == 0:
        print("OOPS, NO TODO WITH THAT NAME EXISTS!!!")


def deleteTodoByTime(time):
    global formattedData
    cnt = 0
    for each in formattedData:
        if each['time'].upper() == time.upper():
            cnt += 1
            formattedData.remove(each)
    writeDataIntoFile(formattedData)
    if cnt == 0:
        print("OOPS, NO TODO WITH THAT NAME EXISTS!!!")
    else:
        print("----- TODOS DELETED SUCCESSFULLY -----")


todoFileName = argv[1]
rawData = []
formattedData = []

readData(todoFileName)
formatData()

print("-"*5, " WELCOME TO TODO APP ", "-"*5)
while True:
    print("----- MENU -----")
    print("Press 1 to See All TODO")
    print("Press 2 to See All TODO By Time")
    print("Press 3 to See All TODO By Status")
    print("Press 4 to See A Particular TODO's info")
    print("Press 5 to Add a TODO")
    print("Press 6 to Update TODO Time")
    print("Press 7 to Delete a TODO")
    print("Press 8 to Delete all TODO's with a Particular Time")
    print("Press 0 to EXIT")
    userChoice = input("Enter The Choice >>> ")
    if userChoice == '1':
        showAllTodo()
    elif userChoice == '2':
        time = input("Enter The Time >>> ")
        showAllTodoByTime(time)
    elif userChoice == '3':
        status = input("Enter The Status >>> ")
        showAllTodoByStatus(status)
    elif userChoice == '4':
        name = input("Enter The TODO Name >>> ")
        showTodoByName(name)
    elif userChoice == '5':
        addTodo()
    elif userChoice == '6':
        name = input("Enter The Name >>> ")
        updateTodoTimeByName(name)
    elif userChoice == '7':
        name = input("Enter The Name >>> ")
        deleteTodoByName(name)
    elif userChoice == '8':
        time = input("Enter The Time >>> ")
        deleteTodoByTime(time)
    elif userChoice == '0':
        print("----- Have A Nice Day -----")
        exit(0)
