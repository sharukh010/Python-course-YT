from tabulate import tabulate
"""
Todo Application: 
1. add a todo (title)
2. display (pending/ completed)
3. Mark a todo as completed 
"""
def display_todos(pending=False):
    global todos 
    headers=["ID","Title"]
    rows = []
    if pending == False:
        for i in range(len(todos)):
            if i+1 in completed:
                 rows.append([i+1,todos[i]])
    else:
        for i in range(len(todos)):
            if i+1 not in completed:
                rows.append([i+1,todos[i]])
    print(tabulate(rows,headers=headers,tablefmt="grid"))
def is_validID(tid):
    if tid>=1 and tid<=len(todos):
        return True 
    else:
        return False 

todos = [] 
completed = [] # this is going to contain id's of completed todos
options = """Options: 
1. Add a Todo 
2. Display Todos
3. Mark a Todo as Complete
4. Exit
"""

while True: 
    print(options)
    choice = int(input("Enter your choice: "))
    match choice: 
        case 1:
            print("Adding Todo:")
            todo = input("Enter the Title: ")
            if len(todo) == 0: 
                print("Cannot add empty Todo. Try again...")
            else:
                todos.append(todo)
                print("Successfully added Todo")
        case 2: 
            print("Display Todos: ")
            print("1. Pending Todos\n2. Completed Todos")
            sub_choice = int(input("Enter your choice(1-2): "))
            match sub_choice:
                case 1:
                    display_todos(pending=True)
                case 2:
                    display_todos()
                case _ :
                    print("Invalid choice.")
        case 3:
            print("Mark Todo as Completed: ")
            tid = int(input("Enter the Todo ID: "))
            # 5 -> 0 , 1,2,3,4 : 1,2,3,4,5  
            if is_validID(tid):
                completed.append(tid)
            else:
                print("Todo Not found.")
        case 4:
            print("Exiting..")
            break 
    print("="*20)