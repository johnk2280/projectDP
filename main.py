import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

from pd_main_window import Ui_MainWindow
from gui.add_apps_widget import Ui_AddAppsForm
from gui.edit_apps_widget import Ui_Form


class DPlane(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DPlane, self).__init__(parent)
        self.setupUi(self)

        """ Список виджетов для динамической смены. """
        self.widget_list = []

        """ Виджет добавления заявок. """
        self.apps_form = AddAppsForm()
        self.apps_form.add_button.clicked.connect(self.add_application)
        self.apps_form.save_button.clicked.connect(self.save_apps)
        self.apps_form.cancel_button.clicked.connect(self.close_add_apps_widget)
        print(self.apps_form)

        """ Виджет редактирования заявок. """
        self.edit_form = EditAppsForm()

        """ Виджет просмотра заявок, распечатки и экспорта в .csv/.xml.  """
        self.view_form = None

        """ Добавление виджетов в список. """
        self.widget_lis.append(self.apps_form)
        self.widget_lis.append(self.edit_form)
        self.widget_lis.append(self.view_form)
        print(self.apps_list)

        """ Проброс сигналов от кнопок к слотам. """
        self.add_apps_btn.clicked.connect(self.insert_add_apps_widget)
        self.edit_apps_btn.clicked.connect(self.insert_edit_apps_widget)

    def insert_add_apps_widget(self):
        """ Вставка виджета добавления заявок. """
        if self.verticalLayout_3.isEmpty():
            self.verticalLayout_3.addWidget(self.apps_list[0])
        print('1', self.apps_form)

    def close_add_apps_widget(self):
        """ Скрытие виджета добавления заявок. """
        self.apps_form.setParent(None)
        print('2', self.apps_form)

    def add_application(self):
        """ Добавление заявки в список перед сохранением. """
        print('added application')

    def save_apps(self):
        """ Добавления списка заявок в БД и скрытие виджета. """
        self.apps_form.setParent(None)
        print('applications saved')

    def insert_edit_apps_widget(self):
        """ Вставка виджета редактиования заявок. """
        if self.verticalLayout_3.isEmpty():
            self.verticalLayout_3.addWidget(self.apps_list[1])

    def view_apps(self):
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


class AddAppsForm(QtWidgets.QWidget, Ui_AddAppsForm):
    def __init__(self, parent=None):
        super(AddAppsForm, self).__init__(parent)
        self.setupUi(self)


class EditAppsForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(EditAppsForm, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    plane = DPlane()
    plane.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
