# Initialize an empty to-do list
todo_list = []

# Main loop
while True:
    # Display menu options
    print("\nOptions:")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        todo_list.append(task)
        print("Task added to the to-do list.")
    elif choice == "2":
        if todo_list:
            print("To-Do List:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
        else:
            print("To-Do List is empty.")
    elif choice == "3":
        print("Exiting the to-do list application.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
