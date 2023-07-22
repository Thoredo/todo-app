import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', 
                   layout=[[label], [input_box, add_button]], 
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = functions.get_todo_list()
            new_todo = values['todo'] + "\n"
            todo_list.append(new_todo)
            functions.write_todo_list(todo_list)
        case sg.WIN_CLOSED:
            break

window.close()