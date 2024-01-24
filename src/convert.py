import settings
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QPushButton,
    QWidget,
    QLabel,
    QVBoxLayout
)

#   TODO: layout
#       - [X] title text
#       - [ ] value input validation text
#       - [ ] temperature value input
#       - [ ] from_unit dropdow
#       - [ ] to_unit dropdow
#       - [ ] convert button
#       - [ ] result text

#   TODO: functionality
#       - [ ] checking if input is numberic (float or int, either is okay)
#       - [ ] get conversion method based on from_unit and to_unit
#       - [ ] converting input if it's valid
#       - [ ] update input validation text as user types temperature value
#       - [ ] display converted value upon succesful conversion
#       - [ ] display error message upon unsuccesful conversion

#   TODO: conversion methods
#       - [ ] Celsius to Fahrenheit
#       - [ ] Celsius to Kelvin
#       - [ ] Fahrenheit to Celsius
#       - [ ] Fahrenheit to Kelvin
#       - [ ] Kelvin to Celsius
#       - [ ] Kelvin to Fahrenheit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


# START OF TITLE SETUP
        window_title: QLabel = QLabel(text=settings.title)

        title_font = window_title.font()
        title_font.setPointSize(24)

        window_title.setFont(title_font)
# END OF TITLE SETUP


# START OF LAYOUT SETUP
        layout = QVBoxLayout()
        layout.addWidget(window_title)

        container = QWidget()
        container.setLayout(layout)
# END OF LAYOUT SETUP

        self.setCentralWidget(container)


app = QApplication([])

window = MainWindow()

window.setWindowTitle(settings.title)
window.setMinimumSize(settings.min_w, settings.min_h)
window.setMaximumSize(settings.max_w, settings.max_h)

window.show()

app.exec()
