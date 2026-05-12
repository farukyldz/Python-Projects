tasks = []

while True:
    print("\n 1- Add Task")
    print("2- Delete Task")
    print("3- List Tasks")
    print("4- Exit")

    choise = input("your choise: ")

    if choise== "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("task added.")
        
        # --- Let’s display the list after the addition has been made ---
        print("\nYour Current Task List:")
        for i, g in enumerate(tasks, start=1):
            print(f"{i} - {g}")
        # --------------------------------------------------

    elif choise == "2":
        task = input("Enter the task to delete: ")
        if task in tasks:
            tasks.remove(task)
            print("The task has been deleted.")
        else:
            print("No task found.")
            
    elif choise == "3":
        print("\nTasks:")
        if not tasks: 
            print("The list is currently empty.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, "-", task)
                
    elif choise == "4":
        print("The programme has been cancelled.")
        break
    else:
        print("Invalid selection.")
        
