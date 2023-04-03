import PySimpleGUI as sg
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set default voice type
voice_id = 'english+f3'

# Define GUI layout
layout = [
    [sg.Text('Enter text to convert to speech:')],
    [sg.Input(key='input')],
    [sg.Text('Select a voice type:')],
    [sg.OptionMenu(values=engine.getProperty('voices'), key='voice')],
    [sg.Text('Volume:')],
    [sg.Slider(range=(0, 100), orientation='h', size=(20, 15), default_value=50, key='volume')],
    [sg.Text('Speed:')],
    [sg.Slider(range=(0, 500), orientation='h', size=(20, 15), default_value=200, key='speed')],
    [sg.Button('Speak'), sg.Button('Exit')]
]

# Create GUI window
window = sg.Window('SpeakEasy', layout)

# Define function to speak text
def speak(text):
    # Set voice type
    engine.setProperty('voice', voice_id)
    
    # Set volume and speed
    volume = window['volume'].get() / 100
    speed = window['speed'].get() / 100
    engine.setProperty('volume', volume)
    engine.setProperty('rate', speed * 200)
    
    # Speak text
    engine.say(text)
    engine.runAndWait()

# Define event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Speak':
        # Get input text
        text = values['input']
        
        # Get selected voice type
        voice_id = values['voice']
        
        # Speak text
        speak(text)

# Close GUI window
window.close()
