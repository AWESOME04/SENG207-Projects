import io
import qrcode
from PySimpleGUI import Window, Input, Button, Column, Image, popup, WIN_CLOSED, Combo, Text


class MainWindow(Window):
    def __init__(self) -> None:
        # Define the window's contents
        self.layout = [
            [Input()],     # Text input field for entering data to encode in the QR code
            [Button('Create')],  # Button to generate the QR code
            [Column([[Image(key='-QR-')]], size=(300, 300), justification='center')],  # Container for displaying the QR code
            [Text('Fill Color: '), Combo(['Black', 'White', 'Red', 'Green', 'Blue'], key='-FILL-', default_value='Black')],  # Dropdown for selecting the fill color of the QR code
            [Text('Background Color: '), Combo(['White', 'Black', 'Red', 'Green', 'Blue'], key='-BACK-', default_value='White')],  # Dropdown for selecting the background color of the QR code
            [Text('Border Size: '), Combo(['1', '2', '3', '4', '5'], key='-BORDER-', default_value='4')],  # Dropdown for selecting the border size of the QR code
            [Text('Box Size: '), Combo(['5', '6', '7', '8', '9'], key='-BOX-', default_value='7')],  # Dropdown for selecting the box size of the QR code

        ]
        # Initialize the Window class
        super().__init__('QR Code Generator', self.layout)

    def genCode(self, data, fill_color, back_color, border_size, box_size):
        "Generates the QR code with the specified parameters"
        qr = qrcode.QRCode(version=1, box_size=int(box_size), border=int(border_size))
        qr.add_data(data)
        qr.make(fit=True)
        self.img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Make the image look nicer
        self.img = self.img.resize((300, 300))
        self.img = self.img.convert('RGB')

        # Display the QR code
        self.showCode()

    def showCode(self):
        "Displays the generated QR code"
        with io.BytesIO() as buffer:
        # Save the image data to a bytes buffer
            self.img.save(buffer, format='PNG')
            img_bytes = buffer.getvalue()
            self['-QR-'].update(data=img_bytes)

    def removeCode(self):
        "Removes the QR code from the container"
        self['-QR-'].update(data=b'')


if __name__ == '__main__':
    # Create the window
    window = MainWindow()
    while True:
        # Interact with the Window
        event, values = window.read()
        if event == WIN_CLOSED or event == 'Exit':
            # Finish up by removing from the screen
            window.close()
            # Break from the loop and end the program
            break
        elif values[0]:
            # Generate the QR code
            window.genCode(values[0], values['-FILL-'], values['-BACK-'], values['-BORDER-'], values['-BOX-'])
        else: 
            # Notify the user of an empty textfield
            popup("Error", "Textfield cannot be empty") 
            window.removeCode()
