from PyQt5.QtWidgets import QWidget

window_width = 800
window_height = 600


def set_window_geometry(widget: QWidget, width=window_width, height=window_height):
    widget.setGeometry(0, 0, width, height)
