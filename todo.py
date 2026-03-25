import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

class Task:
    def __init__(self, title, priority="Low", due_date=None, completed=False):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date,
            "completed": self.completed
        }

class TodoApp:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(FILE_NAME):
            return []
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return [Task(**item) for item in data]

    def save_tasks(self):
        with open(FILE_NAME, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def show_tasks(self):
        if not self.tasks:
            print("\nNo tasks available")
            return

        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks):
            status = "✔" if task.completed else "✘"
            print(f"{i+1}. [{status}] {task.title} | Priority: {task.priority} | Due: {task.due_date}")

    def add_task(self):
        title = input("Enter task: ")
        priority = input("Enter priority (Low/Medium/High): ")
        due_date = input("Enter due date (YYYY-MM-DD): ")

        # Validate date
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except:
            print("Invalid date format!")
            return

        task = Task(title, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()
        print("Task added!")

    def delete_task(self):
        self.show_tasks()
        try:
            num = int(input("Enter task number to delete: "))
            self.tasks.pop(num - 1)
            self.save_tasks()
            print("Task deleted!")
        except:
            print("Invalid input")

    def mark_complete(self):
        self.show_tasks()
        try:
            num = int(input("Enter task number to mark complete: "))
            self.tasks[num - 1].completed = True
            self.save_tasks()
            print("Task marked as completed!")
        except:
            print("Invalid input")

    def search_task(self):
        keyword = input("Enter keyword to search: ").lower()
        results = [t for t in self.tasks if keyword in t.title.lower()]

        if not results:
            print("No matching tasks found")
        else:
            print("\nSearch Results:")
            for task in results:
                print(f"- {task.title} (Priority: {task.priority})")

    def run(self):
        while True:
            print("\n--- ADVANCED TO-DO APP ---")
            print("1. Show Tasks")
            print("2. Add Task")
            print("3. Delete Task")
            print("4. Mark Complete")
            print("5. Search Task")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.show_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.mark_complete()
            elif choice == '5':
                self.search_task()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    app = TodoApp()
    app.run()