tasks = []

while True:
    print("\n1. Add Task")
    print("2. Run Tasks")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        priority = input("Enter priority (high/low): ")
        ready = input("Is the task ready? (yes/no): ")

        if priority == "high" or ready == "yes":
            tasks.append(task)
            print("Task added.")
        else:
            print("Task does not meet the execution condition.")

    elif choice == "2":
        if tasks:
            print("\nRunning Tasks:")

            for task in tasks:
                print("Executing:", task)

            tasks.clear()
        else:
            print("No tasks available.")

    elif choice == "3":
        if tasks:
            print("\nScheduled Tasks:")
            for task in tasks:
                print(task)
        else:
            print("No tasks scheduled.")

    elif choice == "4":
        print("Exiting Task Scheduler.")
        break

    else:
        print("Invalid choice.")