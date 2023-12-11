from main_window import MainWindow
from create_widgets_functions import *
from window_functions import *
from graph_window import *


class BudgetChange(QWidget):
    def return_to_main_menu(self):
        self.main_menu = MainWindow()
        self.main_menu.show()
        self.close()

    def __init__(self):
        super().__init__()
        self.return_button = None
        self.ok_button = None
        self.key_label = None
        self.to_date_label = None
        self.from_date_label = None
        self.to_date = None
        self.from_date = None
        self.input_field = None
        self.graph_window = None
        self.main_menu = None
        self.setup_ui()

    def create_graph(self):
        self.graph_window = GraphWindow(self)
        self.graph_window.show()
        self.close()

    def setup_ui(self):
        self.setWindowTitle('Динамика изменения бюджета')
        set_window_geometry(self)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(15)
        self.input_field = create_line_edit(self, 50, 200, 700, 60, font)
        self.from_date = create_datetime_edit(self, 125, 40, 210, 40, font)
        self.to_date = create_datetime_edit(self, 400, 40, 210, 40, font)
        font.setBold(True)
        self.from_date_label = create_label(self, 125, 10, 260, 31, font, 'Начало периода')
        self.to_date_label = create_label(self, 400, 10, 260, 31, font, 'Конец периода')
        font.setBold(True)
        self.key_label = create_label(self, 50, 125, 800, 50, font, 'Введите через запятую наименования квитанций')
        self.ok_button = create_ok_button(self, font)
        self.ok_button.clicked.connect(self.create_graph)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_main_menu)
