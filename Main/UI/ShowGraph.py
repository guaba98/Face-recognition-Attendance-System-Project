# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowGraph(object):
    def setupUi(self, ShowGraph):
        ShowGraph.setObjectName("ShowGraph")
        ShowGraph.resize(840, 485)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ShowGraph)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(ShowGraph)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(ShowGraph)
        QtCore.QMetaObject.connectSlotsByName(ShowGraph)

    def retranslateUi(self, ShowGraph):
        _translate = QtCore.QCoreApplication.translate
        ShowGraph.setWindowTitle(_translate("ShowGraph", "Dialog"))
        self.pushButton.setText(_translate("ShowGraph", "닫기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShowGraph = QtWidgets.QDialog()
    ui = Ui_ShowGraph()
    ui.setupUi(ShowGraph)
    ShowGraph.show()
    sys.exit(app.exec_())