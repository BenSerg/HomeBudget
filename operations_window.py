from main_window import MainWindow
from create_widgets_functions import *
from window_functions import *


class OperationsWindow(QWidget):
    def return_to_main_menu(self):
        self.main_menu = MainWindow()
        self.main_menu.show()
        self.close()

    def goto_enter_window(self):
        self.enter_window = OperationsEnterWindow()
        self.enter_window.show()
        self.close()

    def goto_modify_window(self):
        self.modify_window = OperationsModifyWindow()
        self.modify_window.show()
        self.close()

    def goto_delete_window(self):
        self.delete_window = OperationsDeleteWindow()
        self.delete_window.show()
        self.close()

    def __init__(self):
        self.delete_button = None
        self.delete_window = None
        self.modify_window = None
        self.enter_window = None
        self.main_menu = None
        self.enter_button = None
        self.return_button = None
        self.modify_button = None
        self.layout = QVBoxLayout()
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Менеджер операций')
        set_window_geometry(self)
        font = create_font(size=41)
        font.setPointSize(41)
        font.setBold(True)
        font.setWeight(75)

        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_main_menu)

        font.setPointSize(20)

        self.enter_button = create_button(self, 174, 50, 471, 125, font, 'Регистрация операций')
        self.enter_button.clicked.connect(self.goto_enter_window)

        self.modify_button = create_button(self, 180, 220, 471, 125, font, 'Модификация операций')
        self.modify_button.clicked.connect(self.goto_modify_window)

        self.delete_button = create_button(self, 175, 400, 471, 125, font, 'Удаление операций')
        self.delete_button.clicked.connect(self.goto_delete_window)
        self.setLayout(self.layout)


class OperationsEnterWindow(QWidget):
    def return_to_articles_window(self):
        self.operations_window = OperationsWindow()
        self.operations_window.show()
        self.close()

    def __init__(self):
        super().__init__()
        self.return_button = None
        self.ok_button = None
        self.datetime_label = None
        self.credit_label = None
        self.debit_label = None
        self.name_label = None
        self.datetime_input = None
        self.credit_input = None
        self.debit_input = None
        self.name_input = None
        self.operations_window = None
        self.layout = QVBoxLayout()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Регистрация операций')
        set_window_geometry(self)
        font = create_font()
        self.name_input = create_line_edit(self, 400, 100, 311, 31, font)
        self.debit_input = create_line_edit(self, 70, 300, 311, 31, font)
        self.credit_input = create_line_edit(self, 400, 300, 311, 31, font)
        self.datetime_input = create_datetime_edit(self, 70, 100, 221, 31, font)

        font.setBold(True)
        self.name_label = create_label(self, 400, 70, 321, 16, font, 'Наименование квитанции')
        self.debit_label = create_label(self, 70, 270, 311, 31, font, 'Приход в рублях')
        self.credit_label = create_label(self, 400, 270, 311, 31, font, 'Расход в рублях')
        self.datetime_label = create_label(self, 70, 70, 321, 31, font, 'Дата и время')

        self.ok_button = create_ok_button(self, font)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_articles_window)

        self.setLayout(self.layout)


class OperationsModifyWindow(QWidget):
    def return_to_operations_window(self):
        self.operations_window = OperationsWindow()
        self.operations_window.show()
        self.close()

    def __init__(self):
        super().__init__()
        self.return_button = None
        self.ok_button = None
        self.datetime_label = None
        self.article_label = None
        self.credit_label = None
        self.debit_label = None
        self.key_label = None
        self.choice_field = None
        self.article_choice = None
        self.datetime_input = None
        self.date_choice = None
        self.article_input = None
        self.credit_input = None
        self.debit_input = None
        self.operations_window = None
        self.layout = QVBoxLayout()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Модификация операций')
        set_window_geometry(self)
        font = create_font()
        self.debit_input = create_line_edit(self, 440, 90, 311, 31, font)
        self.credit_input = create_line_edit(self, 440, 160, 311, 31, font)
        self.article_input = create_line_edit(self, 440, 230, 311, 31, font)
        self.datetime_input = create_datetime_edit(self, 440, 310, 321, 31, font)

        self.date_choice = create_radio_button(self, 10, 180, 171, 20, font, 'Дата и время')
        self.article_choice = create_radio_button(self, 10, 220, 311, 20, font, 'Наименование квитанции')
        self.choice_field = create_line_edit(self, 10, 260, 311, 31, font)

        font.setBold(True)

        self.key_label = create_label(self, 10, 140, 261, 31, font, 'Ключ модификации')
        self.debit_label = create_label(self, 440, 50, 301, 31, font, 'Приход в рублях')
        self.credit_label = create_label(self, 440, 130, 321, 31, font, 'Расход в рублях')
        self.article_label = create_label(self, 440, 200, 321, 31, font, 'Наименование статьи')
        self.datetime_label = create_label(self, 440, 280, 291, 21, font, 'Новая дата')

        self.ok_button = create_ok_button(self, font)

        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_operations_window)


class OperationsDeleteWindow(QWidget):
    def return_to_operations_window(self):
        self.operations_window = OperationsWindow()
        self.operations_window.show()
        self.close()

    def __init__(self):
        super().__init__()
        self.return_button = None
        self.ok_button = None
        self.key_label = None
        self.choice_field = None
        self.article_choice = None
        self.date_choice = None
        self.operations_window = None
        self.layout = QVBoxLayout()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Удаление операций')
        set_window_geometry(self)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(15)
        self.date_choice = create_radio_button(self, 250, 180, 171, 20, font, 'Дата и время')
        self.article_choice = create_radio_button(self, 250, 220, 311, 20, font, 'Наименование квитанции')
        self.choice_field = create_line_edit(self, 250, 260, 311, 31, font)

        font.setBold(True)
        self.key_label = create_label(self, 250, 140, 261, 31, font, 'Ключ удаления')

        self.ok_button = create_ok_button(self, font)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_operations_window)
        self.setLayout(self.layout)
