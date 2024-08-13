from PyQt5.QtWidgets import QApplication
import sys
from main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Browser")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
