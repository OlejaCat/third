import random
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class YellowCircle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.setupUi(self)

        self.pushButton.clicked.connect(self.action)

    def action(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            d = random.randint(100, 200)
            r = random.randint(0, 254)
            g = random.randint(0, 254)
            b = random.randint(0, 254)
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(100, 100, int(d / 2), int(d / 2))
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = YellowCircle()
    prog.show()
    sys.exit(app.exec())