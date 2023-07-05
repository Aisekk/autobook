import sys
from PyQt6.QtCore import QTranslator, QLocale, QCoreApplication, qDebug
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

app = QApplication(sys.argv)

translator = QTranslator()
if translator.load("./sources/translations/autobook_ru_RU.qm"):
    QCoreApplication.installTranslator(translator)

qDebug("123")

window = MainWindow()
window.resize(1000, 800)
window.show()

sys.exit(app.exec())
