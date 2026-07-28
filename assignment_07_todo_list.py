                                                                                                                                                                                                                                                     # =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def add_task(tasks):
    task = input("Enter task description: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        print(f'Successfully added: "{task}"')
    else:
        print("Error: Task description cannot be left blank.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found in your list.")
    else:
        print("\nCurrent Task List:")
        for idx, item in enumerate(tasks, start=1):
            status = "✓" if item["completed"] else " "
            print(f"{idx}. [{status}] {item['task']}")
        print()


def delete_task(tasks):
    if not tasks:
        print("Your list is already empty. Nothing to delete.")
        return

    view_tasks(tasks)
    try:
        choice = int(input("Enter the task number you want to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f'Deleted task: "{removed["task"]}"')
        else:
            print("Error: That task number does not exist.")
    except ValueError:
        print("Error: Please enter a valid numerical digit.")


def main():
    tasks = []
    print("Welcome to your interactive Console To-Do List!")

    while True:
        print("\n==============================")
        print("      TO-DO LIST MENU")
        print("==============================")
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. Delete a Task")
        print("4. Quit")

        selection = input("Enter your choice (1-4): ").strip()

        if selection == '1':
            add_task(tasks)
        elif selection == '2':
            view_tasks(tasks)
        elif selection == '3':
            delete_task(tasks)
        elif selection == '4':
            print("Thank you for using the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid input! Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
