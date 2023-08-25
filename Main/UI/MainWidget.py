# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(1120, 630)
        MainWidget.setMaximumSize(QtCore.QSize(1120, 630))
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_widget = QtWidgets.QWidget(MainWidget)
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
"QPushButton::hover{\n"
"     border-bottom: 3px solid #3C82F2;\n"
"}")
        self.top_widget.setObjectName("top_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.top_vlay = QtWidgets.QVBoxLayout()
        self.top_vlay.setObjectName("top_vlay")
        spacerItem1 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.top_vlay.addItem(spacerItem1)
        self.widget_11 = QtWidgets.QWidget(self.top_widget)
        self.widget_11.setMaximumSize(QtCore.QSize(270, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.widget_11.setFont(font)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.home_btn = QtWidgets.QPushButton(self.widget_11)
        self.home_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.home_btn.setFont(font)
        self.home_btn.setObjectName("home_btn")
        self.horizontalLayout_12.addWidget(self.home_btn)
        self.atd_btn = QtWidgets.QPushButton(self.widget_11)
        self.atd_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.atd_btn.setFont(font)
        self.atd_btn.setObjectName("atd_btn")
        self.horizontalLayout_12.addWidget(self.atd_btn)
        self.mypage_btn = QtWidgets.QPushButton(self.widget_11)
        self.mypage_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mypage_btn.setFont(font)
        self.mypage_btn.setObjectName("mypage_btn")
        self.horizontalLayout_12.addWidget(self.mypage_btn)
        self.top_vlay.addWidget(self.widget_11)
        self.horizontalLayout_2.addLayout(self.top_vlay)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.top_widget)
        self.bottom_widget = QtWidgets.QWidget(MainWidget)
        self.bottom_widget.setStyleSheet("background-color: rgb(241, 242, 246);")
        self.bottom_widget.setObjectName("bottom_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.bottom_widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.home_page)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.home_page_main_widget = QtWidgets.QWidget(self.home_page)
        self.home_page_main_widget.setObjectName("home_page_main_widget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.home_page_main_widget)
        self.verticalLayout_12.setSpacing(9)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.img_lab = QtWidgets.QLabel(self.home_page_main_widget)
        self.img_lab.setMinimumSize(QtCore.QSize(60, 60))
        self.img_lab.setMaximumSize(QtCore.QSize(60, 60))
        self.img_lab.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.img_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.img_lab.setObjectName("img_lab")
        self.horizontalLayout_7.addWidget(self.img_lab)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.home_name_lab = QtWidgets.QLabel(self.home_page_main_widget)
        self.home_name_lab.setMaximumSize(QtCore.QSize(16777215, 30))
        self.home_name_lab.setObjectName("home_name_lab")
        self.verticalLayout_11.addWidget(self.home_name_lab)
        self.home_dept_lab = QtWidgets.QLabel(self.home_page_main_widget)
        self.home_dept_lab.setMaximumSize(QtCore.QSize(16777215, 30))
        self.home_dept_lab.setObjectName("home_dept_lab")
        self.verticalLayout_11.addWidget(self.home_dept_lab)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)
        self.out_btn = QtWidgets.QPushButton(self.home_page_main_widget)
        self.out_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.out_btn.setStyleSheet("#out_btn{\n"
"border-radius:10px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.out_btn.setObjectName("out_btn")
        self.horizontalLayout_7.addWidget(self.out_btn)
        self.end_btn = QtWidgets.QPushButton(self.home_page_main_widget)
        self.end_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.end_btn.setStyleSheet("border-radius:10px;\n"
"border: 1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.end_btn.setObjectName("end_btn")
        self.horizontalLayout_7.addWidget(self.end_btn)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.home_bottom_widget = QtWidgets.QWidget(self.home_page_main_widget)
        self.home_bottom_widget.setObjectName("home_bottom_widget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.home_bottom_widget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_3 = QtWidgets.QWidget(self.home_bottom_widget)
        self.widget_3.setMinimumSize(QtCore.QSize(250, 100))
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(20, 14, 16, 14)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setMinimumSize(QtCore.QSize(60, 60))
        self.label_9.setMaximumSize(QtCore.QSize(60, 60))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setStyleSheet("border-radius:30px;\n"
"background-color: rgb(230, 234, 245);")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/attendance.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.horizontalLayout_5.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.home_bottom_widget)
        self.widget_2.setMinimumSize(QtCore.QSize(250, 100))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(20, 14, 16, 14)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setMinimumSize(QtCore.QSize(60, 60))
        self.label_6.setMaximumSize(QtCore.QSize(60, 60))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet("border-radius:30px;\n"
"background-color: rgb(230, 234, 245);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/out.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_5.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.home_bottom_widget)
        self.widget.setMinimumSize(QtCore.QSize(250, 100))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(20, 14, 16, 14)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(60, 60))
        self.label_3.setMaximumSize(QtCore.QSize(60, 60))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("border-radius:30px;\n"
"background-color: rgb(230, 234, 245);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/absent.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalLayout_5.addWidget(self.widget)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem8)
        self.widget_5 = QtWidgets.QWidget(self.home_bottom_widget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 236))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 240))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.label_10 = QtWidgets.QLabel(self.widget_6)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.horizontalLayout_6.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.label_11 = QtWidgets.QLabel(self.widget_7)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.horizontalLayout_6.addWidget(self.widget_7)
        self.verticalLayout_10.addWidget(self.widget_5)
        self.verticalLayout_12.addWidget(self.home_bottom_widget)
        self.horizontalLayout_9.addWidget(self.home_page_main_widget)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.stackedWidget.addWidget(self.home_page)
        self.atd_page = QtWidgets.QWidget()
        self.atd_page.setObjectName("atd_page")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.atd_page)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem10 = QtWidgets.QSpacerItem(61, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_13.addItem(spacerItem11)
        self.widget_9 = QtWidgets.QWidget(self.atd_page)
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setPointSize(4)
        self.widget_9.setFont(font)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem12 = QtWidgets.QSpacerItem(649, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.label_16 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_11.addWidget(self.label_16)
        self.comboBox = QtWidgets.QComboBox(self.widget_9)
        self.comboBox.setMinimumSize(QtCore.QSize(156, 41))
        self.comboBox.setStyleSheet("#comboBox{\n"
"    border-radius:10px;\n"
"    background-color: rgb(217, 217, 217);\n"
"    padding-left:10px;}\n"
"\n"
"#comboBox::drop-down{\n"
"    border:0px;\n"
"}\n"
"\n"
"#comboBox::down-arrow{\n"
"    image: url(:/down.png);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    margin-right:15px;\n"
"}\n"
"#comboBox::on{\n"
" border:4px solid gray;\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.widget_9)
        self.pushButton.setMinimumSize(QtCore.QSize(66, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(217, 217, 217);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_11.addWidget(self.pushButton)
        self.verticalLayout_13.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(self.atd_page)
        self.widget_10.setMaximumSize(QtCore.QSize(16777215, 280))
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_10)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 280))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_14.addWidget(self.tableWidget)
        self.verticalLayout_13.addWidget(self.widget_10)
        self.label_15 = QtWidgets.QLabel(self.atd_page)
        self.label_15.setMinimumSize(QtCore.QSize(960, 0))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 54))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_13.addWidget(self.label_15)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_13.addItem(spacerItem13)
        self.horizontalLayout_10.addLayout(self.verticalLayout_13)
        spacerItem14 = QtWidgets.QSpacerItem(61, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem14)
        self.stackedWidget.addWidget(self.atd_page)
        self.my_page = QtWidgets.QWidget()
        self.my_page.setStyleSheet("QLineEdit{\n"
"height: 40px;\n"
"border-radius: 10px;\n"
"border: 1px solid #3085FE;\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QComboBox{\n"
"height: 40px;\n"
"\n"
"}\n"
"")
        self.my_page.setObjectName("my_page")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.my_page)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.my_page_main_widget = QtWidgets.QWidget(self.my_page)
        self.my_page_main_widget.setObjectName("my_page_main_widget")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.my_page_main_widget)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.widget_13 = QtWidgets.QWidget(self.my_page_main_widget)
        self.widget_13.setMaximumSize(QtCore.QSize(16777215, 380))
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_13.setContentsMargins(120, -1, 120, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.my_img_lab = QtWidgets.QLabel(self.widget_13)
        self.my_img_lab.setMinimumSize(QtCore.QSize(230, 230))
        self.my_img_lab.setMaximumSize(QtCore.QSize(230, 230))
        self.my_img_lab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.my_img_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.my_img_lab.setObjectName("my_img_lab")
        self.horizontalLayout_13.addWidget(self.my_img_lab)
        spacerItem15 = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem15)
        self.line = QtWidgets.QFrame(self.widget_13)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_13.addWidget(self.line)
        spacerItem16 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem16)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.name_lineedit = QtWidgets.QLineEdit(self.widget_13)
        self.name_lineedit.setMinimumSize(QtCore.QSize(300, 0))
        self.name_lineedit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_lineedit.setFont(font)
        self.name_lineedit.setObjectName("name_lineedit")
        self.gridLayout.addWidget(self.name_lineedit, 1, 1, 1, 1)
        self.dept_combobox = QtWidgets.QComboBox(self.widget_13)
        self.dept_combobox.setMinimumSize(QtCore.QSize(300, 0))
        self.dept_combobox.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dept_combobox.setFont(font)
        self.dept_combobox.setStyleSheet("#dept_combobox{\n"
"    border-radius:10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid #3085FE;\n"
"    padding-left:10px;}\n"
"\n"
"#dept_combobox::drop-down{\n"
"    border:0px;\n"
"}\n"
"\n"
"#dept_combobox::down-arrow{\n"
"    image: url(:/down.png);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    margin-right:15px;\n"
"}\n"
"#dept_combobox::on{\n"
" border:4px solid gray;\n"
"}\n"
"")
        self.dept_combobox.setObjectName("dept_combobox")
        self.gridLayout.addWidget(self.dept_combobox, 2, 1, 1, 1)
        self.pw_lab = QtWidgets.QLabel(self.widget_13)
        self.pw_lab.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pw_lab.setFont(font)
        self.pw_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.pw_lab.setObjectName("pw_lab")
        self.gridLayout.addWidget(self.pw_lab, 4, 0, 1, 1)
        self.user_id_lab = QtWidgets.QLabel(self.widget_13)
        self.user_id_lab.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_id_lab.setFont(font)
        self.user_id_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.user_id_lab.setObjectName("user_id_lab")
        self.gridLayout.addWidget(self.user_id_lab, 3, 0, 1, 1)
        self.pw_recheck_lineedit = QtWidgets.QLineEdit(self.widget_13)
        self.pw_recheck_lineedit.setMinimumSize(QtCore.QSize(300, 0))
        self.pw_recheck_lineedit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pw_recheck_lineedit.setFont(font)
        self.pw_recheck_lineedit.setObjectName("pw_recheck_lineedit")
        self.gridLayout.addWidget(self.pw_recheck_lineedit, 5, 1, 1, 1)
        self.dept_lab = QtWidgets.QLabel(self.widget_13)
        self.dept_lab.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dept_lab.setFont(font)
        self.dept_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.dept_lab.setObjectName("dept_lab")
        self.gridLayout.addWidget(self.dept_lab, 2, 0, 1, 1)
        self.name_lab = QtWidgets.QLabel(self.widget_13)
        self.name_lab.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_lab.setFont(font)
        self.name_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lab.setObjectName("name_lab")
        self.gridLayout.addWidget(self.name_lab, 1, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.widget_13)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 0, 0, 1, 1)
        self.user_id_lineedit = QtWidgets.QLineEdit(self.widget_13)
        self.user_id_lineedit.setMinimumSize(QtCore.QSize(300, 0))
        self.user_id_lineedit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_id_lineedit.setFont(font)
        self.user_id_lineedit.setObjectName("user_id_lineedit")
        self.gridLayout.addWidget(self.user_id_lineedit, 3, 1, 1, 1)
        self.pw_lineedit = QtWidgets.QLineEdit(self.widget_13)
        self.pw_lineedit.setMinimumSize(QtCore.QSize(300, 0))
        self.pw_lineedit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pw_lineedit.setFont(font)
        self.pw_lineedit.setObjectName("pw_lineedit")
        self.gridLayout.addWidget(self.pw_lineedit, 4, 1, 1, 1)
        self.pw_recheck_lab = QtWidgets.QLabel(self.widget_13)
        self.pw_recheck_lab.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pw_recheck_lab.setFont(font)
        self.pw_recheck_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.pw_recheck_lab.setObjectName("pw_recheck_lab")
        self.gridLayout.addWidget(self.pw_recheck_lab, 5, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget_13)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 6, 0, 1, 1)
        self.horizontalLayout_13.addLayout(self.gridLayout)
        self.verticalLayout_15.addWidget(self.widget_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.edit_btn = QtWidgets.QPushButton(self.my_page_main_widget)
        self.edit_btn.setMinimumSize(QtCore.QSize(300, 40))
        self.edit_btn.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.edit_btn.setFont(font)
        self.edit_btn.setStyleSheet("background-color: rgb(48, 133, 254);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.edit_btn.setObjectName("edit_btn")
        self.horizontalLayout_14.addWidget(self.edit_btn)
        self.verticalLayout_15.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15.addWidget(self.my_page_main_widget)
        self.stackedWidget.addWidget(self.my_page)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.bottom_widget)

        self.retranslateUi(MainWidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Form"))
        self.home_btn.setText(_translate("MainWidget", "홈"))
        self.atd_btn.setText(_translate("MainWidget", "근태화면"))
        self.mypage_btn.setText(_translate("MainWidget", "마이페이지"))
        self.img_lab.setText(_translate("MainWidget", "이미지"))
        self.home_name_lab.setText(_translate("MainWidget", "이름이름"))
        self.home_dept_lab.setText(_translate("MainWidget", "부서부서"))
        self.out_btn.setText(_translate("MainWidget", "외출하기"))
        self.end_btn.setText(_translate("MainWidget", "퇴근하기"))
        self.label_7.setText(_translate("MainWidget", "00일"))
        self.label_8.setText(_translate("MainWidget", "출근일"))
        self.label_4.setText(_translate("MainWidget", "00일"))
        self.label_5.setText(_translate("MainWidget", "외출일"))
        self.label.setText(_translate("MainWidget", "00일"))
        self.label_2.setText(_translate("MainWidget", "결근일"))
        self.label_10.setText(_translate("MainWidget", "그래프에 대한 설명"))
        self.label_11.setText(_translate("MainWidget", "그래프에 대한 설명"))
        self.label_16.setText(_translate("MainWidget", "월별조회"))
        self.comboBox.setItemText(0, _translate("MainWidget", "테스트"))
        self.comboBox.setItemText(1, _translate("MainWidget", "테스트"))
        self.pushButton.setText(_translate("MainWidget", "확인"))
        self.label_15.setText(_translate("MainWidget", "000님의 0월 출근일수는 00일, 근태율은 00%입니다."))
        self.my_img_lab.setText(_translate("MainWidget", "이미지"))
        self.pw_lab.setText(_translate("MainWidget", "비밀번호"))
        self.user_id_lab.setText(_translate("MainWidget", "아이디"))
        self.dept_lab.setText(_translate("MainWidget", "부서"))
        self.name_lab.setText(_translate("MainWidget", "이름"))
        self.pw_recheck_lab.setText(_translate("MainWidget", "비밀번호 확인"))
        self.edit_btn.setText(_translate("MainWidget", "수정하기"))
from Main.UI import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWidget = QtWidgets.QWidget()
    ui = Ui_MainWidget()
    ui.setupUi(MainWidget)
    MainWidget.show()
    sys.exit(app.exec_())
