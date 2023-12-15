from PyQt5.QtWidgets import QWidget, QVBoxLayout

from application_functions.create_widgets_functions import *
from application_functions.window_functions import *
from functools import lru_cache


@lru_cache
class MainWindow(QWidget):
    def goto_article_window(self):
        from application_windows.article_window import ArticleWindow
        self.article_window = ArticleWindow()
        self.article_window.show()
        self.close()

    def goto_operations_window(self):
        from application_windows.operations_window import OperationsWindow
        self.operations_window = OperationsWindow()
        self.operations_window.show()
        self.close()

    def goto_amount_window(self):
        from application_windows.amount_window import AmountWindow
        self.amount_window = AmountWindow()
        self.amount_window.show()
        self.close()

    def goto_journal_window(self):
        from application_windows.journal_window import JournalWindow
        self.journal_window = JournalWindow()
        self.journal_window.show()
        self.close()

    def goto_budget_change_window(self):
        from application_windows.budget_change_window import BudgetChange
        self.budget_change_window = BudgetChange()
        self.budget_change_window.show()
        self.close()

    def goto_threads_window(self):
        from application_windows.financial_threads_window import FinancialThreads
        self.financial_window = FinancialThreads()
        self.financial_window.show()
        self.close()

    def __init__(self):
        self.financial_window = None
        self.budget_change_window = None
        self.journal_window = None
        self.amount_window = None
        self.operations_window = None
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

    def setup_ui(self):
        self.setWindowTitle("Автоматизация домашнего бюджета")

        set_window_geometry(self)
        font = create_font()

        self.operations_button = create_button(self, 0, 0, 400, 200, font=font, object_name='Менеджер операций')
        self.article_button = create_button(self, 400, 0, 400, 200, font=font, object_name='Менеджер квитанций')
        self.streams_button = create_button(self, 400, 200, 400, 200, font, 'Динамика потоков по квитанциям',
                                            background_color='blue')
        self.streams_button.clicked.connect(self.goto_threads_window)
        self.budget_change_button = create_button(self, 0, 200, 400, 200, font, 'Динамика изменения бюджета',
                                                  background_color='blue')
        self.budget_change_button.clicked.connect(self.goto_budget_change_window)
        self.journal_button = create_button(self, 0, 400, 400, 200, font, 'Журнал анализа', background_color='red')
        self.journal_button.clicked.connect(self.goto_journal_window)
        self.amount_button = create_button(self, 400, 400, 400, 200, font, 'Отображение прибыли',
                                           background_color='red')
        self.article_button.clicked.connect(self.goto_article_window)
        self.operations_button.clicked.connect(self.goto_operations_window)
        self.amount_button.clicked.connect(self.goto_amount_window)
        self.setLayout(self.layout)


