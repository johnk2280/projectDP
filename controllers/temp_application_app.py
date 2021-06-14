import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

from gui.pd_main_window import Ui_MainWindow
from gui.add_apps_widget_v_1_0 import Ui_AddAppsForm
from gui.edit_apps_widget import Ui_Form
from gui.firm_widget import Ui_FirmForm

from database.database import Database


class WidgetForm:
    def __init__(self, db):
        self.db = db

    def _save(self):
        data = []
        self.db.add_app(data)

    def _close(self):
        print('_close')


class Firm(QtWidgets.QWidget, Ui_FirmForm, WidgetForm):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setupUi(self)

        self.save_button.clicked.connect(self._save)
        self.cancel_button.clicked.connect(self._close)


if __name__ == '__main__':
    orm_database = Database('sqlite:///dp_base.db')
    app = QApplication(sys.argv)
    f = Firm(orm_database)
    f.show()
    sys.exit(app.exec_())
