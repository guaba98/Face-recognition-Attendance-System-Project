# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Opening.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Opening(object):
    def setupUi(self, Opening):
        Opening.setObjectName("Opening")
        Opening.resize(1120, 630)
        self.label = QtWidgets.QLabel(Opening)
        self.label.setGeometry(QtCore.QRect(260, 100, 651, 341))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Opening)
        QtCore.QMetaObject.connectSlotsByName(Opening)

    def retranslateUi(self, Opening):
        _translate = QtCore.QCoreApplication.translate
        Opening.setWindowTitle(_translate("Opening", "Form"))
        self.label.setText(_translate("Opening", "로딩중이오 잠시만 기다리소 \n"
"그렇게 급하면 어제 키지 그랬소"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Opening = QtWidgets.QWidget()
    ui = Ui_Opening()
    ui.setupUi(Opening)
    Opening.show()
    sys.exit(app.exec_())