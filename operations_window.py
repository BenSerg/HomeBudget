from main_window import MainWindow
from create_widgets_functions import *
from window_functions import *
from main import conn


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

    def insert_operation(self):
        cur = conn.cursor()
        cur.execute(f"select id from articles where name = '{self.name_input.text()}'")
        if cur.rowcount == 0:
            msgbox = create_msg_box('Ошибка', f'Квитанции с наименованием {self.name_input.text()} не существует')
        else:
            article_id = cur.fetchone()[0]
            cur.execute(
                f"insert into operations(article_id, debit, credit, create_date) values({article_id}, {self.debit_input.text()}, {self.credit_input.text()}, '{self.datetime_input.text()}')")
            msgbox = create_msg_box('Уведомление', f'Операция по квитанции {self.name_input.text()} успешно вставлена')
        msgbox.exec_()
        conn.commit()

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
        self.ok_button.clicked.connect(self.insert_operation)
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

    def modify_operations(self):
        if not (check_pressed(self.date_choice) or check_pressed(self.article_choice)):
            msgbox = create_msg_box(title='Ошибка', message='Не установлен ключ модификации')
        else:
            modify_key = check_pressed(self.date_choice)
            cur = conn.cursor()
            if modify_key:
                cur.execute(f"select id from operations where create_date = '{self.choice_field.text()}'")
                if cur.rowcount == 0:
                    msgbox = create_msg_box(title='Ошибка', message='Операции с такой датой не существует')
                else:
                    id_op = cur.fetchone()[0]
                    cur.execute(f"select id from articles where name = '{self.article_input.text()}'")
                    if cur.rowcount != 0:
                        article_id = cur.fetchone()[0]
                        cur.execute(
                            f"update operations set debit={self.debit_input.text()}, "
                            f"credit={self.credit_input.text()}, article_id = {article_id}, create_date = '{self.datetime_input.text()}' "
                            f"where id = {id_op}")
                        msgbox = create_msg_box(title='Уведомление', message='Операция успешно модифицирована')
                    else:
                        msgbox = create_msg_box(title='Ошибка', message='Квитанции с таким наименованием не существует')
            else:
                if cur.rowcount != 0:
                    cur.execute(f"select id from articles where name = '{self.choice_field.text()}'")
                    article_id = cur.fetchone()[0]
                    cur.execute(f"select id from operations where article_id = {article_id}")
                    id_op = cur.fetchone()[0]
                    cur.execute(
                        f"update operations set debit={self.debit_input.text()}, "
                        f"credit={self.credit_input.text()}, article_id = {article_id}, create_date = '{self.datetime_input.text()}' "
                        f"where id = {id_op}")
                    msgbox = create_msg_box(title='Уведомление', message=f'Операция по статье {self.choice_field.text()} успешно модифицирована')
                else:
                    msgbox = create_msg_box(title='Ошибка',
                                            message='Операции с таким наименованием квитанции не существует')
        conn.commit()
        msgbox.exec_()

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
        self.article_label = create_label(self, 440, 200, 321, 31, font, 'Наименование квитанции')
        self.datetime_label = create_label(self, 440, 280, 291, 21, font, 'Новая дата')

        self.ok_button = create_ok_button(self, font)
        self.ok_button.clicked.connect(self.modify_operations)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_operations_window)


class OperationsDeleteWindow(QWidget):
    def return_to_operations_window(self):
        self.operations_window = OperationsWindow()
        self.operations_window.show()
        self.close()

    def delete_operation(self):
        if not (check_pressed(self.date_choice) or check_pressed(self.article_choice)):
            msgbox = create_msg_box(title='Ошибка', message='Ключ удаления не установлен')
        else:
            cur = conn.cursor()
            datetime_key = check_pressed(self.date_choice)
            if datetime_key:
                cur.execute(f"select id from operations where create_date = '{self.choice_field.text()}'")
                if cur.rowcount == 0:
                    msgbox = create_msg_box(title='Ошибка', message='Операции с такой датой не существует')
                else:
                    id_op = tuple([i[0] for i in cur.fetchall()])
                    cur.execute(f"delete from operations where id in {id_op}")
                    msgbox = create_msg_box(title='Уведомление',
                                            message=f'Операция c датой {self.choice_field.text()} удалены')
            else:
                cur.execute(f"select id from articles where name = '{self.choice_field.text()}'")
                if cur.rowcount == 0:
                    msgbox = create_msg_box(title='Ошибка', message='Квитанции с таким наименованием не существует')
                else:
                    article_id = cur.fetchone()[0]
                    cur.execute(f"select id from operations where article_id = {article_id}")
                    id_op = cur.fetchone()[0]
                    cur.execute(f"delete from operations where id in {id_op}")
                    msgbox = create_msg_box(title='Уведомление',
                                            message=f'Операция по статье {self.choice_field.text()} успешно удалена')
        msgbox.exec_()

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
        self.ok_button.clicked.connect(self.delete_operation)
        font.setPointSize(41)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_operations_window)
        self.setLayout(self.layout)
