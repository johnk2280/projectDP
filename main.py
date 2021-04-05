import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from pd_main_window import Ui_MainWindow


class DPlane(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(DPlane, self).__init__()
        self.setupUi(self)

    def closeEvent(self, a0: QtGui.QCloseEvent):
        reply = QMessageBox.question(
            self,
            'Message',
            'Are you sure to quit?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.close()


def main():
    app = QApplication(sys.argv)
    plane = DPlane()
    plane.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
