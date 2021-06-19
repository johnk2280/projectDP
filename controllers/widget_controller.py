from PyQt5 import QtWidgets, QtCore
from controllers.main_window_controller import Ui_MainWindow


class WidgetForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WidgetForm, self).__init__(parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def get_data(self):
        item_values = []
        for obj in self.frame.children():
            if isinstance(obj, QtWidgets.QDateTimeEdit):
                item_values.append(obj.text())
            elif isinstance(obj, QtWidgets.QComboBox):
                item_values.append(obj.currentText())
            elif isinstance(obj, QtWidgets.QLineEdit):
                item_values.append(obj.text())

        # TODO: добавить логику обработки чекбоксов для виджета firm.
        #  Обработать исключения.
        #  Проверить последовательность считывания данных.
        #  После закрытия виджета, остаются выбранные значения.

        return item_values

    @QtCore.pyqtSlot()
    def save(self):
        data = self.get_data()
        self.close()

    @QtCore.pyqtSlot()
    def hide_widget(self):
        self.close()
