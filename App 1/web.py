import streamlit as st
import functions as fun
import time

curr_time = time.strftime('%d %B, %Y %H:%M:%S')

st.title("My Todo App")
st.header("This is my Todo App")

st.write("This app helps to remember the work needs to be done.")
st.write('Current Time:', curr_time)

user_todos = fun.get_todos()
for todo in user_todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="add a new todo here...")