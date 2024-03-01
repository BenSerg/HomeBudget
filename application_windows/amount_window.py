from PyQt5.QtWidgets import QWidget
from config.connection import conn
from application_windows.main_window import MainWindow
from application_functions.create_widgets_functions import *
from application_functions.window_functions import *
from application_windows.graph_window import GraphWindow
from application_functions.logger import logger


class AmountWindow(QWidget):
    def return_to_main_menu(self):
        if hasattr(self, 'main_menu'):
            self.main_menu.show()
            self.close()
        else:
            self.main_menu = MainWindow()
            self.main_menu.show()
            self.close()

    def create_graph(self):
        cur = conn.cursor()
        query = (f"select accumulated_sum, create_date from (select operations.create_date, sum(sum(operations.debit)"
                 f" - sum(operations.credit)) over (order by operations.create_date) as accumulated_sum from operations"
                 f" where operations.create_date >= '{self.from_date.text()}' and operations.create_date <= '{self.to_date.text()}' "
                 f"group by operations.create_date) as subquery;")
        cur.execute(query)
        logger.debug(f'Выполнен запрос: {query}')
        data = cur.fetchall()
        dct = {i[1]: i[0] for i in data}
        self.graph_window = GraphWindow(self, list(dct.keys()), list(dct.values()))
        self.graph_window.show()
        self.close()

    def __init__(self):
        super().__init__()
        self.ok_button = None
        self.graph_window = None
        self.return_button = None
        self.to_date_label = None
        self.from_date_label = None
        self.to_date = None
        self.from_date = None
        self.main_menu = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Прибыль бюджета')
        font = create_font()
        set_window_geometry(self)
        self.from_date = create_datetime_edit(self, 125, 40, 210, 40, font)
        self.to_date = create_datetime_edit(self, 400, 40, 210, 40, font)
        font.setBold(True)
        self.from_date_label = create_label(self, 125, 10, 260, 31, font, 'Начало периода')
        self.to_date_label = create_label(self, 400, 10, 260, 31, font, 'Конец периода')
        self.ok_button = create_ok_button(self, font)
        self.ok_button.clicked.connect(self.create_graph)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_main_menu)
