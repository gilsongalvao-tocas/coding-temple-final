def display_menu():
    print("\n=== To-Do List Menu ===")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")


def add_task(tasks):
    try:
        task = input("Enter the task you want to add: ").strip()
    except EOFError:
        print("No task was entered.")
        return

    if task:
        tasks.append(task)
        print(f'"{task}" was added to your to-do list.')
    else:
        print("Task cannot be empty. Please enter a task description.")


def view_tasks(tasks):
    if not tasks:
        print("There are no tasks to view.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(tasks):
    if not tasks:
        print("There are no tasks to delete.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter the task number to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    except EOFError:
        print("No task number was entered.")
    else:
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'"{removed_task}" was deleted from your to-do list.')
        else:
            print("That task does not exist. Please choose a valid task number.")
    finally:
        print("Returning to the main menu.")


def get_menu_choice():
    try:
        choice = int(input("Choose an option from 1 to 4: "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 4.")
        return None
    except EOFError:
        print("No menu choice was entered. Quitting the application.")
        return 4
    else:
        return choice
    finally:
        print("Menu selection processed.")


def run_todo_app():
    tasks = []
    is_running = True

    print("Welcome to the Python To-Do List Application!")

    while is_running:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            print("Thank you for using the To-Do List Application. Goodbye!")
            is_running = False
        elif choice is not None:
            print("That menu option does not exist. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    run_todo_app()
