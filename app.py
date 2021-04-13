#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from os import path
from sys import argv, exit

from PySide6.QtCore import QFile, Slot
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtUiTools import QUiLoader

from ui.mainwindow import Ui_Calculator

from modules.calculate import calculate, format_number


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.expression = ""
        buttons = {
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "comma": ".",
            "add": "+",
            "substract": "-",
            "multiply": "×",
            "divide": "÷",
            "power": "^",
            "openingParenthesis": "(",
            "closingParenthesis": ")"
        }
        for btn in buttons.items():
            def fun(wtf=False, writes=btn[1]):
                self.expression += writes
                self.update()
            self.__setattr__(btn[0], fun)
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        
        with open("qss/light.qss", "r") as f:
            self.setStyleSheet(f.read())

    def correct(self):
        self.expression = self.expression[:-1]
        self.update()

    def reset(self):
        self.expression = ""
        self.update()

    def update(self):
        self.findChild(QLabel, "label_calculation").setText(self.expression)
        try:
            self.findChild(QLabel, "label_calculation").setStyleSheet(
                "color: grey")
            result = format_number(str(round(calculate(self.expression), 8)))
        except:
            self.findChild(QLabel, "label_calculation").setStyleSheet(
                "color: red")
            result = ""
        self.findChild(QLabel, "label_result").setText(result)


if __name__ == "__main__":
    app = QApplication(argv)
    widget = MainWindow()
    widget.show()
    exit(app.exec_())
