from application_functions.logger import logger
from config.connection import conn
from application_windows.graph_window import *
from application_windows.main_window import MainWindow


class FinancialThreads(QWidget):
    def return_to_main_menu(self):
        self.main_menu = MainWindow()
        self.main_menu.show()
        self.close()

    def create_graph(self):
        cur = conn.cursor()
        query = f"select id from articles where name in {tuple(self.input_field.text().split(','))}"
        cur.execute(query)
        logger.debug(f"Выполнен запрос: {query}")
        ids = tuple(i[0] for i in cur.fetchall())
        query = (
            f"""select article_id,
            case
                when credit = 0 then 0
                else cast(debit / credit as DECIMAL(10,3))
            end as debit_credit_ratio
        from 
            (select
                operations.article_id,
                sum(operations.debit) as debit,
                sum(operations.credit) as credit from operations where operations.article_id in {ids}
             group by operations.article_id) as subquery
            order by 
            article_id;""")
        cur.execute(query)
        logger.debug(f"Выполнен запрос {query}")
        data = cur.fetchall()
        id_hist = tuple([i[0] for i in data])
        query = f"select name from articles where id in {id_hist}"
        cur.execute(query)
        logger.debug(f"Выполнен запрос: {query}")
        names = tuple(i[0] for i in cur.fetchall())
        self.graph_window = GraphWindow(self, [i[1] for i in data], names)
        self.graph_window.show()
        self.close()

    def __init__(self):
        super().__init__()
        self.return_button = None
        self.ok_button = None
        self.key_label = None
        self.input_field = None
        self.graph_window = None
        self.main_menu = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Соотношение финансовых потоков')
        set_window_geometry(self)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(15)
        self.input_field = create_line_edit(self, 50, 200, 700, 60, font)
        font.setBold(True)
        font.setBold(True)
        self.key_label = create_label(self, 50, 125, 800, 50, font, 'Введите через запятую наименования квитанций')
        self.ok_button = create_ok_button(self, font)
        self.ok_button.clicked.connect(self.create_graph)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_main_menu)
