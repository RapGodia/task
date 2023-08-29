import json

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print("Task created successfully!")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print("Task marked as completed!")
        else:
            print("Invalid task index!")

    def list_tasks(self):
        print("Tasks:")
        for index, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{index}: {task.title} - {status}")

    def save_tasks_to_file(self, filename):
        with open(filename, 'w') as file:
            task_list = [{"title": task.title, "description": task.description, "completed": task.completed}
                         for task in self.tasks]
            json.dump(task_list, file)
            print("Tasks saved to file!")

    def load_tasks_from_file(self, filename):
        with open(filename, 'r') as file:
            task_list = json.load(file)
            self.tasks = [Task(task['title'], task['description']) for task in task_list]
            for index, task in enumerate(self.tasks):
                task.completed = task_list[index]['completed']
            print("Tasks loaded from file!")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Create Task")
        print("2. Mark Task as Completed")
        print("3. List Tasks")
        print("4. Save Tasks to File")
        print("5. Load Tasks from File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.create_task(title, description)
        elif choice == '2':
            task_manager.list_tasks()
            task_index = int(input("Enter the task index to mark as completed: "))
            task_manager.mark_task_completed(task_index)
        elif choice == '3':
            task_manager.list_tasks()
        elif choice == '4':
            filename = input("Enter the filename to save tasks: ")
            task_manager.save_tasks_to_file(filename)
        elif choice == '5':
            filename = input("Enter the filename to load tasks from: ")
            task_manager.load_tasks_from_file(filename)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
