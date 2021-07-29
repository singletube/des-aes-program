import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QFileDialog, QVBoxLayout, QScrollArea,
                             QMessageBox, QApplication)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Obuchenie = QtWidgets.QLabel(self.centralwidget)
        self.Obuchenie.setGeometry(QtCore.QRect(20, 20, 1081, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Obuchenie.setFont(font)
        self.Obuchenie.setObjectName("Obuchenie")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 281, 519))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Aes_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.Aes_label.setFont(font)
        self.Aes_label.setObjectName("Aes_label")
        self.verticalLayout_2.addWidget(self.Aes_label)
        self.Aes_teory = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Aes_teory.setFont(font)
        self.Aes_teory.setObjectName("Aes_teory")
        self.verticalLayout_2.addWidget(self.Aes_teory)
        self.Aes_test = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Aes_test.setFont(font)
        self.Aes_test.setObjectName("Aes_test")
        self.verticalLayout_2.addWidget(self.Aes_test)
        self.Aes_zadani = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Aes_zadani.setFont(font)
        self.Aes_zadani.setObjectName("Aes_zadani")
        self.verticalLayout_2.addWidget(self.Aes_zadani)
        self.Des_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.Des_label.setFont(font)
        self.Des_label.setObjectName("Des_label")
        self.verticalLayout_2.addWidget(self.Des_label)
        self.des_teory = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.des_teory.setFont(font)
        self.des_teory.setObjectName("des_teory")
        self.verticalLayout_2.addWidget(self.des_teory)
        self.des_test = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.des_test.setFont(font)
        self.des_test.setObjectName("des_test")
        self.verticalLayout_2.addWidget(self.des_test)
        self.des_zadanie = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.des_zadanie.setFont(font)
        self.des_zadanie.setObjectName("des_zadanie")
        self.verticalLayout_2.addWidget(self.des_zadanie)
        self.main_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.main_text.setGeometry(QtCore.QRect(310, 80, 961, 591))
        self.main_text.setObjectName("main_text")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(310, 80, 961, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 270, 961, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.a1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.a1.setFont(font)
        self.a1.setObjectName("a1")
        self.verticalLayout.addWidget(self.a1)
        self.a2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.a2.setFont(font)
        self.a2.setObjectName("a2")
        self.verticalLayout.addWidget(self.a2)
        self.a3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.a3.setFont(font)
        self.a3.setObjectName("a3")
        self.verticalLayout.addWidget(self.a3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 570, 961, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(310, 630, 961, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Obuchenie.setText(_translate("MainWindow", "Обучение симетричным алгоритмам шифрования DES и AES"))
        self.Aes_label.setText(_translate("MainWindow", "AES"))
        self.Aes_teory.setText(_translate("MainWindow", "Теория"))
        self.Aes_test.setText(_translate("MainWindow", "Тест"))
        self.Aes_zadani.setText(_translate("MainWindow", "Задания"))
        self.Des_label.setText(_translate("MainWindow", "DES"))
        self.des_teory.setText(_translate("MainWindow", "Теория"))
        self.des_test.setText(_translate("MainWindow", "Тест"))
        self.des_zadanie.setText(_translate("MainWindow", "Задания"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600;\">Вопрос: 1</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:14pt;\">o</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">   </span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:14pt; font-weight:600;\">алгоритм для симметричного шифрования, разработанный фирмой IBM и утверждённый правительством США в 1977 году как официальный стандарт (FIPS 46-3)</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></body></html>"))
        self.a1.setText(_translate("MainWindow", "Ответ 1"))
        self.a2.setText(_translate("MainWindow", "Ответ 1"))
        self.a3.setText(_translate("MainWindow", "Ответ 1"))
        self.pushButton.setText(_translate("MainWindow", "Следующий вопрос"))



class Widget(QWidget):
    def __init__(self, parent, name_file):
        super(Widget, self).__init__(parent)
        self.setFixedSize(800, 600)

        widget = QWidget()
        layout = QVBoxLayout(self)
        pixmap = QPixmap(name_file)
        image = QtWidgets.QLabel()
        image.setPixmap(pixmap)
        layout.addWidget(image)
        widget.setLayout(layout)
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        self.setLayout(vLayout)

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1280, 720)

        self.all_answ = []
        self.DesT = Widget(self.centralwidget, 'Desteory.png')
        self.DesT.setGeometry(QtCore.QRect(350, 90, 961, 591))
        self.DesT.hide()
        self.AesT = Widget(self.centralwidget, 'Aesteory.png')
        self.AesT.setGeometry(QtCore.QRect(350, 90, 961, 591))
        self.AesT.hide()
        self.AesZ = Widget(self.centralwidget, 'Aesz.png')
        self.AesZ.setGeometry(QtCore.QRect(350, 90, 961, 591))
        self.AesZ.hide()
        self.DesZ = Widget(self.centralwidget, 'Desz.png')
        self.DesZ.setGeometry(QtCore.QRect(350, 90, 961, 591))
        self.DesZ.hide()
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.a1)
        self.button_group.addButton(self.a2)
        self.button_group.addButton(self.a3)
        self.main_text.hide()
        self.textBrowser.setReadOnly(True)
        self.des_test.clicked.connect(self.des_test_started)
        self.Aes_test.clicked.connect(self.aes_test_started)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)
        self.pushButton.clicked.connect(self.next_q)
        self.Aes_teory.clicked.connect(self.read_teory)
        self.Aes_zadani.clicked.connect(self.read_teory)
        self.des_teory.clicked.connect(self.read_teory)
        self.des_zadanie.clicked.connect(self.read_teory)
        self.pushButton.hide()
        self.progress = 0
        self.Obuchenie.hide()

        self.textBrowser.setText('')
        self.des = ['DES – это', 'Размер блока для DES равен: ', 'В основе алгоритма лежит сеть Фейстеля с: ',
                    'Ключ имеет длину:', 'Сколько существует перестановок в стандарте DES:',
                    'Какие перестановки существуют в стандарте DES', 'Как называется модификация DESa']
        self.des_answers = [['алгоритм для симметричного шифрования, разработанный фирмой IBM\n и утверждённый правительством США в 1977 году как официальный\n стандарт (FIPS 46-3)',
                             'симметричный алгоритм блочного шифрования\n (размер блока 128 бит, ключ 128/192/256 бит),\n принятый в качестве стандарта шифрования правительством\n США по результатам конкурса AES',
                             '-----------------'], ['36 бит', '64 бит', '84 бит'], ['14 циклами', '16 циклами', '18 циклами'],
                            ['64 бит', '56 бит', '36 бит'], ['3', '4', '2'], ['Расширенные, Простые', 'Расширенные, Простые, Сокращенные', 'Простые, Сокращенные'],
                            ['Triple Des', 'М-506', 'Deh']]

        self.aes = ['AES – это', 'Размер блока в AES:', 'Размер ключа в AES может быть', 'Что такое SubBytes?',
                    'Поддержка ускорения AES была введена фирмой Intel в семейство процессоров:', 'От размера ключа зависит',
                    'AES зашифровывает и расшифровывает']

        self.aes_answers = [['криптографический алгоритм, реализующий блочное симметричное\n шифрование с переменной длиной ключа. Разработан Брюсом \nШнайером в 1993 году. Представляет собой сеть Фейстеля. Выполнен на простых\n и быстрых операциях: XOR, подстановка, сложение.',
                             'алгоритм для симметричного шифрования, разработанный фирмой \nIBM и утверждённый правительством США в 1977 году как официальный\n стандарт (FIPS 46-3)',
                             'симметричный алгоритм блочного шифрования (размер блока 128 бит, ключ \n128/192/256 бит), принятый в качестве стандарта \nшифрования правительством США'],
                            ['256 бит', '128 бит', '64 бит'], ['64/156/284', '128/192/256', '16/36/64'],
                            ['побайтовая подстановка в S-боксе с фиксированной таблицей замен', 'перемешивание байтов в столбцах',
                             'побайтовый сдвиг строк матрицы State на различное количество байт'],
                            ['x86', 'x97', 'x75'], ['число раундов шифрования', 'количество матриц', 'размер блока'],
                            ['256-битовые блоки данных', '192-битовые блоки данных', '128-битовые блоки данных']]

        self.a1.hide()
        self.a2.hide()
        self.a3.hide()
        self.progressBar.hide()
        self.textBrowser.hide()



    def des_test_started(self):
        self.Disable_all()
        self.progress = 0
        self.shifr = 'des'
        self.AesT.hide()
        self.DesT.hide()
        self.AesZ.hide()
        self.DesZ.hide()


        self.a1.show()
        self.a2.show()
        self.a3.show()
        self.progressBar.show()
        self.textBrowser.show()
        self.Make_qest(self.shifr, self.progress)

    def aes_test_started(self):
        self.AesT.hide()
        self.DesT.hide()
        self.AesZ.hide()
        self.DesZ.hide()
        self.Disable_all()
        self.progress = 0
        self.shifr = 'aes'
        self.a1.show()
        self.a2.show()
        self.a3.show()
        self.progressBar.show()
        self.textBrowser.show()
        self.Make_qest(self.shifr, self.progress)

    def Make_qest(self, shifr, num):
        if shifr == 'des':
            a = ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                 f" text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600;\">Вопрос: {num + 1}</span></p>\n"
                 '<p> </p>\n'
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                 "text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:14pt;\">o</span><span style=\""
                 " font-family:\'Times New Roman\'; font-size:7pt;\">   </span><span style=\" font-family:\'"
                 f"Times New Roman\',\'serif\'; font-size:14pt; font-weight:600;\">{self.des[num]}"
                 "</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></body></html>")

            answers = self.des_answers[num]
        else:
            a = ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                 "p, li { white-space: pre-wrap; }\n"
                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                 f" text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600;\">Вопрос: {num + 1}</span></p>\n"
                 '<p> </p>\n'
                 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                 "text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:14pt;\">o</span><span style=\""
                 " font-family:\'Times New Roman\'; font-size:7pt;\">   </span><span style=\" font-family:\'"
                 f"Times New Roman\',\'serif\'; font-size:14pt; font-weight:600;\">{self.aes[num]}"
                 "</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></body></html>")

            answers = self.aes_answers[num]
        self.textBrowser.setHtml(a)
        b = [self.a1, self.a2, self.a3]
        for i in range(3):
            b[i].setText(answers[i])

    def _on_radio_button_clicked(self):
        self.pushButton.show()

    def final_check(self, shifr):
        if shifr == 'des':
            a = ['a1', 'a2', 'a2', 'a2', 'a1', 'a2', 'a1']
            count = 0
            for i in range(7):
                if self.all_answ[i] == a[i]:
                    count += 1
        if shifr == 'aes':
            a = ['a3', 'a2', 'a2', 'a1', 'a1', 'a1', 'a3']
            count = 0
            for i in range(7):
                if self.all_answ[i] == a[i]:
                    count += 1
        return count


    def read_teory(self, sendler):

        if self.sender().objectName() == 'Aes_teory':
            self.AesT.show()
            self.DesT.hide()
            self.AesZ.hide()
            self.DesZ.hide()
        elif self.sender().objectName() == 'Aes_zadani':
            self.AesT.hide()
            self.DesT.hide()
            self.AesZ.show()
            self.DesZ.hide()
        elif self.sender().objectName() == 'des_teory':
            self.AesT.hide()
            self.DesT.show()
            self.AesZ.hide()
            self.DesZ.hide()
        elif self.sender().objectName() == 'des_zadanie':
            self.AesT.hide()
            self.DesT.hide()
            self.AesZ.hide()
            self.DesZ.show()



    def next_q(self):
        self.progress += 1
        if self.progress < 7:
            self.progressBar.setValue(15 * self.progress)
            a = self.button_group.checkedButton().objectName()
            self.all_answ.append(a)
            self.button_group.setExclusive(False)
            self.a1.setChecked(False)
            self.a2.setChecked(False)
            self.a3.setChecked(False)
            self.button_group.setExclusive(True)
            self.Make_qest(self.shifr, self.progress)
            self.pushButton.hide()
        else:
            a = self.button_group.checkedButton().objectName()
            self.all_answ.append(a)
            self.button_group.setExclusive(False)
            self.a1.setChecked(False)
            self.a2.setChecked(False)
            self.a3.setChecked(False)
            self.button_group.setExclusive(True)
            self.progressBar.setValue(100)
            c = self.final_check(self.shifr)
            if c <= 2:
                out = 'неудовлетворительно'
            elif c <= 5:
                out = 'хорошо'
            else:
                out = 'Отлично'

            d = QtWidgets.QDialog()
            b1 = QtWidgets.QLabel(f"Вы набрали {self.final_check(self.shifr)}, {out}", d)
            d.setFixedSize(200, 100)
            b1.move(10, 50)
            d.setWindowTitle("Dialog")
            d.setWindowModality(QtCore.Qt.ApplicationModal)
            d.exec_()
            self.Disable_all(True)
            self.a1.hide()
            self.a2.hide()
            self.a3.hide()
            self.progressBar.hide()
            self.textBrowser.hide()
            self.pushButton.hide()






    def Disable_all(self, arg=False):
        if arg:
            for i in (self.des_test, self.des_teory, self.Aes_teory, self.Aes_test, self.Aes_zadani, self.des_zadanie):
                i.setDisabled(False)
        else:
            for i in (self.des_test, self.des_teory, self.Aes_teory, self.Aes_test, self.Aes_zadani, self.des_zadanie):
                i.setDisabled(True)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())