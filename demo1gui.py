import PySimpleGUI as sg
print(sg.version, sg)
sg.change_look_and_feel('Dark Blue 3')

layout = [  [sg.Text('My Window')],
            [sg.Input(key='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
            [sg.Button('Go'), sg.B('Nothing'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout, alpha_channel=0, finalize=True)

window.set_alpha(1)
i = 0
while True:             # Event Loop
    event, values = window.read(timeout=200)
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Go':
        sg.show_debugger_window()
        sg.show_debugger_popout_window((0,0))
    i += 1
window.close()