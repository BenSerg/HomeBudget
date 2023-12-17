from PyQt5.QtWidgets import QWidget, QVBoxLayout

from application_functions.create_widgets_functions import create_font, create_line_edit, create_label, \
    create_ok_button, create_return_button, create_button, create_msg_box
from application_functions.window_functions import set_window_geometry
from config.connection import conn


class RegisterWindow(QWidget):
    def goto_main_window(self):
        from application_windows.auth_window import AuthWindow
        self.auth_window = AuthWindow()
        self.auth_window.show()
        self.close()

    def __init__(self):
        super().__init__()
        self.register_button = None
        self.auth_window = None
        self.return_button = None
        self.main_window = None
        self.ok_button = None
        self.password_label = None
        self.password_input = None
        self.username_label = None
        self.username_input = None
        self.layout = QVBoxLayout()
        self.setup_ui()

    def register(self):
        cur = conn.cursor()
        cur.execute(
            f"insert into users(user_name, user_password) values('{self.username_input.text()}', md5('{self.password_input.text()}'))")
        msgbox = create_msg_box(title='Уведомление', message='Пользователь зарегистрирован')
        msgbox.exec_()
        conn.commit()

    def setup_ui(self):
        self.setWindowTitle('Регистрация')
        set_window_geometry(self)
        font = create_font()

        self.username_input = create_line_edit(self, 245, 120, 311, 31, font)

        self.password_input = create_line_edit(self, 245, 250, 311, 31, font)

        font.setBold(True)
        self.username_label = create_label(self, 245, 90, 350, 31, font, 'Логин пользователя')
        self.password_label = create_label(self, 245, 220, 350, 31, font, 'Пароль пользователя')
        self.ok_button = create_ok_button(self, font)
        self.ok_button.clicked.connect(self.register)

        font.setPointSize(41)
        font.setWeight(75)

        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.goto_main_window)
        self.setLayout(self.layout)
