import functions as fun
import PySimpleGUI as pygui

label = pygui.Text("Type a to-do:")
input_box = pygui.InputText(tooltip="Enter a to-do", key="todo")
add_button = pygui.Button("Add in list")

list_box = pygui.Listbox(values=fun.get_todos(),
                         key="todo_items",
                         enable_events=True,
                         size=[45, 10])
edit_button = pygui.Button("Edit list")

exit_button = pygui.Button("EXIT")

window = pygui.Window('My To-Do App',
                      layout=[[label],
                              [input_box, add_button],
                              [list_box, edit_button],
                              [exit_button]],
                      font=('Comic Sans MS', 12))

while True:
    event, value = window.read()
    print(window.read())
    # print('hello')
    # print('event:', event)
    # print('value:', value)

    match event:
        case 'Add in list':
            new_todo = value["todo"] + '\n'

            user_todos = fun.get_todos()
            user_todos.append(new_todo)

            fun.write_todos(user_todos)
            window["todo_items"].update(values=user_todos)

        case 'Edit list':
            edited_todo = value["todo_items"][0]
            new_todo = value["todo"] + '\n'

            user_todos = fun.get_todos()
            index = user_todos.index(edited_todo)
            user_todos[index] = new_todo

            fun.write_todos(user_todos)
            window["todo_items"].update(values=user_todos)

        case 'todo_items':
            window['todo'].update(value=value["todo_items"][0])

        case pygui.WINDOW_CLOSED | 'EXIT':
            break


window.close()
