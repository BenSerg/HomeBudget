from create_widgets_functions import *
from window_functions import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class GraphWindow(QWidget):
    def return_to_parent_window(self):
        self.parent.show()
        self.close()

    def __init__(self, parent: QWidget):
        super().__init__()
        self.return_button = None
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('График')
        set_window_geometry(self)
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 1, 5, 2]
        plt.plot(x, y, color='r')
        plt.savefig('plot.png')
        plt_label = QLabel(self)
        plot_pixmap = QtGui.QPixmap('plot.png')
        plt_label.setPixmap(plot_pixmap)
        font = create_font(size=41)
        font.setBold(True)
        font.setWeight(75)
        self.return_button = create_return_button(self, font)
        self.return_button.clicked.connect(self.return_to_parent_window)
