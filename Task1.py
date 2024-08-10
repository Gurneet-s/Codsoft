# To-Do List

def add_task(tasks):
  task = input("Enter a new task: ")
  tasks.append(task)

def delete_task(tasks):
  task_number = int(input("Enter the task number to delete: "))
  try:
      del tasks[task_number - 1]
  except IndexError:
      print("Invalid task number.")

def update_task(tasks):
  task_number = int(input("Enter the task number to update: "))
  new_task = input("Enter the new task: ")
  try:
      tasks[task_number - 1] = new_task
  except IndexError:
      print("Invalid task number.")

def display_tasks(tasks):
  print("To-Do List:")
  for i, task in enumerate(tasks, start=1):
      print(f"{i}. {task}")

def main():
  tasks = []

  while True:
      print("\nOptions:")
      print("1. Add task")
      print("2. Delete task")
      print("3. Update task")
      print("4. Display tasks")
      print("5. Quit")

      choice = input("Enter your choice: ")

      if choice == "1":
          add_task(tasks)
      elif choice == "2":
          delete_task(tasks)
      elif choice == "3":
          update_task(tasks)
      elif choice == "4":
          display_tasks(tasks)
      elif choice == "5":
          break
      else:
          print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()