import pyttsx3
import PySimpleGUI as sg

def speak(text, gender):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set the voice property based on the selected gender
    voices = engine.getProperty('voices')
    if gender == 'male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    # Set the speaking rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + 50)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter Text to Speak:')],
            [sg.InputText(key='-IN-')],
            [sg.Text('Select Gender:')],
            [sg.Radio('Male', 'gender', key='-MALE-'), sg.Radio('Female', 'gender', key='-FEMALE-', default=True)],
            [sg.Text('Speaking Rate:')],
            [sg.Slider(range=(0, 200), orientation='h', size=(20, 15), default_value=100, key='-RATE-')],
            [sg.Button('Speak'), sg.Button('Cancel')] ]

# Create the window
window = sg.Window('Text to Speech', layout)

# Event loop to process "events" and get the "values" of inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':   # If user closes window or clicks Cancel
        break
    if event == 'Speak': # If the user clicks Speak
        text = values['-IN-']
        gender = 'male' if values['-MALE-'] else 'female'
        rate = values['-RATE-']
        speak(text, gender)
