import functions
import time

now = time.strftime("%A %d %B, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todo_list = functions.get_todo_list()

        todo_list.append(todo)

        functions.write_todo_list(todo_list)

    elif user_action.startswith("show"):
        todo_list = functions.get_todo_list()
        
        for index, todo in enumerate(todo_list):
            row = f"{index + 1}: {todo}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1

            todo_list = functions.get_todo_list()

            current_todo = todo_list[number]
            new_todo = input(f"What do you want to replace '{current_todo}' with: ")
            todo_list[number] = new_todo

            functions.write_todo_list(todo_list)
        except ValueError:
            print("Your Command is not valid, edit needs the number of a todo behind it.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todo_list = functions.get_todo_list()

            index = number - 1
            todo_to_remove = todo_list[index]
            todo_list.pop(index)

            functions.write_todo_list(todo_list)

            message = f"Todo {todo_to_remove} has been removed."
            print(message)
        except ValueError:
            print("Your Command is not valid, complete needs the number of a todo behind it.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Bye!")
