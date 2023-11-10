import functions as fun
import PySimpleGUI as pygui

label = pygui.Text("Type a to-do:")
input_box = pygui.InputText(tooltip="Enter a to-do", key="todo")
add_button = pygui.Button("Add in list")

exit_button = pygui.Button("EXIT")

window = pygui.Window('My To-Do App',
                      layout=[[label], [input_box, add_button], [exit_button]],
                      font=('Comic Sans MS', 12))

while True:
    event, value = window.read()
    # print('hello')
    # print('event:', event)
    # print('value:', value)

    match event:
        case 'Add in list':
            new_todo = value['todo'] + '\n'

            user_todos = fun.get_todos()
            user_todos.append(new_todo)

            fun.write_todos(user_todos)

        case pygui.WINDOW_CLOSED | 'EXIT':
            break


window.close()
