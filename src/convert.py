import settings
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QWidget,
    QLabel,
    QVBoxLayout,
    QComboBox
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

        # TITLE
        window_title: QLabel = QLabel(text=settings.title)

        title_font = window_title.font()
        title_font.setPointSize(24)

        window_title.setFont(title_font)

        # CONVERSION INPUT
        self.conversion_value: QLineEdit = QLineEdit()
        self.conversion_value.setPlaceholderText('Conversion Value')
        self.conversion_value.textChanged.connect(
            self.validate_conversion_input)

        # FROM UNIT
        from_label: QLabel = QLabel(text='From')
        from_unit: QComboBox = QComboBox()
        from_unit.addItems(['Celsius', 'Fahrenheit', 'Kelvin'])

        # TO UNIT
        to_label: QLabel = QLabel(text='To')
        to_unit: QComboBox = QComboBox()
        to_unit.addItems(['Celsius', 'Fahrenheit', 'Kelvin'])

        # FROM LAYOUT
        from_layout = QVBoxLayout()
        from_layout.addWidget(from_label)
        from_layout.addWidget(from_unit)

        from_container = QWidget()
        from_container.setLayout(from_layout)

        # TO LAYOUT
        to_layout = QVBoxLayout()
        to_layout.addWidget(to_label)
        to_layout.addWidget(to_unit)

        to_container = QWidget()
        to_container.setLayout(to_layout)

        # UNITS LAYOUT
        units_layout = QHBoxLayout()
        units_layout.addWidget(from_container)
        units_layout.addWidget(to_container)

        units_container = QWidget()
        units_container.setLayout(units_layout)

        # CONVERT BUTTON
        self.convert_button: QPushButton = QPushButton(text='Convert')
        self.convert_button.setDisabled(True)

        # RESULT TEXT
        result_text: QLabel = QLabel(text='Result: ')

        result_font = result_text.font()
        result_font.setPointSize(16)
        result_text.setFont(result_font)

        # MAIN
        main_layout = QVBoxLayout()
        main_layout.addWidget(window_title)
        main_layout.addWidget(self.conversion_value)
        main_layout.addWidget(units_container)
        main_layout.addWidget(self.convert_button)
        main_layout.addWidget(result_text)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)

    def validate_conversion_input(self):
        value: str = self.conversion_value.text().strip(' ').replace(' ', '')

        try:
            float(value)
            self.convert_button.setDisabled(False)
        except ValueError:
            self.convert_button.setDisabled(True)

        if value == '':
            self.convert_button.setDisabled(True)


app = QApplication([])

window = MainWindow()

window.setWindowTitle(settings.title)
window.setMinimumSize(settings.min_w, settings.min_h)
window.setMaximumSize(settings.max_w, settings.max_h)

window.show()

app.exec()
