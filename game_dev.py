import locale
import sys

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QLineEdit, QPushButton, QTextEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QHBoxLayout, QVBoxLayout, QWidget, QGridLayout, QToolBar, QStatusBar,
    QDateEdit, QMessageBox
)
from PyQt6.QtCore import Qt, QDateTime, QDate
from random import *
from datetime import *

from dateutil.relativedelta import relativedelta

locale.setlocale(locale.LC_ALL, 'ru')


class AnotherWindow(QWidget):
    def __init__(self, root):
        super().__init__()
        self.main = root

        self.setWindowTitle("Изменение информации:")
        layout_main = QVBoxLayout()

        layout1 = QHBoxLayout()
        self.label1 = QLineEdit(placeholderText='Первое имя', clearButtonEnabled=True)
        self.label2 = QLineEdit(placeholderText='Второе имя', clearButtonEnabled=True)
        layout1.addWidget(self.label1)
        layout1.addWidget(self.label2)

        layout2 = QHBoxLayout()
        self.label_text = QLabel('Дата рождения:')
        self.label_text.setFont(get_font(8))
        self.label_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout2.addWidget(self.label_text)

        layout3 = QHBoxLayout()
        self.label3 = QDateEdit()
        self.label4 = QDateEdit()
        layout3.addWidget(self.label3)
        layout3.addWidget(self.label4)

        layout4 = QHBoxLayout()
        button = QPushButton('Подтвердить')
        button_cancel = QPushButton('Отменить')
        layout4.addWidget(button)
        layout4.addWidget(button_cancel)

        layout_main.addLayout(layout1)
        layout_main.addLayout(layout2)
        layout_main.addLayout(layout3)
        layout_main.addLayout(layout4)
        self.setLayout(layout_main)
        button.clicked.connect(self.swap_info)
        button_cancel.clicked.connect(self.cancel)

    def swap_info(self):
        self.main.widget_name_per1.setText(self.label1.text().title())
        self.main.widget_name_per2.setText(self.label2.text().title())
        self.main.per1_date_birt = datetime.strptime(self.label3.text(), '%d.%m.%Y')
        self.main.per2_date_birt = datetime.strptime(self.label4.text(), '%d.%m.%Y')
        self.main.label_point_per1.setText('0')
        self.main.label_point_per2.setText('0')
        self.main.label_result_date1.setText(None)
        self.main.label_result_date2.setText(None)
        self.main.widget_DateDeath_per1.setText(None)
        self.main.widget_DateDeath_per2.setText(None)
        self.close()

    def cancel(self):
        self.close()


def get_font(size=10):
    w1 = QLabel()
    font = w1.font()
    font.setPointSize(size)
    return font


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.lst_years_old1 = []
        self.lst_years_old2 = []
        self.w = None
        self.per1_date_birt = datetime(day=6, month=7, year=2000)
        self.per1_date_death = None
        self.per2_date_birt = datetime(day=18, month=1, year=2000)
        self.per2_date_death = None
        self.text = ''
        self.setWindowTitle("Frolo dev")
        self.setWindowIcon(QIcon('hope.ico'))
        self.setStatusBar(QStatusBar(self))
        # self.resize(700, 100)
        main_layout = QVBoxLayout()
        layout0 = QVBoxLayout()
        layout1 = QGridLayout()
        main_layout.addLayout(layout0)
        main_layout.addLayout(layout1)

        widget = QLabel("В 2020 году Илон Маск говорил,\nчто у него есть амбиции построить тысячу космических "
                        "кораблей за десять лет,\nчтобы к 2050 году переселить на планету миллион "
                        "человек.\n\nПроверим, кто сможет попасть на корабль!")
        widget.setFont(get_font(16))
        widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.widget_name_per1 = QLabel("Дима")
        self.widget_name_per1.setFont(get_font(16))
        self.widget_name_per1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.widget_name_per2 = QLabel("Коля")
        self.widget_name_per2.setFont(get_font(16))
        self.widget_name_per2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button = QPushButton("Результат!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        button_point_null = QAction("Обнулить", self)
        button_point_null.setStatusTip("Обнуляет счётчик очков")
        button_point_null.triggered.connect(self.refresh_counter)

        button_change_info = QAction('Сменить данные', self)
        button_change_info.setStatusTip('Изменение имён и дат рождения')
        button_change_info.triggered.connect(self.show_new_window)

        button_action_exit = QAction("Выход", self)
        button_action_exit.setStatusTip("Выйти из приложения")
        button_action_exit.triggered.connect(self.close)

        self.label_point_per1 = QLabel()
        self.label_point_per1.setFont(get_font(20))
        self.label_point_per1.setText('0')
        self.label_point_per1.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.label_point_per2 = QLabel()
        self.label_point_per2.setFont(get_font(20))
        self.label_point_per2.setText('0')
        self.label_point_per2.setAlignment(Qt.AlignmentFlag.AlignLeft)

        label_vs = QLabel()
        label_vs.setFont(get_font(20))
        label_vs.setText(':')
        label_vs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.widget_DateDeath_per1 = QLabel(self.per1_date_death)
        self.widget_DateDeath_per1.setFont(get_font(8))
        self.widget_DateDeath_per1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_DateDeath_per2 = QLabel(self.per2_date_death)
        self.widget_DateDeath_per2.setFont(get_font(8))
        self.widget_DateDeath_per2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_result_date1 = QLabel()
        self.label_result_date1.setFont(get_font(13))
        self.label_result_date1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_result_date2 = QLabel()
        self.label_result_date2.setFont(get_font(13))
        self.label_result_date2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_years_old1 = QLabel()
        self.label_years_old1.setFont(get_font(13))
        self.label_years_old1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_years_old2 = QLabel()
        self.label_years_old2.setFont(get_font(13))
        self.label_years_old2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout0.addWidget(widget)
        layout0.addWidget(button)

        layout1.addWidget(self.widget_name_per1, 0, 0)
        layout1.addWidget(self.widget_name_per2, 0, 4)
        layout1.addWidget(self.label_point_per1, 0, 1)
        layout1.addWidget(label_vs, 0, 2)
        layout1.addWidget(self.label_point_per2, 0, 3)

        layout1.addWidget(self.label_years_old1, 1, 0)
        layout1.addWidget(self.label_years_old2, 1, 4)

        layout1.addWidget(self.widget_DateDeath_per1, 2, 0)
        layout1.addWidget(self.widget_DateDeath_per2, 2, 4)

        layout1.addWidget(self.label_result_date1, 3, 0)
        layout1.addWidget(self.label_result_date2, 3, 4)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        menu = self.menuBar()

        file_menu = menu.addMenu("Опции")
        file_menu.addAction(button_point_null)
        file_menu.addAction(button_change_info)
        file_menu.addAction(button_action_exit)

    def refresh_counter(self):
        self.label_point_per1.setText('0')
        self.label_point_per2.setText('0')
        self.lst_years_old1 = []
        self.lst_years_old2 = []

    def the_button_was_clicked(self):
        def swap_time(lst, one, two, date_birth, label_years):
            year = datetime(year=randint(2024, 2100), month=randint(1, 12), day=randint(1, 28))
            str_time = datetime.strftime(year, '%a, %d %B %Y Год')
            self.text = str_time
            one.setText(self.text)
            res = (year - datetime.now()).days
            self.text = f'{res} дней осталось'
            two.setText(self.text)
            y = relativedelta(year, date_birth).years
            lst.append(y)
            self.text = f'{text_years_format(y)}'
            label_years.setText(self.text)
            return res

        def round_counter(one, two):
            if one > two:
                c = str(int(self.label_point_per1.text()) + 1)
                self.label_point_per1.setText(c)
            elif one < two:
                c = str(int(self.label_point_per2.text()) + 1)
                self.label_point_per2.setText(c)
            else:
                c = str(int(self.label_point_per1.text()) + 1)
                self.label_point_per1.setText(c)
                c = str(int(self.label_point_per2.text()) + 1)
                self.label_point_per2.setText(c)
            if self.label_point_per1.text() == '10':
                res = int(self.label_point_per1.text()) - int(self.label_point_per2.text())
                self.final(self.widget_name_per1.text(), str(res), self.per1_date_birt, self.lst_years_old1)
            elif self.label_point_per2.text() == '10':
                res = int(self.label_point_per2.text()) - int(self.label_point_per1.text())
                self.final(self.widget_name_per2.text(), str(res), self.per2_date_birt, self.lst_years_old2)

        res_dima = swap_time(self.lst_years_old1, self.label_result_date1, self.widget_DateDeath_per1,
                             self.per1_date_birt, self.label_years_old1)
        res_kolya = swap_time(self.lst_years_old2, self.label_result_date2, self.widget_DateDeath_per2,
                              self.per2_date_birt, self.label_years_old2)
        round_counter(res_dima, res_kolya)

    def show_new_window(self):
        if self.w is None:
            self.w = AnotherWindow(self)
        self.w.show()

    def final(self, name, count, dt,  lst):
        def text_count_format(c):
            if c == '1':
                text_count = 'очко'
            elif c in '234':
                text_count = 'очка'
            else:
                text_count = 'очков'
            return text_count

        def mars(nm, dat):
            d = round(sum(lst) / len(lst))
            dt_to_mars = dat + timedelta(days=d * 365)
            if dt_to_mars.year == 2050:
                return f'Вероятно, {nm} погибните прямо во время запуска ракеты...'
            elif dt_to_mars.year > 2050:
                return f'Ура! {nm} будете жить на Марсе ~{text_years_format(dt_to_mars.year - 2050)}!'
            else:
                return f'{nm}, вероятно, не успеет побывать на Марсе...'

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Финал")
        dlg.setText(f"Победитель: {name}!\n{mars(name, dt)}\n\nОтрыв в {count} {text_count_format(count)}.\nОжидаемая продолжительность "
                    f"жизни: {text_years_format(round(sum(lst) / len(lst)))}\nМинимально: {text_years_format(min(lst))}, максимально {text_years_format(max(lst))}")
        dlg.exec()
        self.refresh_counter()


def text_years_format(i):
    if i in [11, 12, 13, 14]:
        res = str(i) + ' лет'
    elif i % 10 == 1:
        res = str(i) + ' год'
    elif 2 <= i % 10 <= 4:
        res = str(i) + ' года'
    else:
        res = str(i) + ' лет'
    return res


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
