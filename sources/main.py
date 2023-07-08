import sys
#import PySide6.QtCore
from PySide6.QtCore import QTranslator, QLocale, QCoreApplication, qDebug
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

app = QApplication(sys.argv)

translator = QTranslator()
if translator.load("./translations/autobook_ru_RU.qm"):
    QCoreApplication.installTranslator(translator)
qDebug("123")

# Prints PySide6 version
# print(PySide6.__version__)
# Prints the Qt version used to compile PySide6
# print(PySide6.QtCore.__version__)

window = MainWindow()
window.resize(1000, 800)
window.show()

sys.exit(app.exec())
