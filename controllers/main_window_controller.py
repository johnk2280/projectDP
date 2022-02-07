from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox

from gui.main_window import Ui_MainWindow
from gui.contract_widget import ContractForm

from controllers.add_orders_controller import AddOrdersForm
from controllers.add_contract_controller import AddContractForm

from database.database import Database


class DPlane(QMainWindow, Ui_MainWindow):
    def __init__(self, db: Database, parent=None):
        super(DPlane, self).__init__(parent)
        self.setupUi(self)

        self.db = db

        """ Initializing widgets. """
        self.add_orders_form = AddOrdersForm()
        # self.add_contracts_form = AddContractForm()
        # self.contract_form = ContractForm()

        """ Forwarding signals from buttons to slots. """
        self.add_orders_btn.clicked.connect(self.insert_add_orders_widget)
        self.edit_orders_btn.clicked.connect(self.insert_edit_orders_widget)
        self.view_orders_btn.clicked.connect(self.insert_view_orders_widget)
        self.add_contracts_btn.clicked.connect(self.insert_add_contracts_widget)
        self.edit_contracts_btn.clicked.connect(self.insert_edit_contracts_widget)
        self.view_contracts_btn.clicked.connect(self.insert_view_contracts_widget)
        self.add_reports_btn.clicked.connect(self.insert_add_reports_widget)
        self.edit_reports_btn.clicked.connect(self.insert_edit_reports_widget)
        self.view_reports_btn.clicked.connect(self.insert_view_reports_widget)

    @QtCore.pyqtSlot()
    def insert_add_orders_widget(self):
        """ Insert a widget for adding orders. """
        if self.verticalLayout_3.isEmpty():
            self.verticalLayout_3.addWidget(self.add_orders_form)

    @QtCore.pyqtSlot()
    def insert_edit_orders_widget(self):
        """ Вставка виджета редактиования заявок. """
        pass

    @QtCore.pyqtSlot()
    def insert_view_orders_widget(self):
        """ Вставка виджета просмотра заявок. """
        pass

    @QtCore.pyqtSlot()
    def insert_add_contracts_widget(self):
        # if self.verticalLayout_5.isEmpty():
        #     self.verticalLayout_5.addWidget(self.add_contracts_form)
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
