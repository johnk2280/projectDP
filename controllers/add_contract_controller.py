from PyQt5 import QtWidgets, QtCore
from .widget_controller import WidgetForm
from gui.contract_widget import Ui_ContractForm


class AddContractForm(WidgetForm, Ui_ContractForm):
    def __init__(self):
        super(AddContractForm, self).__init__()
        self.setupUi(self)

        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.hide)

    def save(self):
        """ Добавления списка заявок в БД и скрытие виджета. """
        self.setParent(None)

    def hide(self):
        """ Скрытие виджета добавления заявок. """
        self.setParent(None)
