import random
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class YellowCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.action)

    def action(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            d = random.randint(100, 200)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(100, 100, int(d / 2), int(d / 2))
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = YellowCircle()
    prog.show()
    sys.exit(app.exec())