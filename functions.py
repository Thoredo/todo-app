FILEPATH = "todo-list.txt"


def get_todo_list(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    todo_list_local = [todo.strip("\n") for todo in todo_list_local]
    return todo_list_local


def write_todo_list(todos, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    todos = [arg + "\n" for arg in todos]
    with open(filepath, 'w') as file:
            file.writelines(todos)
