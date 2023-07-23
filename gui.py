import functions
import PySimpleGUI as sg
import time

sg.theme("DarkBlue")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")

input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todo_list(), key="todo_list", 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button =sg.Button("Exit")

window = sg.Window('My To-Do App', 
                   layout=[[clock],
                           [label], 
                           [input_box, add_button], 
                           [list_box, edit_button, complete_button],
                           [exit_button]], 
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%A %d %B, %Y %H:%M:%S"))
    match event:
        case "Add":
            todo_list = functions.get_todo_list()
            new_todo = values['todo']
            if new_todo != "":
                todo_list.append(new_todo)
                functions.write_todo_list(todo_list)
                window['todo_list'].update(values=todo_list)

        case "Edit":
            try:
                todo_to_edit = values['todo_list'][0]
                new_todo = values['todo']

                todo_list = functions.get_todo_list()
                index = todo_list.index(todo_to_edit)
                if new_todo != "":
                    todo_list[index] = new_todo
                    functions.write_todo_list(todo_list)
                    window['todo_list'].update(values=todo_list)
            except IndexError:
                sg.Popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todo_list'][0]
                todo_list = functions.get_todo_list()
                todo_list.remove(todo_to_complete)
                functions.write_todo_list(todo_list)
                window['todo_list'].update(values=todo_list)
                window['todo'].update(value="")
            except IndexError:
                sg.Popup("Please select an item first.", font=("Helvetica", 20))

        case "Exit":
            break

        case "todo_list":
            window['todo'].update(value=values['todo_list'][0])

        case sg.WIN_CLOSED:
            break

window.close()