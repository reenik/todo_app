import functions as fun
import PySimpleGUI as pygui

label = pygui.Text("Type a to-do:")
input_box = pygui.InputText(tooltip="Enter a to-do")
add_button = pygui.Button("Add in list")


window = pygui.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
print('hello')
window.close()