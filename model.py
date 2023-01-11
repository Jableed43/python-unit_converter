import PySimpleGUI as sg

#Layout config
layout = [[]]

#Title and layout itself
window = sg.Window('Unit Converter', layout)

#It allows not to close your window when interact with a btn
#WIN_CLOSED it's an event that's triggered by closing the window
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
window.close()