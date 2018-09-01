from MyClass import MyClass


def init():
    tasksList = []


def menu():
    print("====Application menu====")
    print("1. Output tasks")
    print("2. Add task")
    print("3. Edit task")
    print("4. Mark as completed")
    print("5. Delete task")
    print("0. Close the app")
    print("========================")
    choice = input()
    return choice


def is_task_found(name):
    for task in tasksList:
        if task.name == name:
            return True
        else:
            return False


def add_task(name):
    tasksList.append(name)


def edit_ask(name, new_name):

    for task in tasksList:
        if task.name == name:
            task.name = new_name


def get_list():
    i = 0
    for task in tasksList:
        print(task.name)


def switch(choice):
    switcher = {
        1: get_list(),
        2: tasksList.append("Test")
    }


tasksList = []
while True:
    get_list()
    choice = menu()
    if choice == '0':
        quit()
    if choice == '1':
        get_list()
    if choice == '2':
        name = input("Enter the name of the task")
        new_task = MyClass(name)
        add_task(new_task)
    if choice == '3':
        name = input("Enter task name for editing")
        if not is_task_found(name):
            print("There is no " + name + " task!")
        else:
            new_name = input("Enter new name for the task " + name)
            edit_ask(name, new_name)
