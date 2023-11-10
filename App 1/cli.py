# from functions import get_todos, write_todos
import functions as fun
import time

curr_time = time.strftime('%d %B, %Y %H:%M:%S')
print('Current Time:', curr_time)

while True:
    user_action = input('Type add or show or edit or complete or exit: ').lower().strip()

    # add
    if user_action.startswith('add'):
        todo = user_action[4:].capitalize() + '\n'

        user_todos = fun.get_todos()

        user_todos.append(todo)

        fun.write_todos(user_todos)

    # show
    elif user_action.startswith('show'):
        user_todos = fun.get_todos()

        print('below is the user todo list:')
        for index, items in enumerate(user_todos, 1):
            items = items.replace('\n', '')
            print(f'{index}: {items}')

    # edit
    elif user_action.startswith('edit'):
        try:
            edit_index = int(user_action[5:]) - 1

            user_todos = fun.get_todos()

            new_user_todo = input(f'pls enter a new todo in replacement of:\n').capitalize().strip() + '\n'
            user_todos[edit_index] = new_user_todo

            fun.write_todos(user_todos)

        except ValueError:
            print('wrong command entered, pls enter again')

    # complete
    elif user_action.startswith('complete'):
        try:
            completed_todo = int(user_action[9:]) - 1

            user_todos = fun.get_todos()

            removed_todo = user_todos.pop(completed_todo).strip('\n')
            print(f'successfully removed {removed_todo} from todos')

            fun.write_todos(todos=user_todos)

        except IndexError:
            print('There is no item on that number, pls try again.')

    elif user_action.startswith('exit'):
        break

    else:
        print(f'{user_action.split()[0]} does not exist')

print('bye')
