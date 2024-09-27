import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl, QCoreApplication, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from threading import Thread
from app import app


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://localhost:5000"))
        self.setCentralWidget(self.browser)
        self.showMaximized()


def run_flask():
    app.run()


if __name__ == '__main__':
    # Run flask in the background
    thread = Thread(target=run_flask)
    thread.start()

    # Suitable to High DPI display
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

    # Rub application
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("CMU Move-In Hub")
    main = MainWindow()
    app.exec_()
