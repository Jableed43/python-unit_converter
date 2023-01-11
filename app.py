import PySimpleGUI as sg

#Layout config
layout = [
    [sg.Input(key = '-INPUT-'),
     sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key = '-UNITS-'),
     sg.Button('Convert', key = '-CONVERT-')
    ],
        [sg.Text('Output', key = '-OUTPUT-')]
]

#Title and layout itself
window = sg.Window('Unit Converter', layout)

#It allows not to close your window when interact with a btn
#WIN_CLOSED it's an event that's triggered by closing the window
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        #Check if value is numeric, by the way it's a string type
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    #float() is used because input_value is a string type
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} km are {output} miles'
                case 'kg to pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} kg are {output} pounds'
                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} seconds are {output} minutes'
        #Updates output with value 
            window['-OUTPUT-'].update(output_string)
        #In case you don't send a number
        else:
            window['-OUTPUT-'].update('Please enter a number')

window.close()