import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

from gui1.pd_main_window import Ui_MainWindow
from gui1.add_orders_widget import Ui_AddOrdersForm
from gui1.edit_orders_widget import Ui_Form

from database.database import Database


class DPlane(QMainWindow, Ui_MainWindow):
    def __init__(self, db: Database, parent=None):
        super(DPlane, self).__init__(parent)
        self.setupUi(self)

        self.db = db
        """ Список виджетов для динамической смены. """
        self.widget_list = []

        """ Виджет добавления заявок. """
        # self.add_orders_form = AddOrdersForm(self.db)

        """ Виджет редактирования заявок. """
        self.edit_orders_form = EditOrdersForm()

        """ Виджет просмотра заявок, распечатки и экспорта в .csv/.xml.  """
        self.view_orders_form = None

        """ Добавление виджетов в список. """
        self.widget_list.append(self.add_orders_form)
        self.widget_list.append(self.edit_orders_form)
        self.widget_list.append(self.view_orders_form)

        """ Проброс сигналов от кнопок к слотам. """
        self.add_orders_btn.clicked.connect(self.insert_add_orders_widget)
        self.edit_orders_btn.clicked.connect(self.insert_edit_orders_widget)
        self.view_orders_btn.clicked.connect(self.insert_view_orders_widget)

        self.add_contracts_btn.clicked.connect(self.insert_add_contracts_widget)
        self.edit_contracts_btn.clicked.connect(self.insert_edit_contracts_widget)
        self.view_contracts_btn.clicked.connect(self.insert_view_contracts_widget)

        self.add_reports_btn.clicked.connect(self.insert_add_reports_widget)
        self.edit_reports_btn.clicked.connect(self.insert_edit_reports_widget)
        self.view_reports_btn.clicked.connect(self.insert_view_reports_widget)

    def insert_add_orders_widget(self, event: QtCore.QEvent):
        """ Вставка виджета добавления заявок. """
        if self.verticalLayout_3.isEmpty():
            self.verticalLayout_3.addWidget(self.widget_list[0])

    def insert_edit_orders_widget(self):
        """ Вставка виджета редактиования заявок. """
        if self.verticalLayout_3.isEmpty():
            self.verticalLayout_3.addWidget(self.widget_list[1])

    def insert_view_orders_widget(self):
        """ Вставка виджета просмотра заявок. """
        pass

    def insert_add_contracts_widget(self):
        pass

    def insert_edit_contracts_widget(self):
        pass

    def insert_view_contracts_widget(self):
        pass

    def insert_add_reports_widget(self):
        pass

    def insert_edit_reports_widget(self):
        pass

    def insert_view_reports_widget(self):
        pass

    def closeEvent(self, event):
        print(event)
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


class WidgetForm:
    def __init__(self):
        pass

    def get_data(self):
        pass

    def save(self):
        pass

    def hide(self):
        pass


# class AddOrdersForm(QtWidgets.QWidget, Ui_AddOrdersForm):
#     """ Виджет добавления заявок. """
#     def __init__(self, db: Database, parent=None):
#         super(AddOrdersForm, self).__init__(parent)
#         self.setupUi(self)
#
#         self.db = db
#         """ Список содержащий выбор пользователя во всех QComboBox. """
#         self.orders_items = []
#         self.header_labels = ['', 'Начало', 'Конец']
#
#         """ Кнопка удлаения заявки. """
#         self.del_app = None
#
#         self.add_button.clicked.connect(self.add_application)
#         self.save_button.clicked.connect(self.save)
#         self.cancel_button.clicked.connect(self.hide)
#         self.clear_button.clicked.connect(self.clear_table)
#         # self.add_orders_form.add_project_btn.clicked.connect()
#         # self.add_orders_form.add_workpack_btn.clicked.connect()
#         # self.add_orders_form.add_service_btn.clicked.connect()
#         # self.add_orders_form.add_contract_btn.clicked.connect()
#         # self.add_orders_form.add_type_btn.clicked.connect()
#         # self.add_orders_form.add_builder_btn.clicked.connect()
#
#         """ Инициализация всех QComboBox в виджете добавления заявок. """
#
#         self.project_cbox.addItems([
#             'жд 1 мкр34', 'жд 2 мкр 33', 'жд 31 мкр 34', 'жд 15 мкр 33', 'жд 34 мкр 34'
#         ])
#         self.contract_cbox.addItems(['001/125-НГ', '123/004-2020/НГ'])
#         self.workpack_cbox.addItems([
#             'Земляные работы', 'Конструкции сборные железобетонные', 'Отделочные работы'
#         ])
#         self.type_cbox.addItems(['Мерло', 'Экскаватор', 'Бульдозер', 'Башенный кран'])
#         self.service_cbox.addItems([
#             'Мерло 5т', 'Мерло 10т', 'Бульдозер 180л.с.', 'Liebherr 8H', 'Komatsu PC300'
#         ])
#         self.builder_cbox.addItems(['ОРВС', 'ДСУ-2', 'ЮУС'])
#
#         self.create_table()
#
#     def create_table(self):
#         """ Создание таблицы в QTableWidget. """
#
#         for obj in self.project_frame.children():
#             if isinstance(obj, QtWidgets.QLabel):
#                 self.header_labels.append(obj.text())
#
#         num_cols = len(self.header_labels)
#         self.orders_table_widget.setColumnCount(num_cols)
#
#         self.orders_table_widget.setHorizontalHeaderLabels(self.header_labels)
#         self.orders_table_widget.horizontalHeader().setSectionResizeMode(0, 2)
#
#         for i in range(1, num_cols - 1):
#             self.orders_table_widget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
#
#         self.orders_table_widget.horizontalHeader().setSectionResizeMode(num_cols - 1, QtWidgets.QHeaderView.Stretch)
#
#     def get_items(self, clear_=False):
#         """
#         Функция наполняет список значениями
#         из QDateTimeEdit, QComboBox, QLineEdit.
#         """
#
#         self.orders_items.append(self.dateTimeEdit_1)
#         self.orders_items.append(self.dateTimeEdit_2)
#
#         for obj in self.project_frame.children():
#             if isinstance(obj, QtWidgets.QComboBox):
#                 self.orders_items.append(obj.currentText())
#             elif isinstance(obj, QtWidgets.QLineEdit):
#                 self.orders_items.append(obj.text())
#
#     def add_application(self):
#         """ Добавление заявки в список перед сохранением. """
#         self.add_row()
#         self.get_items()
#         self.add_items()
#         self.orders_items.clear()
#
#     def add_items(self):
#         """ Функция наполнения строки таблицы содержимым всех QComboBox. """
#         num_cols = self.orders_table_widget.columnCount()
#         num_row = self.orders_table_widget.rowCount()
#
#         """ Добавление кнопки <Удалить> в 0-ю ячейки строки. """
#         self.del_app = QtWidgets.QPushButton()
#         self.del_app.setText('Удалить')
#         self.orders_table_widget.setCellWidget(num_row - 1, 0, self.del_app)
#         self.del_app.clicked.connect(self.delete_row)
#
#         for i in range(1, num_cols):
#             if isinstance(self.orders_items[i - 1], QtWidgets.QDateTimeEdit):
#                 cell_info = QtWidgets.QTableWidgetItem(self.orders_items[i - 1].text())
#             else:
#                 cell_info = QtWidgets.QTableWidgetItem(self.orders_items[i - 1])
#
#             cell_info.setFlags(
#                 QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
#             )
#             self.orders_table_widget.setItem(num_row - 1, i, cell_info)
#
#     def add_row(self):
#         num_row = self.orders_table_widget.rowCount()
#
#         if num_row:
#             self.orders_table_widget.insertRow(num_row)
#         else:
#             self.orders_table_widget.setRowCount(1)
#
#     def delete_row(self):
#         button = self.sender()
#         if button:
#             row_index = self.orders_table_widget.indexAt(button.pos()).row()
#             self.orders_table_widget.removeRow(row_index)
#
#     def clear_table(self):
#         """ Очистка QTableWidget от таблицы. """
#         for i in range(self.orders_table_widget.rowCount() - 1, -1, -1):
#             self.orders_table_widget.removeRow(i)
#
#     def save(self):
#         """ Добавления списка заявок в БД и скрытие виджета. """
#         data = {}
#         self.db.add_app(data)
#         self.clear_table()
#         self.setParent(None)
#         self.orders_items.clear()
#
#     def hide(self):
#         """ Скрытие виджета добавления заявок. """
#         self.clear_table()
#         self.setParent(None)
#         self.orders_items.clear()


class EditOrdersForm(QtWidgets.QWidget, Ui_Form):
    """ Виджет редактирования заявок. """
    def __init__(self, parent=None):
        super(EditOrdersForm, self).__init__(parent)
        self.setupUi(self)
