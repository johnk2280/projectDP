from PyQt5 import QtWidgets, QtCore
from controllers.main_window_controller import Ui_MainWindow


class WidgetForm(QtWidgets.QWidget):
    def __init__(self):
        super(WidgetForm, self).__init__()
        self.setWindowModality(QtCore.Qt.WindowModal)

    def get_data(self):
        pass

    @QtCore.pyqtSlot()
    def save(self):
        self.close()

    @QtCore.pyqtSlot()
    def hide_widget(self):
        self.close()
