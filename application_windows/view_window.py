from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from application_functions.create_widgets_functions import *
from application_functions.logger import logger
from config.connection import conn
from application_functions.window_functions import *


class ViewWindow(QWidget):
    def return_to_journal_window(self):
        self.parent_window.show()
        self.close()

    def setup_table(self):
        self.table_widget = QtWidgets.QTableWidget(self)
        cur = conn.cursor()
        query = f"select * from {self.window_type}"
        cur.execute(query)
        logger.debug(f"Выполнен запрос: {query}")
        data = cur.fetchall()
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(data[0]))
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                self.table_widget.setItem(row_num, col_num, item)
        conn.commit()
        self.table_widget.setHorizontalHeaderLabels(self.names)
        self.table_widget.resizeColumnToContents(1)
        self.table_widget.setGeometry(0, 50, 750, 500)

    def __init__(self, parent_window):
        self.names = None
        self.return_button = None
        self.table_widget = None
        self.parent_window = parent_window
        self.window_type = 'balance'
        super().__init__()

        self.setup_ui()
        set_window_geometry(self)

    def setup_ui(self):
        from application_windows.article_window import ArticleWindow
        from application_windows.operations_window import OperationsWindow
        if self.parent_window.__class__ == ArticleWindow:
            self.setWindowTitle('Просмотр квитанций')
            self.window_type = 'articles'
            self.names = ['Идентификатор', 'Наименование квитанции']

        elif self.parent_window.__class__ == OperationsWindow:
            self.setWindowTitle('Просмотр операций')
            self.window_type = 'operations'
            self.names = ['Идентификатор', 'Идентификатор квитанции', 'Приход', 'Расход', 'Дата проведения',
                          'Идентификатор баланса']
        else:
            self.setWindowTitle('Просмотр балансов')
            self.names = ['Идентификатор', 'Дата формирования', 'Приход', 'Расход', 'Прибыль']
            self.window_type = 'balance'
        font = create_font()
        font.setBold(True)
        font.setPointSize(41)
        font.setWeight(75)
        self.setup_table()
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_journal_window)
