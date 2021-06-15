import sys

from PyQt5.QtWidgets import QApplication

from controllers.main_window_controller import DPlane
from database.database import Database


def main():
    orm_database = Database('sqlite:///dp_base.db')
    app = QApplication(sys.argv)
    plane = DPlane(orm_database)
    plane.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
