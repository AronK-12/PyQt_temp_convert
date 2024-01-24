import settings
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QPushButton,
    QLabel,
    QVBoxLayout
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print('hello, pyside.')


app = QApplication([])

window = MainWindow()

window.setWindowTitle(settings.title)
window.setMinimumSize(settings.min_w, settings.min_h)
window.setMaximumSize(settings.max_w, settings.max_h)

window.show()

app.exec()
