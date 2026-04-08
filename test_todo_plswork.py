def to_do_list(input_func=input, print_func=print):
    tasks = []

    while True:
        print_func("\n View To-do List Menu:")
        print_func("1. View Tasks")
        print_func("2. Add Task")
        print_func("3. Mark Task as done")
        print_func("4. Exit")

        choice = input_func("Choose one of the options above").strip()

        if choice == "1":
            if tasks:
                print_func("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print_func(f"{i}. {task}")
            else:
                print_func("No tasks added yet.")
        elif choice == "2":
            task = input_func("Enter a task: ").strip()
            tasks.append(task)
            print_func(f"{task} has been added to the list")
        elif choice == "3":
            task_num_str = input_func("Enter the task number to remove: ").strip()
            if task_num_str.isdigit():
                task_num = int(task_num_str)
                if 0 < task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print_func(f"Task '{removed_task}' removed.")
                else:
                    print_func("Invalid task number, please type a number greater than 0")
            else:
                print_func("Please enter a valid number.")
        elif choice == "4":
            print_func("Goodbye!")
            break
        else:
            print_func("Invalid function")


def test_to_do_list():
    # Sequence of simulated user inputs
    inputs = iter([
        '2', 'Buy milk',     # Add "Buy milk"
        '1',                 # View tasks
        '2', 'Read book',    # Add "Read book"
        '1',                 # View tasks
        '3', '1',            # Remove task 1 ("Buy milk")
        '1',                 # View tasks again
        '4'                  # Exit
    ])

    # List to capture printed output
    outputs = []

    # Mock input function
    def mock_input(prompt):
        return next(inputs)

    # Mock print function
    def mock_print(message):
        outputs.append(message)

    # Run the to_do_list with mocked input/output
    to_do_list(input_func=mock_input, print_func=mock_print)

    # Perform assertions
    assert "Buy milk has been added to the list" in outputs
    assert "Your tasks:" in outputs
    assert "Read book has been added to the list" in outputs
    assert "Task 'Buy milk' removed." in outputs
    assert "Goodbye!" in outputs

    # Optional: print the outputs for visual confirmation
    for line in outputs:
        print(line)

if __name__ == "__main__":
    # Run the test when executing the script
    test_to_do_list()