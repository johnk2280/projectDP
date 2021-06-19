from gui.services_widget import ServiceForm
from controllers.widget_controller import WidgetForm


class AddServiceForm(ServiceForm, WidgetForm):
    def __init__(self):
        super(AddServiceForm, self).__init__()
        self.setupUi(self)
        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.hide_widget)
