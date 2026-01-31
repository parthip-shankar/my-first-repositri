class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print("Task added ✅")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return

        for i, task in enumerate(self.tasks):
            status = "✔" if task["done"] else "✘"
            print(f"{i+1}. [{status}] {task['task']}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print("Task marked as done 🎉")
        else:
            print("Invalid task number")
