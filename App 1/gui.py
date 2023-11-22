import functions as fun
import PySimpleGUI as pygui
import time

pygui.theme("DarkTanBlue")
# label_clock = pygui.Text("", key="clock")
label = pygui.Text("Type a to-do:")
input_box = pygui.InputText(tooltip="Enter a to-do",
                            key="todo")
add_button = pygui.Button("Add in list")

list_box = pygui.Listbox(values=fun.get_todos(),
                         key="todo_items",
                         enable_events=True,
                         size=[45, 9])
edit_button = pygui.Button("Edit list")

complete_button = pygui.Button("Completed")
exit_button = pygui.Button("EXIT")
output = pygui.Text(key="output")

window = pygui.Window('My To-Do App',
                      layout=[[label],
                              [input_box, add_button],
                              [list_box, edit_button, complete_button],
                              [exit_button, output]],
                      font=('Comic Sans MS', 12))

while True:
    event, value = window.read()
    print(window.read())
    # window["clock"].update(value=time.strftime('%d %B, %Y %H:%M:%S'))
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
            window['todo'].update(value="")

        case 'Edit list':
            try:
                edited_todo = value["todo_items"][0]
                new_todo = value["todo"] + '\n'

                user_todos = fun.get_todos()
                index = user_todos.index(edited_todo)
                user_todos[index] = new_todo

                fun.write_todos(user_todos)
                window["todo_items"].update(values=user_todos)
                window['todo'].update(value="")

            except IndexError:
                pygui.popup("oops 😅 you didn't selected anything to edit.\n"
                            "Pls select an item from list to edit.",
                            font=('Comic Sans MS', 14))

        case 'Completed':
            try:
                completed_todo = value["todo_items"][0]

                user_todos = fun.get_todos()

                user_todos.remove(completed_todo)

                fun.write_todos(user_todos)

                completed_todo = completed_todo.strip('\n')

                window['output'].update(value=f"completed '{completed_todo}', hence removed from list. 😊",
                                        text_color="black")
                window["todo_items"].update(values=user_todos)
                window['todo'].update(value="")

            except IndexError:
                pygui.popup("oops 😅 you didn't selected anything to be completed.\n"
                            "Pls select an item from list to complete.",
                            font=('Comic Sans MS', 14))

        case 'todo_items':
            window['todo'].update(value=value["todo_items"][0].strip('\n'))

        case pygui.WINDOW_CLOSED | 'EXIT':
            break


window.close()
