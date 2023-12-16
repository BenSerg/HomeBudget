import os
import shutil

import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget

from application_functions.create_widgets_functions import *
from application_functions.window_functions import *


class GraphWindow(QWidget):
    def return_to_parent_window(self):
        self.parent.show()
        self.close()

    def create_report(self):
        file_name = self.parent.__class__.__name__
        shutil.copy(self.path, f'reports/{file_name}.png')
        msgbox = create_msg_box(title='Уведомление', message='Сохранено')
        msgbox.exec_()

    def __init__(self, parent: QWidget, data_y, data_x):
        super().__init__()
        self.report_button = None
        self.path = None
        self.return_button = None
        self.data_x = data_x
        self.data_y = data_y
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('График')
        set_window_geometry(self)
        from application_windows.budget_change_window import BudgetChange
        from application_windows.amount_window import AmountWindow
        from application_windows.financial_threads_window import FinancialThreads
        if self.parent.__class__ == BudgetChange:
            self.setWindowTitle('Приход и расход бюджета')
            plt.figure()
            plt.plot(self.data_y, [i[0] for i in self.data_x], color='red', label='Расход', marker='.', markersize=20)
            plt.plot(self.data_y, [i[1] for i in self.data_x], color='green', label='Приход', marker='.', markersize=20)
            plt.xlabel('Дата проведения операции')
            plt.ylabel('Сумма величины')
        elif self.parent.__class__ == AmountWindow:
            self.setWindowTitle('Прибыль бюджета')
            plt.figure()
            plt.plot(self.data_y, self.data_x, color='blue', label='Прибыль', marker='.', markersize=20)
            plt.xlabel('Время')
            plt.ylabel('Прибыль')
        elif self.parent.__class__ == FinancialThreads:
            self.setWindowTitle('Соотношение финансовых потоков')
            plt.figure()
            plt.bar(self.data_x, self.data_y, color='yellow', edgecolor='black', alpha=0.5,
                    label='Соотношение потоков по статьям')
            plt.xlabel('Наименование квитанции')
            plt.ylabel('Число соотношения')
            plt.grid(axis='x')
        else:
            plt.figure()
            plt.plot(self.data_y, self.data_x, color='purple', label='Соотношение Приход/Расход', marker='.',
                     markersize=20)
        plt.xticks(rotation=25)
        plt.grid()
        plt.legend()
        self.path = 'tmp_resources/graph.png'
        plt.savefig(self.path)
        plt_label = QLabel(self)
        plot_pixmap = QtGui.QPixmap(self.path)
        plt_label.setPixmap(plot_pixmap)
        font = create_font(size=41)
        font.setBold(True)
        font.setWeight(75)

        self.report_button = create_button(self, 500, 500, 150, 100, create_font(), 'Сохранить')
        self.report_button.clicked.connect(self.create_report)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_parent_window)
