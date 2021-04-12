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
        self.add_apps_form = AddAppsForm()

        """ Виджет редактирования заявок. """
        self.edit_apps_form = EditAppsForm()

        """ Виджет просмотра заявок, распечатки и экспорта в .csv/.xml.  """
        self.view_apps_form = None

        # print(*self.__dict__, sep='\n')
        # print('*' * 30)
        # print(*self.add_apps_form.__dict__.items(), sep='\n')

        """ Добавление виджетов в список. """
        self.widget_list.append(self.add_apps_form)
        self.widget_list.append(self.edit_apps_form)
        self.widget_list.append(self.view_apps_form)

        """ Проброс сигналов от кнопок к слотам. """
        self.add_apps_btn.clicked.connect(self.insert_add_apps_widget)
        self.edit_apps_btn.clicked.connect(self.insert_edit_apps_widget)
        self.view_apps_btn.clicked.connect(self.insert_view_apps_widget)

    def insert_add_apps_widget(self):
        """ Вставка виджета добавления заявок. """
        if self.verticalLayout_3.isEmpty():
            self.verticalLayout_3.addWidget(self.widget_list[0])

    def insert_edit_apps_widget(self):
        """ Вставка виджета редактиования заявок. """
        if self.verticalLayout_3.isEmpty():
            self.verticalLayout_3.addWidget(self.widget_list[1])

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


class AddAppsForm(QtWidgets.QWidget, Ui_AddAppsForm):
    """ Виджет добавления заявок. """
    def __init__(self, parent=None):
        super(AddAppsForm, self).__init__(parent)
        self.setupUi(self)

        self.add_button.clicked.connect(self.add_application)
        self.save_button.clicked.connect(self.save_apps)
        self.cancel_button.clicked.connect(self.hide_widget)
        self.clear_button.clicked.connect(self.clear_table)
        # self.add_apps_form.add_project_btn.clicked.connect()
        # self.add_apps_form.add_workpack_btn.clicked.connect()
        # self.add_apps_form.add_service_btn.clicked.connect()
        # self.add_apps_form.add_contract_btn.clicked.connect()
        # self.add_apps_form.add_type_btn.clicked.connect()
        # self.add_apps_form.add_builder_btn.clicked.connect()

        """ Кнопка удлаения заявки. """
        self.del_application = None
        # self.del_application.setText('Удалить')
        # self.del_application.clicked.connect(self.delete_row)

        """ Инициализация всех QComboBox в виджете добавления заявок. """

        self.project_cbox.addItems([
            'жд 1 мкр34', 'жд 2 мкр 33', 'жд 31 мкр 34', 'жд 15 мкр 33', 'жд 34 мкр 34'
        ])
        self.contract_cbox.addItems(['001/125-НГ', '123/004-2020/НГ'])
        self.workpack_cbox.addItems([
            'Земляные работы', 'Конструкции сборные железобетонные', 'Отделочные работы'
        ])
        self.type_cbox.addItems(['Мерло', 'Экскаватор', 'Бульдозер', 'Башенный кран'])
        self.service_cbox.addItems([
            'Мерло 5т', 'Мерло 10т', 'Бульдозер 180л.с.', 'Liebherr 8H', 'Komatsu PC300'
        ])
        self.builder_cbox.addItems(['ОРВС', 'ДСУ-2', 'ЮУС'])

        """ Создание таблицы в QTableWidget. """
        self.apps_table_widget.setColumnCount(10)
        self.apps_table_widget.setHorizontalHeaderLabels([
            '', 'Начало', 'Конец', 'Объект',
            'Договор', 'Пакет  работ', 'Вид техники',
            'Вид услуги', 'Подрядчик', 'Отв.'
        ])

        """ Список содержащий выбор пользователя во всех QComboBox. """
        self.apps_items = []

    def get_items(self, clear_=False):
        self.apps_items.append(self.dateTimeEdit_1.date())
        self.apps_items.append(self.dateTimeEdit_2.date())
        self.apps_items.append(self.project_cbox.currentText())
        self.apps_items.append(self.contract_cbox.currentText())
        self.apps_items.append(self.workpack_cbox.currentText())
        self.apps_items.append(self.type_cbox.currentText())
        self.apps_items.append(self.service_cbox.currentText())
        self.apps_items.append(self.builder_cbox.currentText())
        self.apps_items.append(self.person_cbox.text())

    def add_application(self):
        """ Добавление заявки в список перед сохранением. """
        self.add_row()
        self.get_items()
        self.add_items()
        self.apps_items.clear()

    def add_items(self):
        """ Наполнение строки таблицы содержимым всех QComboBox. """
        num_cols = self.apps_table_widget.columnCount()
        num_row = self.apps_table_widget.rowCount()

        """ Добавление кнопки УДОЛИ в 0-ю ячейки строки. """
        self.del_application = QtWidgets.QPushButton()
        self.del_application.setText('Удалить')
        self.apps_table_widget.setCellWidget(num_row - 1, 0, self.del_application)

        for i in range(1, num_cols):
            cell_info = QtWidgets.QTableWidgetItem(str(self.apps_items[i - 1]))
            cell_info.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.apps_table_widget.setItem(num_row - 1, i, cell_info)

    def add_row(self):
        num_row = self.apps_table_widget.rowCount()

        if num_row:
            self.apps_table_widget.insertRow(num_row)
        else:
            self.apps_table_widget.setRowCount(1)

    def delete_row(self):
        print('11')

    def clear_table(self):
        """ Очистка QTableWidget от таблицы. """
        for i in range(self.apps_table_widget.rowCount() - 1, -1, -1):
            self.apps_table_widget.removeRow(i)

    def save_apps(self):
        """ Добавления списка заявок в БД и скрытие виджета. """
        self.clear_table()
        self.setParent(None)
        self.apps_items.clear()

    def hide_widget(self):
        """ Скрытие виджета добавления заявок. """
        self.clear_table()
        self.setParent(None)
        self.apps_items.clear()


class EditAppsForm(QtWidgets.QWidget, Ui_Form):
    """ Виджет редактирования заявок. """
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
