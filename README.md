# SENG-207-Course-Project-2

## Introduction:

This repository contains two Python applications developed using the PySimpleGUI library, which is a Python module for creating graphical user interfaces (GUIs) quickly and easily. The two applications included are a Text to Speech App and a QR Code Generator App.

## Text to Speech App:

The Text to Speech App is an application that converts text input into spoken words using the pyttsx3 library. The app has a simple and user-friendly interface, with an input text box, a Speak button, and a drop-down menu for selecting the voice type (male or female). The app also has options to adjust the volume and speed of the spoken words. This application can benefit individuals with visual impairments or those who prefer an audio-based interface.

## QR Code Generator App:

The QR Code Generator App is an application that converts text input into a QR code image using the qrcode library. The app has a simple and user-friendly interface, with an input text box and a Create button. The app also has options to customize the size and color of the generated QR code image. This application can be useful for a variety of applications, such as generating QR codes for product information or event invitations.

## Installation:

To use these applications, you must have Python 3 installed on your system. You can download the latest version of Python from the official Python website. You also need to install the PySimpleGUI, pyttsx3, and qrcode libraries using pip. To install these libraries, open your terminal or command prompt and run the following commands:

```
pip install PySimpleGUI
pip install pyttsx3
pip install qrcode
```

## Running the Applications:

To run these applications, navigate to the directory where the Python files are located and run the command:

```
python app_name.py
Replace app_name with the name of the Python file you want to run (either text_to_speech_app.py or qr_code_generator_app.py).
```

## Packaging the Applications:

To package these applications into standalone executables, you can use the PyInstaller library. First, install PyInstaller using pip:

```
pip install pyinstaller
Next, navigate to the directory where the Python files are located and run the following command:
pyinstaller --onefile app_name.py
Replace app_name with the name of the Python file you want to package (either text_to_speech_app.py or qr_code_generator_app.py). This command will create a "dist" folder containing the packaged executable.
```

## Contributing:

If you have any suggestions or improvements for these applications, feel free to submit a pull request. Any contributions are welcome and appreciated.


## Conclusion:

These applications are a demonstration of the practical applications of Python in solving real-world problems. By developing these applications, we have applied fundamental concepts in Python, such as functions, procedural programming, and object-oriented programming, as well as relevant Python libraries to create desktop applications. We hope these applications can be useful to others and inspire further exploration into Python programming.
