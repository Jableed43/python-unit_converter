import PySimpleGUI as sg

#Layout config
layout = [[sg.Text('Text', enable_events= True, key = '-TEXT-'), sg.Spin(['item 1', 'item 2'])], 
          [sg.Button('Button', key = '-BUTTON1-')], [sg.Input(key = '-INPUT-')], [sg.Text('Test'), sg.Button('Button', key = '-BUTTON2-')]]

#Title and layout itself
window = sg.Window('Unit Converter', layout)

#It allows not to close your window when interact with a btn
#WIN_CLOSED it's an event that's triggered by closing the window
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-BUTTON1-':
      window['-TEXT-'].update(values['-INPUT-'])
    
    if event == '-BUTTON2-':
        print(values['-INPUT-'])
        
    if event == '-TEXT-':
        print('TEXT pressed')
        
window.close()