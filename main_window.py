from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QStackedWidget, QMainWindow, QVBoxLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self):
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

        self.operations_button = self.create_button(0, 0, 400, 200, font, 'Менеджер операций')
        self.article_button = self.create_button(400, 0, 400, 200, font, 'Менеджер квитанций')
        self.streams_button = self.create_button(400, 200, 400, 200, font, 'Динамика потоков по квитанциям',
                                                 background_color='blue')
        self.budget_change_button = self.create_button(0, 200, 400, 200, font, 'Динамика изменения бюджета',
                                                       background_color='blue')
        self.journal_button = self.create_button(0, 400, 400, 200, font, 'Журнал анализа', background_color='red')
        self.amount_button = self.create_button(400, 400, 400, 200, font, 'Отображение прибыли', background_color='red')

        self.setLayout(self.layout)


class ArticleWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(QtWidgets.QMainWindow())

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(0, 0, 91, 51))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(41)
        font.setBold(True)
        font.setWeight(75)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        self.return_button.clicked.connect(self.on_click)
        self.enter_button = QtWidgets.QPushButton(self.centralwidget)
        self.enter_button.setGeometry(QtCore.QRect(174, 50, 471, 125))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.enter_button.setFont(font)
        self.enter_button.setObjectName("enter_button")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 220, 471, 125))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(175, 400, 471, 125))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Менеджер статей"))
        self.return_button.setText(_translate("mainWindow", "←"))
        self.enter_button.setText(_translate("mainWindow", "Ввод статей"))
        self.pushButton_3.setText(_translate("mainWindow", "Модификация статей"))
        self.pushButton_4.setText(_translate("mainWindow", "Удаление статей"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
