from todo import TodoApp

def main():
    app = TodoApp()

    while True:
        print("\n--- TO-DO APP ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            app.add_task(task)
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            app.view_tasks()
            index = int(input("Enter task number: "))
            app.complete_task(index - 1)
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
