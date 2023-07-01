import sys
from PyQt6.QtWidgets import QApplication
from ui.MainWindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.resize(1000, 800)
window.show()

app.exec()
