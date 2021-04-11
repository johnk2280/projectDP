# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_apps_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddAppsForm(object):
    def setupUi(self, AddAppsForm):
        AddAppsForm.setObjectName("AddAppsForm")
        AddAppsForm.resize(1258, 898)
        AddAppsForm.setMinimumSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        AddAppsForm.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddAppsForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(AddAppsForm)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.empty_frame = QtWidgets.QFrame(self.frame)
        self.empty_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.empty_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.empty_frame.setAutoFillBackground(True)
        self.empty_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.empty_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.empty_frame.setObjectName("empty_frame")
        self.gridLayout_3.addWidget(self.empty_frame, 0, 1, 1, 1)
        self.date_frame = QtWidgets.QFrame(self.frame)
        self.date_frame.setMinimumSize(QtCore.QSize(580, 50))
        self.date_frame.setMaximumSize(QtCore.QSize(580, 50))
        self.date_frame.setAutoFillBackground(True)
        self.date_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.date_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.date_frame.setObjectName("date_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.date_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.date_label_1 = QtWidgets.QLabel(self.date_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date_label_1.setFont(font)
        self.date_label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.date_label_1.setObjectName("date_label_1")
        self.horizontalLayout_3.addWidget(self.date_label_1)
        self.date_hlayout_1 = QtWidgets.QHBoxLayout()
        self.date_hlayout_1.setSpacing(6)
        self.date_hlayout_1.setObjectName("date_hlayout_1")
        self.label_3 = QtWidgets.QLabel(self.date_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.date_hlayout_1.addWidget(self.label_3)
        self.dateTimeEdit_1 = QtWidgets.QDateTimeEdit(self.date_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateTimeEdit_1.setFont(font)
        self.dateTimeEdit_1.setWrapping(False)
        self.dateTimeEdit_1.setDate(QtCore.QDate(2021, 4, 2))
        self.dateTimeEdit_1.setCalendarPopup(True)
        self.dateTimeEdit_1.setObjectName("dateTimeEdit_1")
        self.date_hlayout_1.addWidget(self.dateTimeEdit_1)
        self.horizontalLayout_3.addLayout(self.date_hlayout_1)
        self.date_hlayout_2 = QtWidgets.QHBoxLayout()
        self.date_hlayout_2.setObjectName("date_hlayout_2")
        self.label_2 = QtWidgets.QLabel(self.date_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.date_hlayout_2.addWidget(self.label_2)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.date_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateTimeEdit_2.setFont(font)
        self.dateTimeEdit_2.setDate(QtCore.QDate(2021, 4, 2))
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.date_hlayout_2.addWidget(self.dateTimeEdit_2)
        self.horizontalLayout_3.addLayout(self.date_hlayout_2)
        self.gridLayout_3.addWidget(self.date_frame, 0, 0, 1, 1)
        self.apps_frame = QtWidgets.QFrame(self.frame)
        self.apps_frame.setAutoFillBackground(True)
        self.apps_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.apps_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.apps_frame.setObjectName("apps_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.apps_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.project_frame = QtWidgets.QFrame(self.apps_frame)
        self.project_frame.setMinimumSize(QtCore.QSize(650, 230))
        self.project_frame.setMaximumSize(QtCore.QSize(650, 230))
        self.project_frame.setAutoFillBackground(True)
        self.project_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.project_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.project_frame.setObjectName("project_frame")
        self.layoutWidget = QtWidgets.QWidget(self.project_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 646, 217))
        self.layoutWidget.setObjectName("layoutWidget")
        self.project_glayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.project_glayout.setContentsMargins(0, 0, 0, 0)
        self.project_glayout.setSpacing(8)
        self.project_glayout.setObjectName("project_glayout")
        self.project_label = QtWidgets.QLabel(self.layoutWidget)
        self.project_label.setMinimumSize(QtCore.QSize(153, 23))
        self.project_label.setMaximumSize(QtCore.QSize(153, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.project_label.setFont(font)
        self.project_label.setObjectName("project_label")
        self.project_glayout.addWidget(self.project_label, 0, 0, 1, 1)
        self.project_cbox = QtWidgets.QComboBox(self.layoutWidget)
        self.project_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.project_cbox.setMaximumSize(QtCore.QSize(400, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.project_cbox.setFont(font)
        self.project_cbox.setEditable(True)
        self.project_cbox.setObjectName("project_cbox")
        self.project_glayout.addWidget(self.project_cbox, 0, 1, 1, 1)
        self.add_project_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.add_project_btn.setMinimumSize(QtCore.QSize(75, 0))
        self.add_project_btn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.add_project_btn.setObjectName("add_project_btn")
        self.project_glayout.addWidget(self.add_project_btn, 0, 2, 1, 1)
        self.contract_label = QtWidgets.QLabel(self.layoutWidget)
        self.contract_label.setMinimumSize(QtCore.QSize(153, 23))
        self.contract_label.setMaximumSize(QtCore.QSize(153, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_label.setFont(font)
        self.contract_label.setObjectName("contract_label")
        self.project_glayout.addWidget(self.contract_label, 1, 0, 1, 1)
        self.contract_cbox = QtWidgets.QComboBox(self.layoutWidget)
        self.contract_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.contract_cbox.setMaximumSize(QtCore.QSize(400, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_cbox.setFont(font)
        self.contract_cbox.setEditable(True)
        self.contract_cbox.setObjectName("contract_cbox")
        self.project_glayout.addWidget(self.contract_cbox, 1, 1, 1, 1)
        self.add_contract_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.add_contract_btn.setObjectName("add_contract_btn")
        self.project_glayout.addWidget(self.add_contract_btn, 1, 2, 1, 1)
        self.workpack_label = QtWidgets.QLabel(self.layoutWidget)
        self.workpack_label.setMinimumSize(QtCore.QSize(153, 23))
        self.workpack_label.setMaximumSize(QtCore.QSize(153, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.workpack_label.setFont(font)
        self.workpack_label.setObjectName("workpack_label")
        self.project_glayout.addWidget(self.workpack_label, 2, 0, 1, 1)
        self.workpack_cbox = QtWidgets.QComboBox(self.layoutWidget)
        self.workpack_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.workpack_cbox.setMaximumSize(QtCore.QSize(400, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.workpack_cbox.setFont(font)
        self.workpack_cbox.setEditable(True)
        self.workpack_cbox.setObjectName("workpack_cbox")
        self.project_glayout.addWidget(self.workpack_cbox, 2, 1, 1, 1)
        self.add_workpack_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.add_workpack_btn.setObjectName("add_workpack_btn")
        self.project_glayout.addWidget(self.add_workpack_btn, 2, 2, 1, 1)
        self.type_label = QtWidgets.QLabel(self.layoutWidget)
        self.type_label.setMinimumSize(QtCore.QSize(153, 23))
        self.type_label.setMaximumSize(QtCore.QSize(153, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.type_label.setFont(font)
        self.type_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.type_label.setObjectName("type_label")
        self.project_glayout.addWidget(self.type_label, 3, 0, 1, 1)
        self.type_cbox = QtWidgets.QComboBox(self.layoutWidget)
        self.type_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.type_cbox.setMaximumSize(QtCore.QSize(400, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.type_cbox.setFont(font)
        self.type_cbox.setEditable(True)
        self.type_cbox.setObjectName("type_cbox")
        self.project_glayout.addWidget(self.type_cbox, 3, 1, 1, 1)
        self.add_type_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.add_type_btn.setObjectName("add_type_btn")
        self.project_glayout.addWidget(self.add_type_btn, 3, 2, 1, 1)
        self.service_label = QtWidgets.QLabel(self.layoutWidget)
        self.service_label.setMinimumSize(QtCore.QSize(153, 23))
        self.service_label.setMaximumSize(QtCore.QSize(153, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.service_label.setFont(font)
        self.service_label.setObjectName("service_label")
        self.project_glayout.addWidget(self.service_label, 4, 0, 1, 1)
        self.service_cbox = QtWidgets.QComboBox(self.layoutWidget)
        self.service_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.service_cbox.setMaximumSize(QtCore.QSize(400, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.service_cbox.setFont(font)
        self.service_cbox.setEditable(True)
        self.service_cbox.setObjectName("service_cbox")
        self.project_glayout.addWidget(self.service_cbox, 4, 1, 1, 1)
        self.add_service_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.add_service_btn.setObjectName("add_service_btn")
        self.project_glayout.addWidget(self.add_service_btn, 4, 2, 1, 1)
        self.builder_label = QtWidgets.QLabel(self.layoutWidget)
        self.builder_label.setMinimumSize(QtCore.QSize(153, 23))
        self.builder_label.setMaximumSize(QtCore.QSize(153, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.builder_label.setFont(font)
        self.builder_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.builder_label.setObjectName("builder_label")
        self.project_glayout.addWidget(self.builder_label, 5, 0, 1, 1)
        self.builder_cbox = QtWidgets.QComboBox(self.layoutWidget)
        self.builder_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.builder_cbox.setMaximumSize(QtCore.QSize(400, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.builder_cbox.setFont(font)
        self.builder_cbox.setEditable(True)
        self.builder_cbox.setObjectName("builder_cbox")
        self.project_glayout.addWidget(self.builder_cbox, 5, 1, 1, 1)
        self.add_builder_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.add_builder_btn.setObjectName("add_builder_btn")
        self.project_glayout.addWidget(self.add_builder_btn, 5, 2, 1, 1)
        self.person_label = QtWidgets.QLabel(self.layoutWidget)
        self.person_label.setMinimumSize(QtCore.QSize(153, 22))
        self.person_label.setMaximumSize(QtCore.QSize(153, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_label.setFont(font)
        self.person_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.person_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.person_label.setObjectName("person_label")
        self.project_glayout.addWidget(self.person_label, 6, 0, 1, 1)
        self.person_cbox = QtWidgets.QLineEdit(self.layoutWidget)
        self.person_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.person_cbox.setMaximumSize(QtCore.QSize(400, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_cbox.setFont(font)
        self.person_cbox.setObjectName("person_cbox")
        self.project_glayout.addWidget(self.person_cbox, 6, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.project_frame)
        self.button_hlayout = QtWidgets.QHBoxLayout()
        self.button_hlayout.setContentsMargins(-1, 6, -1, 6)
        self.button_hlayout.setObjectName("button_hlayout")
        self.add_button = QtWidgets.QPushButton(self.apps_frame)
        self.add_button.setMinimumSize(QtCore.QSize(160, 30))
        self.add_button.setMaximumSize(QtCore.QSize(160, 30))
        self.add_button.setObjectName("add_button")
        self.button_hlayout.addWidget(self.add_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_hlayout.addItem(spacerItem)
        self.save_button = QtWidgets.QPushButton(self.apps_frame)
        self.save_button.setMinimumSize(QtCore.QSize(160, 30))
        self.save_button.setMaximumSize(QtCore.QSize(160, 30))
        self.save_button.setObjectName("save_button")
        self.button_hlayout.addWidget(self.save_button)
        self.clear_button = QtWidgets.QPushButton(self.apps_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        self.clear_button.setMinimumSize(QtCore.QSize(160, 30))
        self.clear_button.setMaximumSize(QtCore.QSize(160, 30))
        self.clear_button.setObjectName("clear_button")
        self.button_hlayout.addWidget(self.clear_button)
        self.cancel_button = QtWidgets.QPushButton(self.apps_frame)
        self.cancel_button.setMinimumSize(QtCore.QSize(160, 30))
        self.cancel_button.setMaximumSize(QtCore.QSize(160, 30))
        self.cancel_button.setObjectName("cancel_button")
        self.button_hlayout.addWidget(self.cancel_button)
        self.verticalLayout_2.addLayout(self.button_hlayout)
        self.apps_table_widget = QtWidgets.QTableWidget(self.apps_frame)
        self.apps_table_widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apps_table_widget.sizePolicy().hasHeightForWidth())
        self.apps_table_widget.setSizePolicy(sizePolicy)
        self.apps_table_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.apps_table_widget.setAlternatingRowColors(True)
        self.apps_table_widget.setShowGrid(True)
        self.apps_table_widget.setObjectName("apps_table_widget")
        self.apps_table_widget.setColumnCount(0)
        self.apps_table_widget.setRowCount(0)
        self.apps_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.apps_table_widget.horizontalHeader().setSortIndicatorShown(True)
        self.apps_table_widget.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.apps_table_widget)
        self.gridLayout_3.addWidget(self.apps_frame, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(AddAppsForm)
        QtCore.QMetaObject.connectSlotsByName(AddAppsForm)

    def retranslateUi(self, AddAppsForm):
        _translate = QtCore.QCoreApplication.translate
        AddAppsForm.setWindowTitle(_translate("AddAppsForm", "Form"))
        self.date_label_1.setText(_translate("AddAppsForm", "Дата работы"))
        self.label_3.setText(_translate("AddAppsForm", "с"))
        self.dateTimeEdit_1.setDisplayFormat(_translate("AddAppsForm", "dd.MM.yy H:mm"))
        self.label_2.setText(_translate("AddAppsForm", "по"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("AddAppsForm", "dd.MM.yy H:mm"))
        self.project_label.setText(_translate("AddAppsForm", "<html><head/><body><p>Объект строительства</p></body></html>"))
        self.add_project_btn.setText(_translate("AddAppsForm", "Добавить"))
        self.contract_label.setText(_translate("AddAppsForm", "Договор"))
        self.add_contract_btn.setText(_translate("AddAppsForm", "Добавить"))
        self.workpack_label.setText(_translate("AddAppsForm", "Пакет работ"))
        self.add_workpack_btn.setText(_translate("AddAppsForm", "Добавить"))
        self.type_label.setText(_translate("AddAppsForm", "Вид техники"))
        self.add_type_btn.setText(_translate("AddAppsForm", "Добавить"))
        self.service_label.setText(_translate("AddAppsForm", "Вид услуги (CGC)"))
        self.add_service_btn.setText(_translate("AddAppsForm", "Добавить"))
        self.builder_label.setText(_translate("AddAppsForm", "Подрядчик"))
        self.add_builder_btn.setText(_translate("AddAppsForm", "Добавить"))
        self.person_label.setText(_translate("AddAppsForm", "Ответственный"))
        self.add_button.setText(_translate("AddAppsForm", "Добавить заявку"))
        self.save_button.setText(_translate("AddAppsForm", "Записать и закрыть"))
        self.clear_button.setText(_translate("AddAppsForm", "Очистить таблицу"))
        self.cancel_button.setText(_translate("AddAppsForm", "Отмена"))
