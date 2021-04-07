import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from pd_main_window import Ui_MainWindow
from gui.add_apps_widget import Ui_AddAppsForm


class DPlane(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(DPlane, self).__init__()
        self.setupUi(self)

        self.add_apps_2.clicked.connect(self.add_apps)

    def add_apps(self):
        if self.verticalLayout_3.isEmpty():
            apps = AddAppForm()
            self.verticalLayout_3.addWidget(apps)

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'Message',
            'Are you sure to quit?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.close()
        else:
            event.ignore()


class AddAppForm(QtWidgets.QWidget, Ui_AddAppsForm):
    def __init__(self):
        super(AddAppForm, self).__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    plane = DPlane()
    plane.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
