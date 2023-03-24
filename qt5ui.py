# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'img-compress.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ReduceImage import ReduceImage
import time

class Ui_RadishImageTool(object):
    # 防止重复点击
    lock = False
    def setupUi(self, RadishImageTool):
        RadishImageTool.setObjectName("RadishImageTool")
        RadishImageTool.resize(490, 481)
        self.centralwidget = QtWidgets.QWidget(RadishImageTool)
        self.centralwidget.setObjectName("centralwidget")
        # self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        # self.comboBox.setGeometry(QtCore.QRect(20, 20, 111, 31))
        # self.comboBox.setObjectName("comboBox")
        # self.comboBox.addItem("")
        # self.comboBox.addItem("")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(290, 130, 171, 51))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        # 点击事件
        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.cancel)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 70, 400, 21))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 110, 400, 21))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 61, 31))
        self.lineEdit.setToolTip("")
        self.lineEdit.setText("80")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 20, 61, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText("0")
        # self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit_3.setGeometry(QtCore.QRect(394, 20, 61, 31))
        # self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 26, 160, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 41, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 20, 51, 31))
        self.label_5.setObjectName("label_5")
        RadishImageTool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RadishImageTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 469, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        RadishImageTool.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RadishImageTool)
        self.statusbar.setObjectName("statusbar")
        RadishImageTool.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(5, 181, 481, 231))
        self.listWidget.setObjectName("listWidget")
        # 选择文件
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(20, 60, 91, 31))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(20, 100, 91, 31))
        self.toolButton_2.setObjectName("toolButton_2")

        self.retranslateUi(RadishImageTool)
        QtCore.QMetaObject.connectSlotsByName(RadishImageTool)

        # 按钮点击事件回调
        self.toolButton.clicked.connect(self.clickPath)
        self.toolButton_2.clicked.connect(self.clickPathNew)

    def retranslateUi(self, RadishImageTool):
        _translate = QtCore.QCoreApplication.translate
        RadishImageTool.setWindowTitle(_translate("RadishImageTool", "图片工具"))
        # self.comboBox.setItemText(0, _translate("RadishImageTool", "压缩体积"))
        # self.comboBox.setItemText(1, _translate("RadishImageTool", "压缩尺寸"))
        self.toolButton.setText(_translate("RadishImageTool", "图片所在目录"))
        self.toolButton_2.setText(_translate("RadishImageTool", "图片输出目录"))
        self.label_3.setText(_translate("RadishImageTool", "等比例压缩，按最高尺寸执行"))
        self.label_4.setText(_translate("RadishImageTool", "百分比："))
        self.label_5.setText(_translate("RadishImageTool", "宽高(px)："))
        self.menu.setTitle(_translate("RadishImageTool", "图片处理"))
    
    def clickPath(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "")  # 起始路径
        self.label.setText(m)

    def clickPathNew(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "")  # 起始路径
        self.label_2.setText(m + "/new_" + time.strftime("%y%m%d%H%M%S"))

    def ok(self):
        if self.lock == True:
            QMessageBox.about(self.centralwidget, "提示", "程序还在执行中！！！")
            return
        else:
            self.lock = True
        img = ReduceImage()
        img.infoCon = self.listWidget
        img.inputDir = self.label.text()
        img.outDir = self.label_2.text()
        try:
            img.size = int(self.lineEdit_2.text())
            img.quality = int(self.lineEdit.text())
        except Exception as e:
            QMessageBox.about(self.centralwidget, "提示", "输入框只支持整数！")
            self.lock = False
            return
        if len(img.inputDir) <= 0 or len(img.outDir) <= 0:
            QMessageBox.about(self.centralwidget, "提示", "请选择路径!")
            self.lock = False
        elif img.quality < 0 or img.quality > 100:
            QMessageBox.about(self.centralwidget, "提示", "【百分比】必须大于0小于100的整数!")
            self.lock = False
        else:
            self.listWidget.clear()
            img.ergodicDir(img.inputDir)
            self.lock = False
    def cancel(self):
        if self.lock == True:
            QMessageBox.about(self.centralwidget, "提示", "程序还在执行中！！！")
        else:
            self.listWidget.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RadishImageTool = QtWidgets.QMainWindow()
    ui = Ui_RadishImageTool()
    ui.setupUi(RadishImageTool)
    RadishImageTool.show()
    sys.exit(app.exec_())