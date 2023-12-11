from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QStackedWidget, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QDateTimeEdit, \
    QRadioButton, QLabel


def create_label(widget, x, y, width, height, font, object_name):
    label = QLabel(object_name, widget)
    label.setGeometry(QtCore.QRect(x, y, width, height))
    label.setFont(font)
    label.setObjectName(object_name)
    return label


def create_button(widget, x, y, width, height, font, object_name, background_color='white'):
    button = QPushButton(object_name, widget)
    button.setGeometry(QtCore.QRect(x, y, width, height))
    button.setFont(font)
    button.setStyleSheet(f'background-color: {background_color};')
    button.setObjectName(object_name)
    return button


def create_return_button(widget, font):
    return create_button(widget, 0, 0, 91, 51, font, '←')


def create_font(family='Serif', size=15):
    font = QtGui.QFont()
    font.setFamily(family)
    font.setPointSize(size)
    return font


def create_line_edit(widget, x, y, width, height, font, background_color='white'):
    line_edit = QLineEdit(widget)
    line_edit.setGeometry(QtCore.QRect(x, y, width, height))
    line_edit.setFont(font)
    line_edit.setStyleSheet(f'background-color: {background_color};')
    return line_edit


def create_datetime_edit(widget, x, y, width, height, font, background_color='white'):
    line_edit = QDateTimeEdit(widget)
    line_edit.setGeometry(QtCore.QRect(x, y, width, height))
    line_edit.setFont(font)
    line_edit.setStyleSheet(f'background-color: {background_color};')
    return line_edit


def create_ok_button(widget, font):
    return create_button(widget, 300, 450, 141, 81, font, 'OK')


def create_radio_button(widget, x, y, width, height, font, object_name, background_color='white'):
    button = QRadioButton(object_name, widget)
    button.setGeometry(QtCore.QRect(x, y, width, height))
    button.setFont(font)
    button.setStyleSheet(f'background-color: {background_color};')
    button.setObjectName(object_name)
    return button