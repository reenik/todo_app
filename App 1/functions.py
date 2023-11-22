import os

FILE_PATH = 'todo.txt'

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as file_write:
        pass

def get_todos(filepath=FILE_PATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_r:
        local_user_todos = file_r.readlines()

    return local_user_todos


def write_todos(todos, filepath=FILE_PATH):
    """ Write a to-do item list in the text file."""
    with open(filepath, 'w') as file_w:
        local_user_todos = file_w.writelines(todos)


print("Called function:", __name__)

if __name__ == '__main__':
    print('hello from functions')
    print(get_todos())
