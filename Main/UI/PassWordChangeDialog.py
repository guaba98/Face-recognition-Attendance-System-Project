# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PassWordChangeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PWChangeDialog(object):
    def setupUi(self, PWChangeDialog):
        PWChangeDialog.setObjectName("PWChangeDialog")
        PWChangeDialog.resize(363, 420)
        PWChangeDialog.setStyleSheet("QPushButton#ok_btn{\n"
"    background-color: rgb(48, 133, 254);\n"
"    color:white;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton#cancel_btn{\n"
"    background-color: #E6E6E6;\n"
"    color: #252C58;\n"
"    border-radius:10px;\n"
"}\n"
"QLineEdit{\n"
"height:30px;\n"
"border: 1px solid  rgb(48, 133, 254);\n"
"}")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(PWChangeDialog)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(PWChangeDialog)
        self.widget.setStyleSheet("#widget{background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;}")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(25, 49, 25, 30)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_lab = QtWidgets.QLabel(self.widget_2)
        self.title_lab.setMinimumSize(QtCore.QSize(0, 18))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.title_lab.setFont(font)
        self.title_lab.setObjectName("title_lab")
        self.horizontalLayout.addWidget(self.title_lab)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:10px;")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.new_pw_edit = QtWidgets.QLineEdit(self.widget_2)
        self.new_pw_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.new_pw_edit.setStyleSheet("border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;")
        self.new_pw_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pw_edit.setObjectName("new_pw_edit")
        self.verticalLayout.addWidget(self.new_pw_edit)
        self.new_pw_recheck_edit = QtWidgets.QLineEdit(self.widget_2)
        self.new_pw_recheck_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.new_pw_recheck_edit.setStyleSheet("border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;")
        self.new_pw_recheck_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pw_recheck_edit.setObjectName("new_pw_recheck_edit")
        self.verticalLayout.addWidget(self.new_pw_recheck_edit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 13))
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(244, 30))
        self.lineEdit_4.setStyleSheet("border-radius:10px;")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_5.setStyleSheet("border-radius:10px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.ok_btn = QtWidgets.QPushButton(self.widget_2)
        self.ok_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout_2.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.widget_2)
        self.cancel_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.cancel_btn.setObjectName("cancel_btn")
        self.verticalLayout_2.addWidget(self.cancel_btn)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.horizontalLayout_3.addWidget(self.widget)

        self.retranslateUi(PWChangeDialog)
        QtCore.QMetaObject.connectSlotsByName(PWChangeDialog)

    def retranslateUi(self, PWChangeDialog):
        _translate = QtCore.QCoreApplication.translate
        PWChangeDialog.setWindowTitle(_translate("PWChangeDialog", "Dialog"))
        self.title_lab.setText(_translate("PWChangeDialog", "비밀번호 변경"))
        self.lineEdit.setPlaceholderText(_translate("PWChangeDialog", "현재 비밀번호"))
        self.new_pw_edit.setPlaceholderText(_translate("PWChangeDialog", "새 비밀번호"))
        self.new_pw_recheck_edit.setPlaceholderText(_translate("PWChangeDialog", "비밀번호 확인"))
        self.label_2.setText(_translate("PWChangeDialog", "아래 6자리 문자를 보이는 대로 입력해주세요."))
        self.lineEdit_5.setPlaceholderText(_translate("PWChangeDialog", "자동입력방지문자"))
        self.ok_btn.setText(_translate("PWChangeDialog", "확인"))
        self.cancel_btn.setText(_translate("PWChangeDialog", "취소"))
from Main.UI import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PWChangeDialog = QtWidgets.QDialog()
    ui = Ui_PWChangeDialog()
    ui.setupUi(PWChangeDialog)
    PWChangeDialog.show()
    sys.exit(app.exec_())