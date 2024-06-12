import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box =sg.InputText(tooltip="Enter a Todo")
button=sg.Button("Add")
window=sg.Window('My To-Do App',layout=[[label,input_box,button]])
window.read()
window.close()
