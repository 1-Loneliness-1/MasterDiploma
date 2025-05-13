from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt, QTimer, QRectF
from PyQt6.QtGui import QPainter, QColor, QFont, QPainterPath, QBrush

class ToastWidget(QLabel):
    def __init__(self, parent=None, message="", duration=2000):
        super().__init__(parent)
        self.message = message
        self.duration = duration

        # Прозрачность + поверх всех окон
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Tool |
            Qt.WindowType.WindowStaysOnTopHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)

        self.setFont(QFont("Segoe UI", 16))
        self.setStyleSheet("color: #444444;")  # Цвет текста

        self.adjustSize()

        # Центрирование внизу окна
        if parent:
            self.resize(300, 50)
            parent_rect = parent.geometry()
            x = parent_rect.x() + (parent_rect.width() - self.width()) // 2
            y = parent_rect.y() + parent_rect.height() - self.height() - 40
            self.move(x, y)

        self.show()

        QTimer.singleShot(self.duration, self.close)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        rect = QRectF(0, 0, self.width(), self.height())

        # Цвет фона (светло-серый) и закругления
        bg_color = QColor(255, 255, 255, 245)  # почти белый с легкой прозрачностью
        border_radius = 10

        path = QPainterPath()
        path.addRoundedRect(rect, border_radius, border_radius)

        painter.setBrush(QBrush(bg_color))
        painter.setPen(QColor(230, 230, 230))  # светло-серый бордер
        painter.drawPath(path)

        # Рисуем текст
        painter.setPen(QColor("#444444"))
        painter.drawText(
            rect,
            Qt.AlignmentFlag.AlignCenter,
            self.message
        )
