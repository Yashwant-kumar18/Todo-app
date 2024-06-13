import PySimpleGUI as sg
import functionsA1


label = sg.Text("Type in a To-Do")
input_box =sg.InputText(tooltip="Enter a Todo",key="Todo")
button=sg.Button("Add")
list_box=sg.Listbox(values=functionsA1.get_todos(),key='todos',
                    enable_events=True, size=[45,10])
edit_button=sg.Button("Edit")
window=sg.Window('My To-Do App',
                 layout=[[label],[input_box,button],[list_box,edit_button]],
                 font=('Helvetica', 10))

while True:
    event, value=window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos=functionsA1.get_todos()
            new_todo=value['Todo'] + "\n"
            todos.append(new_todo)
            functionsA1.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = value['todos'][0]
            new_todo=value['Todo'] + "\n"

            todos=functionsA1.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            functionsA1.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['Todo'].update(value=value['todos'][0])
        case sg.WINDOW_CLOSED:
            break
window.close()
