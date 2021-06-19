from PyQt5 import QtCore
from gui.firm_widget import FirmForm
from controllers.widget_controller import WidgetForm


class AddFirmForm(FirmForm, WidgetForm):
    def __init__(self, parent=None):
        super(FirmForm, self).__init__(parent)
        self.setupUi(self)
        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.hide_widget)
