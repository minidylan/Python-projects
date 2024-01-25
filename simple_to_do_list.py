# To do list: 

def add_task(tasks, task):
    # Add the task to the tasks list
    tasks.append(task)



def display_tasks(tasks):
    # Print all tasks
    for task in tasks:
        print(task)


def remove_task(tasks, task_index):
    # Remove a task from the list based on the task index
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    else:
        print("Invalid task index. ")


def main():
    tasks = []

    # 
    while True:
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")


        choice = input("Enter your choice: ")
        

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please Try again")

if __name__== "__main__":
    main() 
