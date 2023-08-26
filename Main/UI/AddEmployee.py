# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddEmployee.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddEmployee(object):
    def setupUi(self, AddEmployee):
        AddEmployee.setObjectName("AddEmployee")
        AddEmployee.resize(1120, 663)
        AddEmployee.setStyleSheet("background-color: rgb(241, 242, 246);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AddEmployee)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top_widget = QtWidgets.QWidget(AddEmployee)
        self.top_widget.setMinimumSize(QtCore.QSize(0, 116))
        self.top_widget.setMaximumSize(QtCore.QSize(16777215, 116))
        self.top_widget.setStyleSheet("\n"
"QWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 3px;\n"
"}\n"
"")
        self.top_widget.setObjectName("top_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.top_vlay = QtWidgets.QVBoxLayout()
        self.top_vlay.setObjectName("top_vlay")
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.top_vlay.addItem(spacerItem1)
        self.widget_11 = QtWidgets.QWidget(self.top_widget)
        self.widget_11.setMaximumSize(QtCore.QSize(290, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.widget_11.setFont(font)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.home_btn = QtWidgets.QPushButton(self.widget_11)
        self.home_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.home_btn.setFont(font)
        self.home_btn.setObjectName("home_btn")
        self.horizontalLayout_12.addWidget(self.home_btn)
        self.top_vlay.addWidget(self.widget_11)
        self.horizontalLayout_2.addLayout(self.top_vlay)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.top_widget)
        self.widget_3 = QtWidgets.QWidget(AddEmployee)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 60, 0, 55)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(323, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setStyleSheet("QLineEdit{\n"
"height: 40px;\n"
"}\n"
"QComboBox{\n"
"height: 40px;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(60)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.user_id_lineedit = QtWidgets.QLineEdit(self.widget)
        self.user_id_lineedit.setMinimumSize(QtCore.QSize(300, 0))
        self.user_id_lineedit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_id_lineedit.setFont(font)
        self.user_id_lineedit.setReadOnly(False)
        self.user_id_lineedit.setObjectName("user_id_lineedit")
        self.gridLayout.addWidget(self.user_id_lineedit, 2, 1, 1, 1)
        self.pw_lab = QtWidgets.QLabel(self.widget)
        self.pw_lab.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pw_lab.setFont(font)
        self.pw_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.pw_lab.setObjectName("pw_lab")
        self.gridLayout.addWidget(self.pw_lab, 3, 0, 1, 1)
        self.dept_lab = QtWidgets.QLabel(self.widget)
        self.dept_lab.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dept_lab.setFont(font)
        self.dept_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.dept_lab.setObjectName("dept_lab")
        self.gridLayout.addWidget(self.dept_lab, 1, 0, 1, 1)
        self.pw_recheck_lineedit = QtWidgets.QLineEdit(self.widget)
        self.pw_recheck_lineedit.setMinimumSize(QtCore.QSize(300, 0))
        self.pw_recheck_lineedit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pw_recheck_lineedit.setFont(font)
        self.pw_recheck_lineedit.setReadOnly(False)
        self.pw_recheck_lineedit.setObjectName("pw_recheck_lineedit")
        self.gridLayout.addWidget(self.pw_recheck_lineedit, 4, 1, 1, 1)
        self.pw_recheck_lab = QtWidgets.QLabel(self.widget)
        self.pw_recheck_lab.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pw_recheck_lab.setFont(font)
        self.pw_recheck_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.pw_recheck_lab.setObjectName("pw_recheck_lab")
        self.gridLayout.addWidget(self.pw_recheck_lab, 4, 0, 1, 1)
        self.name_lab = QtWidgets.QLabel(self.widget)
        self.name_lab.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.name_lab.setFont(font)
        self.name_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lab.setObjectName("name_lab")
        self.gridLayout.addWidget(self.name_lab, 0, 0, 1, 1)
        self.name_lineedit = QtWidgets.QLineEdit(self.widget)
        self.name_lineedit.setMinimumSize(QtCore.QSize(300, 0))
        self.name_lineedit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_lineedit.setFont(font)
        self.name_lineedit.setReadOnly(False)
        self.name_lineedit.setObjectName("name_lineedit")
        self.gridLayout.addWidget(self.name_lineedit, 0, 1, 1, 1)
        self.user_id_lab = QtWidgets.QLabel(self.widget)
        self.user_id_lab.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.user_id_lab.setFont(font)
        self.user_id_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.user_id_lab.setObjectName("user_id_lab")
        self.gridLayout.addWidget(self.user_id_lab, 2, 0, 1, 1)
        self.pw_lineedit = QtWidgets.QLineEdit(self.widget)
        self.pw_lineedit.setMinimumSize(QtCore.QSize(300, 0))
        self.pw_lineedit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pw_lineedit.setFont(font)
        self.pw_lineedit.setReadOnly(False)
        self.pw_lineedit.setObjectName("pw_lineedit")
        self.gridLayout.addWidget(self.pw_lineedit, 3, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.admit_btn = QtWidgets.QPushButton(self.widget_2)
        self.admit_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.admit_btn.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.admit_btn.setFont(font)
        self.admit_btn.setStyleSheet("background-color: rgb(48, 133, 254);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.admit_btn.setObjectName("admit_btn")
        self.horizontalLayout.addWidget(self.admit_btn)
        self.face_rec_btn = QtWidgets.QPushButton(self.widget_2)
        self.face_rec_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.face_rec_btn.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.face_rec_btn.setFont(font)
        self.face_rec_btn.setStyleSheet("background-color: rgb(115, 154, 240);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.face_rec_btn.setObjectName("face_rec_btn")
        self.horizontalLayout.addWidget(self.face_rec_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.widget_2)
        self.cancel_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.cancel_btn.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius:10px;")
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout_3.addWidget(self.widget)
        spacerItem5 = QtWidgets.QSpacerItem(322, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.widget_3)

        self.retranslateUi(AddEmployee)
        QtCore.QMetaObject.connectSlotsByName(AddEmployee)

    def retranslateUi(self, AddEmployee):
        _translate = QtCore.QCoreApplication.translate
        AddEmployee.setWindowTitle(_translate("AddEmployee", "Form"))
        self.home_btn.setText(_translate("AddEmployee", "사원 등록 화면"))
        self.pw_lab.setText(_translate("AddEmployee", "비밀번호"))
        self.dept_lab.setText(_translate("AddEmployee", "부서"))
        self.pw_recheck_lab.setText(_translate("AddEmployee", "비밀번호 확인"))
        self.name_lab.setText(_translate("AddEmployee", "이름"))
        self.user_id_lab.setText(_translate("AddEmployee", "아이디"))
        self.admit_btn.setText(_translate("AddEmployee", "등록"))
        self.face_rec_btn.setText(_translate("AddEmployee", "얼굴인식"))
        self.cancel_btn.setText(_translate("AddEmployee", "취소"))
from Main.UI import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddEmployee = QtWidgets.QWidget()
    ui = Ui_AddEmployee()
    ui.setupUi(AddEmployee)
    AddEmployee.show()
    sys.exit(app.exec_())