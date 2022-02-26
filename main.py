import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui import Ui_MainWindow


class Drawer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.draw_button.clicked.connect(self.paint)
        self.can_paint = False

    def paintEvent(self, event):
        if self.can_paint:
            painter = QPainter()
            painter.begin(self)
            self.draw_circles(painter)
            painter.end()

    def paint(self):
        self.can_paint = True
        self.repaint()

    def draw_circles(self, painter):
        for i in range(randint(1, 10)):
            painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            r = randint(10, 130)
            painter.drawEllipse(randint(0, 700), randint(0, 600), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Drawer()
    form.show()
    sys.exit(app.exec())
