# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'answer.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Answer(object):
    def setupUi(self, Answer):
        Answer.setObjectName("Answer")
        Answer.resize(622, 461)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Answer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.resultsToolBox = QtWidgets.QToolBox(Answer)
        self.resultsToolBox.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.resultsToolBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.resultsToolBox.setObjectName("resultsToolBox")
        self.bloodResultsPage = QtWidgets.QWidget()
        self.bloodResultsPage.setGeometry(QtCore.QRect(0, 0, 608, 190))
        self.bloodResultsPage.setObjectName("bloodResultsPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.bloodResultsPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bloodTextEdit = QtWidgets.QTextEdit(self.bloodResultsPage)
        self.bloodTextEdit.setReadOnly(True)
        self.bloodTextEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.bloodTextEdit.setOverwriteMode(False)
        self.bloodTextEdit.setTabStopWidth(78)
        self.bloodTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.bloodTextEdit.setObjectName("bloodTextEdit")
        self.verticalLayout_3.addWidget(self.bloodTextEdit)
        self.resultsToolBox.addItem(self.bloodResultsPage, "")
        self.renalResultsPage = QtWidgets.QWidget()
        self.renalResultsPage.setGeometry(QtCore.QRect(0, 0, 608, 190))
        self.renalResultsPage.setObjectName("renalResultsPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.renalResultsPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.renalTextEdit = QtWidgets.QTextEdit(self.renalResultsPage)
        self.renalTextEdit.setReadOnly(True)
        self.renalTextEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.renalTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.renalTextEdit.setObjectName("renalTextEdit")
        self.verticalLayout_4.addWidget(self.renalTextEdit)
        self.resultsToolBox.addItem(self.renalResultsPage, "")
        self.liverResultsPage = QtWidgets.QWidget()
        self.liverResultsPage.setGeometry(QtCore.QRect(0, 0, 608, 190))
        self.liverResultsPage.setObjectName("liverResultsPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.liverResultsPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.liverTextEdit = QtWidgets.QTextEdit(self.liverResultsPage)
        self.liverTextEdit.setReadOnly(True)
        self.liverTextEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.liverTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.liverTextEdit.setObjectName("liverTextEdit")
        self.verticalLayout_5.addWidget(self.liverTextEdit)
        self.resultsToolBox.addItem(self.liverResultsPage, "")
        self.thyroidResultsPage = QtWidgets.QWidget()
        self.thyroidResultsPage.setGeometry(QtCore.QRect(0, 0, 608, 190))
        self.thyroidResultsPage.setObjectName("thyroidResultsPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.thyroidResultsPage)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.thyroidTextEdit = QtWidgets.QTextEdit(self.thyroidResultsPage)
        self.thyroidTextEdit.setReadOnly(True)
        self.thyroidTextEdit.setObjectName("thyroidTextEdit")
        self.verticalLayout_6.addWidget(self.thyroidTextEdit)
        self.resultsToolBox.addItem(self.thyroidResultsPage, "")
        self.electrolyteResultsPage = QtWidgets.QWidget()
        self.electrolyteResultsPage.setGeometry(QtCore.QRect(0, 0, 608, 190))
        self.electrolyteResultsPage.setObjectName("electrolyteResultsPage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.electrolyteResultsPage)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.electrolyteTextEdit = QtWidgets.QTextEdit(self.electrolyteResultsPage)
        self.electrolyteTextEdit.setReadOnly(True)
        self.electrolyteTextEdit.setObjectName("electrolyteTextEdit")
        self.verticalLayout_7.addWidget(self.electrolyteTextEdit)
        self.resultsToolBox.addItem(self.electrolyteResultsPage, "")
        self.lipidResultsPage = QtWidgets.QWidget()
        self.lipidResultsPage.setGeometry(QtCore.QRect(0, 0, 608, 190))
        self.lipidResultsPage.setObjectName("lipidResultsPage")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.lipidResultsPage)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lipidTextEdit = QtWidgets.QTextEdit(self.lipidResultsPage)
        self.lipidTextEdit.setReadOnly(True)
        self.lipidTextEdit.setObjectName("lipidTextEdit")
        self.verticalLayout_8.addWidget(self.lipidTextEdit)
        self.resultsToolBox.addItem(self.lipidResultsPage, "")
        self.verticalLayout.addWidget(self.resultsToolBox)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.returnBtn = QtWidgets.QPushButton(Answer)
        self.returnBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.returnBtn.setToolTipDuration(10)
        self.returnBtn.setObjectName("returnBtn")
        self.horizontalLayout.addWidget(self.returnBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.fontComboBox = QtWidgets.QFontComboBox(Answer)
        self.fontComboBox.setToolTipDuration(10)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout.addWidget(self.fontComboBox)
        self.printBtn = QtWidgets.QPushButton(Answer)
        self.printBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.printBtn.setToolTipDuration(10)
        self.printBtn.setObjectName("printBtn")
        self.horizontalLayout.addWidget(self.printBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Answer)
        self.resultsToolBox.setCurrentIndex(5)
        self.fontComboBox.currentIndexChanged['QString'].connect(self.renalTextEdit.setFontFamily)
        self.fontComboBox.currentIndexChanged['QString'].connect(self.liverTextEdit.setFontFamily)
        self.fontComboBox.currentIndexChanged['QString'].connect(self.thyroidTextEdit.setFontFamily)
        self.fontComboBox.currentIndexChanged['QString'].connect(self.electrolyteTextEdit.setFontFamily)
        self.fontComboBox.currentIndexChanged['QString'].connect(self.lipidTextEdit.setFontFamily)
        self.fontComboBox.currentTextChanged['QString'].connect(self.bloodTextEdit.setFontFamily)
        self.returnBtn.pressed.connect(Answer.close)
        QtCore.QMetaObject.connectSlotsByName(Answer)

    def retranslateUi(self, Answer):
        _translate = QtCore.QCoreApplication.translate
        Answer.setWindowTitle(_translate("Answer", "Results"))
        self.resultsToolBox.setToolTip(_translate("Answer", "Click on the tab of your choice to expand and show the results"))
        self.resultsToolBox.setItemText(self.resultsToolBox.indexOf(self.bloodResultsPage), _translate("Answer", "Complete Blood Count"))
        self.resultsToolBox.setItemToolTip(self.resultsToolBox.indexOf(self.bloodResultsPage), _translate("Answer", "Click on this page, to check informations about your blood tests result"))
        self.resultsToolBox.setItemText(self.resultsToolBox.indexOf(self.renalResultsPage), _translate("Answer", "Renal Panel"))
        self.resultsToolBox.setItemToolTip(self.resultsToolBox.indexOf(self.renalResultsPage), _translate("Answer", "Click on this page, to check informations about your urine tests result"))
        self.resultsToolBox.setItemText(self.resultsToolBox.indexOf(self.liverResultsPage), _translate("Answer", "Liver Panel"))
        self.resultsToolBox.setItemToolTip(self.resultsToolBox.indexOf(self.liverResultsPage), _translate("Answer", "Click on this page, to check informations about your liver tests result"))
        self.resultsToolBox.setItemText(self.resultsToolBox.indexOf(self.thyroidResultsPage), _translate("Answer", "Thyroid Panel"))
        self.resultsToolBox.setItemText(self.resultsToolBox.indexOf(self.electrolyteResultsPage), _translate("Answer", "Electrolyte Panel"))
        self.resultsToolBox.setItemText(self.resultsToolBox.indexOf(self.lipidResultsPage), _translate("Answer", "Lipid Panel"))
        self.returnBtn.setToolTip(_translate("Answer", "Click here, if you want to return to main window"))
        self.returnBtn.setText(_translate("Answer", "Return"))
        self.fontComboBox.setToolTip(_translate("Answer", "Choose3 your font type for printing"))
        self.printBtn.setToolTip(_translate("Answer", "Click here, if you want to print all informations about your tests"))
        self.printBtn.setText(_translate("Answer", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Answer = QtWidgets.QWidget()
    ui = Ui_Answer()
    ui.setupUi(Answer)
    Answer.show()
    sys.exit(app.exec_())
