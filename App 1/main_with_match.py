user_prompt = 'Enter a todo: '
# user_todos = []

while True:
    user_action = input('Type add or show or edit or complete or exit: ').lower().strip()
    match user_action:
        case 'add':
            with open('todo.txt', 'r') as file_r:
                user_todos = file_r.readlines()

            todo = input(user_prompt).capitalize().strip() + '\n'
            user_todos.append(todo)

            with open('todo.txt', 'w') as file_w:
                file_w.writelines(user_todos)

        case 'show':
            with open('todo.txt', 'r') as file_r:
                user_todos = file_r.readlines()

            print('below is the user todo list:')
            for index, items in enumerate(user_todos, 1):
                items = items.replace('\n', '')
                print(f'{index}: {items}')

        case 'edit':
            with open('todo.txt', 'r') as file_r:
                user_todos = file_r.readlines()

            print('from the below list pls provided:')
            for index, items in enumerate(user_todos, 1):
                items = items.replace('\n', '')
                print(f'{index}: {items}')

            edit_index = int(input('on which number you want to edit: ')) - 1
            new_user_todo = input(f'pls enter new todo in replacement of {user_todos[edit_index]}').capitalize().strip() + '\n'
            user_todos[edit_index] = new_user_todo

            with open('todo.txt', 'w') as file_w:
                file_w.writelines(user_todos)

        case 'exit':
            break

        case 'complete':
            with open('todo.txt', 'r') as file_r:
                user_todos = file_r.readlines()

            print('from the below list pls provided:')
            for index, items in enumerate(user_todos, 1):
                items = items.replace('\n', '')
                print(f'{index}: {items}')
            completed_todo = int(input('which number is completed: ')) - 1
            print(f'successfully removed {user_todos.pop(completed_todo)} from todos')

            with open('todo.txt', 'w') as file_w:
                file_w.writelines(user_todos)

        case _:
            print(f'pls enter proper input {user_action} is not a valid input')
    # print('value of a:', a)

with open('todo.txt', 'r') as file_r:
    user_todos = file_r.read()

print('user final todo list:\n', user_todos)
print('bye')

# print('type of user_input', type(user_todos))

# title = input('Enter title: ')
# print('length of title entered by user:', len(title))
