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


class UnitConversionWidget(QWidget):
    def __init__(self, name: str, units: list) -> QWidget:
        super().__init__()

        label: QLabel = QLabel(text=name)
        self.unit: QComboBox = QComboBox()
        self.unit.addItems(units)

        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.unit)

        self.container: QWidget = QWidget()
        self.container.setLayout(layout)

    def get_widget(self) -> QWidget:
        return self.container


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.units: list = ['celsius', 'fahrenheit', 'kelvin']

        # TITLE
        window_title: QLabel = QLabel(text=settings.title)

        title_font = window_title.font()
        title_font.setPointSize(24)

        window_title.setFont(title_font)

        # CONVERSION INPUT
        self.conversion_value: QLineEdit = QLineEdit()
        self.conversion_value.setPlaceholderText('Conversion Value')
        self.conversion_value.textChanged.connect(
            self.validate_conversion_input
        )

        self.to_conversion: UnitConversionWidget = UnitConversionWidget(
            'To', self.units
        )

        from_conversion: UnitConversionWidget = UnitConversionWidget(
            'From', self.units
        )
        from_conversion.unit.currentIndexChanged.connect(
            lambda check: self.disable_same_conversion_units(
                from_conversion, self.to_conversion)
        )

        self.disable_same_conversion_units(from_conversion, self.to_conversion)

        # CONVERT BUTTON
        self.convert_button: QPushButton = QPushButton(text='Convert')
        self.convert_button.setDisabled(True)
        self.convert_button.clicked.connect(self.try_convert)

        # RESULT TEXT
        result_text: QLabel = QLabel(text='Result: ')

        result_font = result_text.font()
        result_font.setPointSize(16)
        result_text.setFont(result_font)

        # MAIN
        main_layout = QVBoxLayout()
        main_layout.addWidget(window_title)

        main_layout.addWidget(self.conversion_value)

        main_layout.addWidget(from_conversion.get_widget())
        main_layout.addWidget(self.to_conversion.get_widget())

        main_layout.addWidget(self.convert_button)

        main_layout.addWidget(result_text)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)

    def validate_conversion_input(self):
        value: str = self.conversion_value.text().replace(' ', '')

        try:
            float(value)
            self.convert_button.setDisabled(False)
        except ValueError:
            self.convert_button.setDisabled(True)

        if value == '':
            self.convert_button.setDisabled(True)

    def disable_same_conversion_units(self, from_unit: UnitConversionWidget, to_unit: UnitConversionWidget):
        from_index: int = from_unit.unit.currentIndex()
        to_index: int = to_unit.unit.currentIndex()

        max_index: int = to_unit.unit.count()

        if from_index == to_index:
            if to_index + 1 >= max_index:
                self.to_conversion.unit.setCurrentIndex(0)
            else:
                self.to_conversion.unit.setCurrentIndex(to_index + 1)

    def try_convert(self):
        print('converting...')
        pass


app = QApplication([])

window = MainWindow()

window.setWindowTitle(settings.title)
window.setMinimumSize(settings.width, settings.height)

window.show()

app.exec()
