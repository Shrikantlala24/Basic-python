tasks = []

def add_task(task_name): 
    # To add task
    tasks.append(task_name)
    print(" ⛳ task added ⛳")

def view():
    # To display all the tasks
    print("--- 🧮 Tasks 🧮 ---")
    if tasks:
        for i, t in enumerate(tasks, start = 1) :
            print(f"{i}. {t}")
    else:
        print("No task")

def complete(task_index):
    # To complete the task
    if 1 <= task_index <= len(tasks):
        com_task = tasks.pop(task_index-1)
        print(f"{com_task} ✅ task completed ✅")
    else:
        print("Task not available")



if __name__ == "__main__" :
    while(True):
        print("\n-- Select the options 🔢 --")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Quit ")

        try :
            choice = int(input("Option : "))
            if choice == 1:
                task = input("Enter task name : ")
                add_task(task)
            elif choice == 2:
                view()
            elif choice == 3:
                index = int(input("Enter the Task no. : "))
                complete(index)
            elif choice == 4:
                print("--- See you later! ✌️Goodbye ---")
                break
            else:
                print("Invalid Option number")
        except ValueError:
            print("Please enter a valid number")

        