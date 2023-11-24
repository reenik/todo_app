import streamlit as st
import functions as fun
import time

curr_time = time.strftime('%d %B, %Y %H:%M:%S')

user_todos = fun.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    user_todos.append(new_todo)
    fun.write_todos(user_todos)
    # print(new_todo)


st.title("My Todo App")
st.header("This is my Todo App")

st.write("This app helps to remember the work needs to be done.")
st.write('Current Time:', curr_time)


for index, todo in enumerate(user_todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        user_todos.pop(index)
        fun.write_todos(user_todos)

        del st.session_state[todo]
        st.rerun()

st.text_input(label="ABC", placeholder="add a new todo here...",
              on_change=add_todo, key="new_todo", label_visibility="hidden")

