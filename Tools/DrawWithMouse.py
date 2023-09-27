from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import numpy as np


class DrawWidget(QLabel):
    send_all_coordinates = Signal(int, int, int, int)

    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setScaledContents(True)
        self.start_point = None
        self.end_point = None
        self.completed_rect = None
        self.drawing = False
        self.setCursor(Qt.CrossCursor)
        self.rectangle = True

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.start_point = event.pos()
            self.end_point = event.pos()
            self.send_all_coordinates.emit(self.start_point.x(), self.start_point.y(), event.pos().x(), event.pos().y())

    def mouseMoveEvent(self, event):
        if self.start_point:
            self.end_point = event.pos()
            self.send_all_coordinates.emit(self.start_point.x(), self.start_point.y(), event.pos().x(), event.pos().y())
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.completed_rect = QRect(self.start_point, self.end_point).normalized()
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.black)
        if self.rectangle:
            if self.drawing:
                rect = QRect(self.start_point, self.end_point).normalized()
                painter.drawRect(rect)
                painter.end()
            elif self.completed_rect:
                painter.drawRect(self.completed_rect)
                painter.end()
        else:
            if self.start_point and self.end_point:
                # img = qimage_to_cv2(self.pixmap().toImage())
                direction = self.end_point - self.start_point
                length = np.linalg.norm([direction.x(), direction.y()])
                direction = direction * 100 / length
                endpoint = self.start_point + direction
                painter.drawLine(self.start_point, endpoint)
                painter.end()
