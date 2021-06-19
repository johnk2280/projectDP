from gui.work_pack_widget import WorkPackForm
from controllers.widget_controller import WidgetForm


class AddWorkPackForm(WorkPackForm, WidgetForm):
    def __init__(self):
        super(AddWorkPackForm, self).__init__()
        self.setupUi(self)
        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.hide_widget)
