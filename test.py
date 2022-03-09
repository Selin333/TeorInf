import numexpr as ne
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from PyQt5.QtWinExtras import QtWin
import re

myappid = 'CalcTeorInf'
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
from calc import Ui_MainWindow  # импорт ui
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        primer = self.ui.lineEdit.text()
        pole = (self.ui.lineEdit_2.text())

        # Ошибки
        def Error(info):
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText("Ошибка")
            error.setInformativeText(info)
            error.setWindowTitle("Ой-йой")
            error.exec_()

        def evclid(num1, num2):
            if num1 == 0:
                return (num2, 0, 1)
            else:
                div, x, y = evclid(num2 % num1, num1)
            return (div, y - (num2 // num1) * x, x)

        # Проверка простое ли поле
        def Prime(num):
            count = 2
            while num % count != 0:
                count += 1
            return count == num
        try:

            if not primer or not pole:
                Error("Заполните все поля")
            else:
                pole = int(pole)

                if '^' in primer or '**' in primer:
                    Error("Замените знаки ^ и ** на умножение")

                else:
                    if primer.count("(") != primer.count(")"):
                        Error("Ошибка в расстановке скобок!")

                    else:

                        if Prime(pole) == True:
                            for i in range(len(primer)):
                                if '/' in primer:
                                    zamena = primer.find('/')

                                    primer = re.split("([\*\-\+\/])", primer)
                                    print(primer)
                                    primer[zamena] = '*'
                                    primer[zamena + 1] = str(evclid(int(primer[zamena + 1]), pole)[1]%pole)
                                    primer = ''.join(primer)
                                else:
                                    break

                            primer = int(ne.evaluate(''.join(primer)))
                            otvet = primer % pole

                            self.ui.lineEdit_3.setText(str(otvet))

                        else:
                            Error("Поле не простое")
        except:
            Error("Ошибка при заполнении")

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())



