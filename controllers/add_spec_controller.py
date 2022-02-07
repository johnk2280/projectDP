from gui.spec_widget import SpecForm
from controllers.widget_controller import WidgetForm


class AddSpecForm(SpecForm, WidgetForm):
    def __init__(self, parent=None):
        super(AddSpecForm, self).__init__(parent)
        self.setupUi(self)
        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.hide_widget)
