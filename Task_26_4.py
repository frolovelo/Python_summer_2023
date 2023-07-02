'''PyQt6 меню Описание, инструкция, помощь'''

import sys

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QLineEdit, QPushButton, QTextEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QHBoxLayout, QVBoxLayout, QWidget
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        action = QAction('Программа, которая не может навредить', self)
        action.setStatusTip('Точно не может!')
        action1 = QAction('Просто нажми на кнопку', self)
        action1.setStatusTip('Тык')
        action2 = QAction('Помощи не будет', self)
        action2.setStatusTip('Увы...')

        action3 = QAction('Скрыть/показать Меню', self, checkable=True)
        action3.setChecked(True)
        action3.triggered.connect(self.toggleMenu)

        self.statusBar()

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('Описание')
        fileMenu.addAction(action)
        fileMenu1 = menubar.addMenu('Инструкция')
        fileMenu1.addAction(action1)
        fileMenu2 = menubar.addMenu('Помощь')
        fileMenu2.addAction(action2)

        toolbar = self.addToolBar('Главный туллбар')
        toolbar.addAction(action3)

        self.setGeometry(200, 600, 700, 300)
        self.setWindowTitle('Frolo menu')
        self.show()

    def toggleMenu(self, s):
        if s:
            self.menuBar().show()
        else:
            self.menuBar().hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())
