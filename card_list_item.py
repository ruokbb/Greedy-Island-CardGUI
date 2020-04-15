# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card_list_item.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(712, 461)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.id = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.horizontalLayout.addWidget(self.id)
        self.name = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.kind = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.kind.setFont(font)
        self.kind.setObjectName("kind")
        self.horizontalLayout.addWidget(self.kind)
        self.level = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.level.setFont(font)
        self.level.setObjectName("level")
        self.horizontalLayout.addWidget(self.level)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.describe = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.describe.setFont(font)
        self.describe.setObjectName("describe")
        self.horizontalLayout_2.addWidget(self.describe)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.load = QtWidgets.QPushButton(Form)
        self.load.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.load.setFont(font)
        self.load.setObjectName("load")
        self.horizontalLayout_2.addWidget(self.load)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        self.load.clicked.connect(Form.load_card)
        self.pushButton.clicked.connect(Form.delete_card)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.id.setText(_translate("Form", "24"))
        self.name.setText(_translate("Form", "卢卡斯之眼"))
        self.kind.setText(_translate("Form", "战斗"))
        self.level.setText(_translate("Form", "A"))
        self.describe.setText(_translate("Form", "卡片描述："))
        self.load.setText(_translate("Form", "加载卡片"))
        self.pushButton.setText(_translate("Form", "删除卡片"))
