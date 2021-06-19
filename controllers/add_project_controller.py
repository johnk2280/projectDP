from gui.project_widget import ProjectForm
from controllers.widget_controller import WidgetForm


class AddProjectForm(ProjectForm, WidgetForm):
    def __init__(self):
        super(AddProjectForm, self).__init__()
        self.setupUi(self)
        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.hide_widget)
