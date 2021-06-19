from PyQt5 import QtWidgets, QtCore

from gui.add_orders_widget import Ui_AddOrdersForm
from gui.contract_widget import ContractForm

from controllers.widget_controller import WidgetForm
from controllers.add_contract_controller import AddContractForm
from controllers.add_firm_controller import AddFirmForm
from controllers.add_mech_type_controller import AddMechTypeForm
from controllers.add_project_controller import AddProjectForm
from controllers.add_service_controller import AddServiceForm
from controllers.add_work_pack_controller import AddWorkPackForm
from controllers.add_spec_controller import AddSpecForm


class AddOrdersForm(WidgetForm, Ui_AddOrdersForm):
    """ Виджет добавления заявок. """

    def __init__(self):
        super(AddOrdersForm, self).__init__()
        self.setupUi(self)

        self.add_contract_form = AddContractForm()
        self.add_firm_form = AddFirmForm()

        self.add_mech_type_form = AddMechTypeForm()
        self.add_project_form = AddProjectForm()
        self.add_service_form = AddServiceForm()
        self.add_spec_form = AddSpecForm()
        self.add_work_pack_form = AddWorkPackForm()

        # self.db = db
        """ Список содержащий выбор пользователя во всех QComboBox. """
        self.orders_items = []
        self.header_labels = ['', 'Начало', 'Конец']

        """ Кнопка удлаения заявки. """
        self.del_app = None

        self.add_button.clicked.connect(self.add_application)
        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.hide)
        self.clear_button.clicked.connect(self._clear_table)
        self.add_contract_btn.clicked.connect(self.show_contract_form)
        self.add_org_btn.clicked.connect(self.show_firm_form)
        self.add_project_btn.clicked.connect(self.show_project_form)
        self.add_workpack_btn.clicked.connect(self.show_work_pack_form)
        self.add_service_btn.clicked.connect(self.show_service_form)
        self.add_type_btn.clicked.connect(self.show_mech_type_form)
        self.add_builder_btn.clicked.connect(self.show_firm_form)

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

        self._create_table()

    def _create_table(self):
        """ Создание таблицы в QTableWidget. """

        for obj in self.project_frame.children():
            if isinstance(obj, QtWidgets.QLabel):
                self.header_labels.append(obj.text())

        num_cols = len(self.header_labels)
        self.orders_table_widget.setColumnCount(num_cols)

        self.orders_table_widget.setHorizontalHeaderLabels(self.header_labels)
        self.orders_table_widget.horizontalHeader().setSectionResizeMode(0, 2)

        for i in range(1, num_cols - 1):
            self.orders_table_widget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        self.orders_table_widget.horizontalHeader().setSectionResizeMode(num_cols - 1, QtWidgets.QHeaderView.Stretch)

    def _get_items(self, clear_=False):
        """
        Функция наполняет список значениями
        из QDateTimeEdit, QComboBox, QLineEdit.
        """

        self.orders_items.append(self.dateTimeEdit_1)
        self.orders_items.append(self.dateTimeEdit_2)

        for obj in self.project_frame.children():
            if isinstance(obj, QtWidgets.QComboBox):
                self.orders_items.append(obj.currentText())
            elif isinstance(obj, QtWidgets.QLineEdit):
                self.orders_items.append(obj.text())

    def add_application(self):
        """ Добавление заявки в список перед сохранением. """
        self._add_row()
        self._get_items()
        self._add_items()
        self.orders_items.clear()

    def _add_items(self):
        """ Функция наполнения строки таблицы содержимым всех QComboBox. """
        num_cols = self.orders_table_widget.columnCount()
        num_row = self.orders_table_widget.rowCount()

        """ Добавление кнопки <Удалить> в 0-ю ячейки строки. """
        self.del_app = QtWidgets.QPushButton()
        self.del_app.setText('Удалить')
        self.orders_table_widget.setCellWidget(num_row - 1, 0, self.del_app)
        self.del_app.clicked.connect(self._delete_row)

        for i in range(1, num_cols):
            if isinstance(self.orders_items[i - 1], QtWidgets.QDateTimeEdit):
                cell_info = QtWidgets.QTableWidgetItem(self.orders_items[i - 1].text())
            else:
                cell_info = QtWidgets.QTableWidgetItem(self.orders_items[i - 1])

            cell_info.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.orders_table_widget.setItem(num_row - 1, i, cell_info)

    def _add_row(self):
        num_row = self.orders_table_widget.rowCount()

        if num_row:
            self.orders_table_widget.insertRow(num_row)
        else:
            self.orders_table_widget.setRowCount(1)

    def _delete_row(self):
        button = self.sender()
        if button:
            row_index = self.orders_table_widget.indexAt(button.pos()).row()
            self.orders_table_widget.removeRow(row_index)

    def _clear_table(self):
        """ Очистка QTableWidget от таблицы. """
        for i in range(self.orders_table_widget.rowCount() - 1, -1, -1):
            self.orders_table_widget.removeRow(i)

    @QtCore.pyqtSlot()
    def show_contract_form(self):
        self.add_contract_form.show()

    @QtCore.pyqtSlot()
    def show_firm_form(self):
        self.add_firm_form.show()

    @QtCore.pyqtSlot()
    def show_mech_type_form(self):
        self.add_mech_type_form.show()

    @QtCore.pyqtSlot()
    def show_project_form(self):
        self.add_project_form.show()

    @QtCore.pyqtSlot()
    def show_service_form(self):
        self.add_service_form.show()

    @QtCore.pyqtSlot()
    def show_work_pack_form(self):
        self.add_work_pack_form.show()

    def save(self):
        """ Добавления списка заявок в БД и скрытие виджета. """
        data = {}
        # self.db.add_app(data)
        self._clear_table()
        self.setParent(None)
        self.orders_items.clear()

    def hide_widget(self):
        """ Скрытие виджета добавления заявок. """
        self._clear_table()
        self.setParent(None)
        self.orders_items.clear()
