import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

from gui.pd_main_window import Ui_MainWindow
from gui.add_apps_widget_v_1_0 import Ui_AddAppsForm
from gui.edit_apps_widget import Ui_Form

from database.database import Database


class DPlane(QMainWindow, Ui_MainWindow):
    def __init__(self, db: Database, parent=None):
        super(DPlane, self).__init__(parent)
        self.setupUi(self)

        self.db = db
        """ Список виджетов для динамической смены. """
        self.widget_list = []

        """ Виджет добавления заявок. """
        # self.add_apps_form = AddAppsForm(self.db)

        """ Виджет редактирования заявок. """
        # self.edit_apps_form = EditAppsForm()

        """ Виджет просмотра заявок, распечатки и экспорта в .csv/.xml.  """
        self.view_apps_form = None

        """ Добавление виджетов в список. """
        # self.widget_list.append(self.add_apps_form)
        # self.widget_list.append(self.edit_apps_form)
        # self.widget_list.append(self.view_apps_form)

        """ Проброс сигналов от кнопок к слотам. """
        self.add_apps_btn.clicked.connect(self.insert_add_apps_widget)
        self.edit_apps_btn.clicked.connect(self.insert_edit_apps_widget)
        self.view_apps_btn.clicked.connect(self.insert_view_apps_widget)

    def insert_add_apps_widget(self):
        """ Вставка виджета добавления заявок. """
        if self.verticalLayout_3.isEmpty():
            try:
                self.verticalLayout_3.addWidget(self.widget_list[0])
            except IndexError:
                pass

    def insert_edit_apps_widget(self):
        """ Вставка виджета редактиования заявок. """
        if self.verticalLayout_3.isEmpty():
            try:
                self.verticalLayout_3.addWidget(self.widget_list[1])
            except IndexError:
                pass

    def insert_view_apps_widget(self):
        """ Вставка виджета просмотра заявок. """
        pass

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

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
