from main_window import MainWindow
from create_widgets_functions import *
from window_functions import *
from main_window import MainWindow


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
        self.table_balance = BalanceView()
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

    def __init__(self):
        super().__init__()
        self.return_button = None
        self.ok_button = None
        self.key_label = None
        self.input_field = None
        self.main_menu = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Формирование баланса')
        set_window_geometry(self)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(15)
        self.input_field = create_line_edit(self, 50, 200, 700, 60, font)
        font.setBold(True)
        self.key_label = create_label(self, 50, 100, 800, 50, font, 'Введите через запятую наименования квитанций')
        self.ok_button = create_ok_button(self, font)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_journal_window)


class BalanceDelete(QWidget):
    def return_to_journal_window(self):
        self.main_menu = JournalWindow()
        self.main_menu.show()
        self.close()

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
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_journal_window)


class BalanceView(QWidget):
    def return_to_journal_window(self):
        self.main_menu = JournalWindow()
        self.main_menu.show()
        self.close()

    def __init__(self):
        self.main_menu = None
        font = create_font()
        super().__init__()

        self.setWindowTitle('Table Data Example')
        set_window_geometry(self)

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)

        data = [
            ['John', 'Doe', 30],
            ['Jane', 'Smith', 25],
            ['Tom', 'Brown', 40]
        ]

        for i in range(len(data)):
            for j in range(len(data[i])):
                item = QtWidgets.QTableWidgetItem(str(data[i][j]))
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.setGeometry(QtCore.QRect(150, 150, 150, 150))
        font.setBold(True)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_journal_window)
