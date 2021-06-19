from gui.mechanism_type_widget import MechTypeForm
from controllers.widget_controller import WidgetForm


class AddMechTypeForm(MechTypeForm, WidgetForm):
    def __init__(self, parent=None):
        super(AddMechTypeForm, self).__init__(parent)
        self.setupUi(self)
        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.hide_widget)