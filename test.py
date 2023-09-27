from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import  *
import  numpy as np

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.arrow_pos = QPoint(100, 100)  # position of the arrow
        self.arrow_angle = 45  # angle of the arrow in degrees
        self.arrow_length = 50  # length of the arrow
        self.arrow_width = 10  # width of the arrow
        self.arrow_head_length = 10  # length of the arrow head
        self.arrow_head_width = 10  # width of the arrow head

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # draw the line
        line_end = self.arrow_pos + QPoint(self.arrow_length * np.cos(np.deg2rad(self.arrow_angle)),
                                           -self.arrow_length * np.sin(np.deg2rad(self.arrow_angle)))
        line = QLineF(self.arrow_pos, line_end)
        pen = QPen(QColor(0, 0, 255))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(line)

        # draw the arrow head
        arrow_head = QPolygonF()
        arrow_head.append(line.p2())
        arrow_head.append(line.p2() - QSizeF(self.arrow_head_length, self.arrow_width / 2).toPointF().rotated(-self.arrow_angle))
        arrow_head.append(line.p2() - QSizeF(self.arrow_head_length, -self.arrow_width / 2).toPointF().rotated(-self.arrow_angle))
        brush = QBrush(QColor(0, 0, 255))
        painter.setBrush(brush)
        painter.drawPolygon(arrow_head)


if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()
