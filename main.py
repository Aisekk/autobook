import sys
from PyQt6.QtCore import QTranslator, QLocale, QCoreApplication, qDebug
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow, QPushButton

app = QApplication(sys.argv)

translator = QTranslator()
#if translator.load(QLocale(), "autobook"_L1, "_"_L1, ":/i18n"_L1):
if translator.load("./sources/autobook_ru_RU.qm"):
   QCoreApplication.installTranslator(translator)
   qDebug("installed")

qDebug("123")

window = MainWindow()
window.resize(1000, 800)
window.show()

hello = QPushButton(QCoreApplication.translate("main", "Hello world"))
hello.show()

sys.exit(app.exec())
