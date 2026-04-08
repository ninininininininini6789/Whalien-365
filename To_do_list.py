def to_do_list():
    tasks = []

    while True:
        print("\n View To-do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as done")
        print("4. Exit")

        choice=input("Choose one of the options above").strip()

        if choice == "1":
            if tasks:
                print("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks added yet. ")

        elif choice == "2":
            task = input ("Enter a task: ").strip()
            tasks.append(task)
            print(f"{task} has been added to the list")
        
        elif choice == "3":
            task_num = int(input("Enter the task number to remove:"))
            if 0 < task_num <= len(tasks):
                removed_tasks = tasks.pop(task_num - 1)
                print(f"Task '{removed_tasks}' removed.")
            else:
                print("Invalid task number, please type a number greater than 0")
        
        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid function")

to_do_list()
