from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QStackedWidget, QMainWindow, QVBoxLayout, QPushButton


class MainWindow(QWidget):
    def goto_article_window(self):
        self.article_window = ArticleWindow()
        self.article_window.show()
        self.close()

    def __init__(self):
        self.article_window = None
        self.amount_button = None
        self.journal_button = None
        self.budget_change_button = None
        self.streams_button = None
        self.article_button = None
        self.operations_button = None
        self.layout = QVBoxLayout()
        super().__init__()
        self.setup_ui()

    @staticmethod
    def create_font(family='Serif', size=15):
        font = QtGui.QFont()
        font.setFamily(family)
        font.setPointSize(size)
        return font

    def create_button(self, x, y, width, height, font, object_name, background_color='white'):
        button = QPushButton(object_name, self)
        button.setGeometry(QtCore.QRect(x, y, width, height))
        button.setFont(font)
        button.setStyleSheet(f'background-color: {background_color};')
        button.setObjectName(object_name)
        return button

    def setup_ui(self):
        self.setWindowTitle("MainWindow")

        self.setGeometry(0, 0, 800, 600)
        font = self.create_font()

        self.operations_button = self.create_button(0, 0, 400, 200, font=font, object_name='Менеджер операций')
        self.article_button = self.create_button(400, 0, 400, 200, font=font, object_name='Менеджер квитанций')
        self.streams_button = self.create_button(400, 200, 400, 200, font, 'Динамика потоков по квитанциям',
                                                 background_color='blue')
        self.budget_change_button = self.create_button(0, 200, 400, 200, font, 'Динамика изменения бюджета',
                                                       background_color='blue')
        self.journal_button = self.create_button(0, 400, 400, 200, font, 'Журнал анализа', background_color='red')
        self.amount_button = self.create_button(400, 400, 400, 200, font, 'Отображение прибыли', background_color='red')
        self.article_button.clicked.connect(self.goto_article_window)
        self.setLayout(self.layout)


class ArticleWindow(QWidget):
    def return_to_main_menu(self):
        self.main_menu = MainWindow()
        self.main_menu.show()
        self.close()

    def __init__(self):
        self.main_menu = None
        self.enter_button = None
        self.return_button = None
        self.modify_button = None
        self.layout = QVBoxLayout()
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('Менеджер квитанций')
        self.setGeometry(0, 0, 800, 600)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(41)
        font.setBold(True)
        font.setWeight(75)

        self.return_button = QPushButton('←', self)
        self.return_button.setGeometry(QtCore.QRect(0, 0, 91, 51))
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        self.return_button.clicked.connect(self.return_to_main_menu)

        self.enter_button = QtWidgets.QPushButton('Регистрация квитанция', self)
        self.enter_button.setGeometry(QtCore.QRect(174, 50, 471, 125))
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.enter_button.setFont(font)
        self.enter_button.setObjectName("enter_button")

        self.modify_button = QtWidgets.QPushButton('Модификация квитанций', self)
        self.modify_button.setGeometry(QtCore.QRect(180, 220, 471, 125))
        self.modify_button.setFont(font)

        self.delete_button = QtWidgets.QPushButton('Удаление квитанций', self)
        self.delete_button.setGeometry(QtCore.QRect(175, 400, 471, 125))
        self.delete_button.setFont(font)

        self.setLayout(self.layout)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
