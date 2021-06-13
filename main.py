import sys

from PyQt5.QtWidgets import QApplication

from app import DPlane


def main():
    app = QApplication(sys.argv)
    plane = DPlane()
    plane.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
