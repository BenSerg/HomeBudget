from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from application_functions.logger import logger
from application_windows.view_window import ViewWindow
from application_functions.create_widgets_functions import *
from config.connection import conn
from application_windows.main_window import MainWindow
from application_functions.window_functions import *


class JournalWindow(QWidget):
    def return_to_main_menu(self):
        self.main_menu = MainWindow()
        self.main_menu.show()
        self.close()

    def goto_balance_create_window(self):
        self.balance_window = BalanceCreate()
        self.balance_window.show()
        self.close()

    def goto_balance_delete_window(self):
        self.delete_window = BalanceDelete()
        self.delete_window.show()
        self.close()

    def goto_balance_view_window(self):
        self.table_balance = ViewWindow(self)
        self.table_balance.show()
        self.close()

    def __init__(self):
        self.table_balance = None
        self.balance_window = None
        self.delete_window = None
        self.delete_button = None
        self.main_menu = None
        self.enter_button = None
        self.return_button = None
        self.view_button = None
        self.layout = QVBoxLayout()
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Журнал анализа')
        set_window_geometry(self)
        font = create_font(size=20)
        font.setBold(True)
        font.setWeight(75)
        self.enter_button = create_button(self, 174, 50, 471, 125, font, 'Формирование балансов')
        self.enter_button.clicked.connect(self.goto_balance_create_window)

        self.view_button = create_button(self, 180, 220, 471, 125, font, 'Просмотр балансов')
        self.view_button.clicked.connect(self.goto_balance_view_window)

        self.delete_button = create_button(self, 175, 400, 471, 125, font, 'Расформирование балансов')
        self.delete_button.clicked.connect(self.goto_balance_delete_window)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_main_menu)

        self.setLayout(self.layout)


class BalanceCreate(QWidget):
    def return_to_journal_window(self):
        self.main_menu = JournalWindow()
        self.main_menu.show()
        self.close()

    def create_balance(self):
        cur = conn.cursor()
        cur.execute(f"insert into balance(create_date) values('{self.datetime_input.text()}')")
        query = (
            f"select o.id from operations o join balance b on extract(month from o.create_date) = extract(month FROM b.create_date) "
            f"where extract(month from o.create_date) = extract(month from b.create_date) and balance_id is null"
        )
        cur.execute(query)
        logger.debug(f"Выполнен запрос {query}")

        id_operations = tuple(i[0] for i in cur.fetchall())
        cur.execute(f"select id from balance order by id desc limit 1")
        balance_id = cur.fetchone()[0]
        query = f"update operations set balance_id = {balance_id} where id in {id_operations}"
        cur.execute(query)
        logger.debug(f"Выполнен запрос {query}")
        query = (f"update balance set debit = (select sum(debit) from operations where id in {id_operations}), "
                 f"credit = (select sum(credit) from operations where id in {id_operations}) where id = {balance_id}")
        cur.execute(query)
        logger.debug(f"Выполнен запрос {query}")

        query = f"update balance set amount = debit - credit where id = {balance_id}"
        cur.execute(query)
        logger.debug(f"Выполнен запрос {query}")

        msgbox = create_msg_box(title='Уведомления', message='Баланс успешно сформирован')
        msgbox.exec_()
        conn.commit()

    def __init__(self):
        super().__init__()
        self.datetime_input = None
        self.datetime_label = None
        self.return_button = None
        self.ok_button = None
        self.month_number = None
        self.month_input = None
        self.main_menu = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Формирование баланса')
        set_window_geometry(self)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(15)
        self.datetime_input = create_datetime_edit(self, 250, 150, 300, 50, font)
        font.setBold(True)
        self.datetime_label = create_label(self, 225, 100, 800, 50, font, 'Введите дату формирования')

        self.ok_button = create_ok_button(self, font)
        self.ok_button.clicked.connect(self.create_balance)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_journal_window)


class BalanceDelete(QWidget):
    def return_to_journal_window(self):
        self.main_menu = JournalWindow()
        self.main_menu.show()
        self.close()

    def delete_balance(self):
        cur = conn.cursor()
        cur.execute(f"select * from balance where id = 10")
        if cur.rowcount == 0:
            msgbox = create_msg_box(title='Ошибка',
                                    message=f'Баланс с идентификатором {self.input_field.text()} не существует')
        else:
            cur.execute(f"delete from balance where id = {self.input_field.text()}")
            msgbox = create_msg_box(title='Уведомление',
                                    message=f'Баланс с идентификатором {self.input_field.text()} удален')
        conn.commit()
        msgbox.exec_()

    def __init__(self):
        super().__init__()
        self.ok_button = None
        self.return_button = None
        self.key_label = None
        self.input_field = None
        self.main_menu = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Расформирование баланса')
        set_window_geometry(self)
        font = create_font()
        self.input_field = create_line_edit(self, 300, 200, 150, 30, font)
        font.setBold(True)
        self.key_label = create_label(self, 200, 100, 800, 50, font, 'Введите идентификатор баланса')
        self.ok_button = create_ok_button(self, font)
        self.ok_button.clicked.connect(self.delete_balance)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_journal_window)


class BalanceView(QWidget):
    def return_to_journal_window(self):
        self.main_menu = JournalWindow()
        self.main_menu.show()
        self.close()

    def setup_table(self):
        self.table_widget = QtWidgets.QTableWidget(self)
        cur = conn.cursor()
        cur.execute(f"select * from balance")
        data = cur.fetchall()
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(data[0]))
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                self.table_widget.setItem(row_num, col_num, item)
        conn.commit()
        self.table_widget.setHorizontalHeaderLabels(
            ['Идентификатор', 'Дата формирования', 'Приход', 'Расход', 'Прибыль'])
        self.table_widget.resizeColumnToContents(1)
        self.table_widget.setGeometry(50, 50, 700, 500)

    def __init__(self):
        self.return_button = None
        self.table_widget = None
        self.main_menu = None

        super().__init__()

        self.setup_ui()
        set_window_geometry(self)

    def setup_ui(self):
        self.setWindowTitle('Просмотр балансов')
        font = create_font()
        font.setBold(True)
        font.setPointSize(41)
        font.setWeight(75)
        self.setup_table()
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_journal_window)
