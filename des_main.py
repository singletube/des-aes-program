from Des import Encrypt, Decrypt
import pyDes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import ast

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 288)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 100, 411, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 130, 101, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 411, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 50, 101, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 170, 411, 30))
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 220, 411, 30))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Armenian")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", 'DES'))
        self.pushButton_2.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton.setText(_translate("MainWindow", "Открыть"))
        self.pushButton_3.setText(_translate("MainWindow", "Зашифровать"))
        self.pushButton_4.setText(_translate("MainWindow", "Расшифровать"))
        self.pushButton.clicked.connect(self.OpenClick)
        self.pushButton_2.clicked.connect(self.SaveClick)
        self.pushButton_3.clicked.connect(self.clicked)
        self.pushButton_4.clicked.connect(self.dedede)

    def OpenClick(self):

        file=QFileDialog.getOpenFileName(MainWindow, None, None,"*.txt")
        f = file[0]
        self.lineEdit.setText(file[0])

    def SaveClick(self):


        file=QFileDialog.getSaveFileName(MainWindow, None, None, '*.txt')
        f = file[0]
        self.lineEdit_2.setText(file[0])




    def clicked(self):
        if not self.lineEdit.text():
            QMessageBox.critical(MainWindow, "Ошибка ", "Выберете  файлы", QMessageBox.Ok)
            return 0
        elif not self.lineEdit_2.text():
            QMessageBox.critical(MainWindow, "Ошибка ", "Выберете файлы", QMessageBox.Ok)
            return 0
        else:
            kluch, ok = QInputDialog.getText(MainWindow, 'Input Dialog','Введите ключ:')
            if len(kluch) != 8:
                QMessageBox.critical(MainWindow, "Ошибка ", "Длина ключа должна быть 8", QMessageBox.Ok)
                return 0
            if ok:

                key = (kluch)
                p = self.lineEdit.text()
                g = open(p, encoding='cp1251')

                data = (g.read()).encode(encoding='cp1251')
                cipher_text = Encrypt(key, data)

                print ("Encrypted: %r" % cipher_text)
                print ("Decrypted: %r" % (Decrypt(key, cipher_text)))


                with open(self.lineEdit_2.text(), 'w') as j:
                    j.write(str(cipher_text)[2:][:-1])

    def dedede(self):
       if not self.lineEdit.text():
           QMessageBox.critical(MainWindow, "Ошибка ", "Выберете  файлы", QMessageBox.Ok)
           return 0
       elif not self.lineEdit_2.text():
           QMessageBox.critical(MainWindow, "Ошибка ", "Выберете файлы", QMessageBox.Ok)
           return 0
       else:
           kluch, ok = QInputDialog.getText(MainWindow, 'Input Dialog','Введите ключ:')
           if len(kluch) != 8:
               QMessageBox.critical(MainWindow, "Ошибка ", "Длина ключа должна быть 8", QMessageBox.Ok)
               return 0
           if ok:

            p = self.lineEdit.text()
            g = open(p, encoding='cp1251')
            shifre = g.read()
            key = (kluch)
            cipher = ast.literal_eval('b"' + shifre + '"')
            r2 = Decrypt(key, cipher)

            j = open(self.lineEdit_2.text(), 'w')
            j.write(r2.decode(encoding='cp1251'))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
