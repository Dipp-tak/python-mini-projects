#TO DO LIST APP

task_list = []
def add_task():
    no_of_task = int(input("How many tasks do you want to add :"))
    for i in range(1,no_of_task+1):
        user_task = str(input(f"Enter task{i} --->"))
        task_list.append(user_task)

    return task_list

def view_task():
    print("Here is you task list:")
    for index,task in enumerate(task_list,1):
        print(f"{index}:{task}")

def update_task():
    view_task()
    previous_task = input("Enter the task you want to update--->")
    updated_task = input("Enter new task--->")
    if previous_task in task_list:
        index = task_list.index(previous_task)
        task_list[index] = updated_task
        print(f"{previous_task} is updated with {updated_task}")
    else:
        print(f"Sorry, I can't update the task because '{previous_task}' is not present in your task list.")


def delete_task():
    view_task()
    deleted_task =  input("Choose which task you want to delete--->")
    if deleted_task in task_list:
        user_choice = input(f"You want to delete {deleted_task}(yes/no)?\n")
        if user_choice == 'yes':
            task_list.remove(deleted_task)
            print(f"'{deleted_task}' has been successfully removed from your task list.")
        elif user_choice == 'no':
            pass
    else:
        print(f"Sorry, I can't delete the task because '{deleted_task}' is not present in your task list.")




if __name__ == '__main__':
    print("--Welcome To the Task Management App--")
    while True:
        command = input("Command list to operate the app:\nadd\nview\nupdate\ndelete\nexit\nEnter you command--->")
        if command == 'add':
            add_task()
        elif command == 'view':
            view_task()
        elif command == 'update':
            update_task()
        elif command == 'delete':
            delete_task()
        elif command == 'exit':
            break
        else:
            print("Command is not present in the command list")
