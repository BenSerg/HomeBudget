from PyQt5 import QtWidgets

from application_windows.auth_window import AuthWindow

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    open('config/postgresql.log', 'w').close()
    ui = AuthWindow()
    ui.show()
    sys.exit(app.exec_())
