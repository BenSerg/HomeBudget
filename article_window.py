from main_window import MainWindow
from create_widgets_functions import *
from window_functions import *


class ArticleWindow(QWidget):
    def return_to_main_menu(self):
        self.main_menu = MainWindow()
        self.main_menu.show()
        self.close()

    def goto_enter_window(self):
        self.enter_window = ArticlesEnterWindow()
        self.enter_window.show()
        self.close()

    def goto_modify_window(self):
        self.modify_window = ArticlesModifyWindow()
        self.modify_window.show()
        self.close()

    def goto_delete_window(self):
        self.delete_window = ArticlesDeleteWindow()
        self.delete_window.show()
        self.close()

    def __init__(self):
        self.delete_window = None
        self.modify_window = None
        self.enter_window = None
        self.delete_button = None
        self.main_menu = None
        self.enter_button = None
        self.return_button = None
        self.modify_button = None
        self.layout = QVBoxLayout()
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Менеджер квитанций')
        set_window_geometry(self)
        font = create_font(size=41)
        font.setWeight(75)

        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_main_menu)

        font.setPointSize(20)

        self.enter_button = create_button(self, 174, 50, 471, 125, font, 'Регистрация квитанций')
        self.enter_button.clicked.connect(self.goto_enter_window)

        self.modify_button = create_button(self, 180, 220, 471, 125, font, 'Модификация квитанций')
        self.modify_button.clicked.connect(self.goto_modify_window)

        self.delete_button = create_button(self, 175, 400, 461, 125, font, 'Удаление квитанций')
        self.delete_button.clicked.connect(self.goto_delete_window)

        self.setLayout(self.layout)


class ArticlesEnterWindow(QWidget):
    def return_to_articles_window(self):
        self.article_window = ArticleWindow()
        self.article_window.show()
        self.close()

    def __init__(self):
        super().__init__()
        self.return_button = None
        self.ok_button = None
        self.name_label = None
        self.name_input = None
        self.article_window = None
        self.layout = QVBoxLayout()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Регистрация квитанций')
        set_window_geometry(self)
        font = create_font()
        self.name_input = create_line_edit(self, 245, 220, 311, 31, font)
        font.setBold(True)
        self.name_label = create_label(self, 245, 140, 350, 31, font, 'Наименование квитанции')

        self.ok_button = create_ok_button(self, font)
        font.setPointSize(41)
        font.setBold(True)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_articles_window)

        self.setLayout(self.layout)


class ArticlesModifyWindow(QWidget):
    def return_to_articles_window(self):
        self.article_window = ArticleWindow()
        self.article_window.show()
        self.close()

    def __init__(self):
        super().__init__()
        self.return_button = None
        self.ok_button = None
        self.name_label = None
        self.old_name_label = None
        self.old_name_input = None
        self.name_input = None
        self.article_window = None
        self.layout = QVBoxLayout()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Модификация квитанций')
        set_window_geometry(self)
        font = create_font()
        self.name_input = create_line_edit(self, 400, 100, 311, 31, font)

        self.old_name_input = create_line_edit(self, 25, 100, 311, 31, font)

        font.setBold(True)
        self.old_name_label = create_label(self, 25, 70, 311, 31, font, 'Старое наименование')

        self.name_label = create_label(self, 400, 70, 321, 16, font, 'Новое наименование')

        self.ok_button = create_ok_button(self, font)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_articles_window)

        self.setLayout(self.layout)


class ArticlesDeleteWindow(QWidget):
    def return_to_articles_window(self):
        self.article_window = ArticleWindow()
        self.article_window.show()
        self.close()

    def __init__(self):
        super().__init__()
        self.return_button = None
        self.ok_button = None
        self.name_label = None
        self.name_input = None
        self.article_window = None
        self.layout = QVBoxLayout()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Регистрация квитанций')
        set_window_geometry(self)
        font = create_font()
        self.name_input = create_line_edit(self, 245, 220, 311, 31, font)
        font.setBold(True)
        self.name_label = create_label(self, 245, 140, 350, 31, font, 'Наименование квитанции')

        self.ok_button = create_ok_button(self, font)
        font.setPointSize(41)
        font.setBold(True)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_articles_window)
        self.setLayout(self.layout)
