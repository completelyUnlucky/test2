from PyQt5.QtCore import Qt #
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

class Game(QMainWindow):
    def keyPressEvent(self, event):
        key = event.key()
        x = button.x()
        y = button.y()

        if key == Qt.Key_Left:
            button.move(button.x() - 10, button.y())
            button.setPixmap(pixmap2)
        if key == Qt.Key_Right:
            button.move(button.x() + 10, button.y())
            button.setPixmap(pixmap3)
        if key == Qt.Key_Up:
            button.move(button.x(), button.y() - 10)
            button.setPixmap(pixmap4)
        if key == Qt.Key_Down:
            button.move(button.x(), button.y() + 10)
            button.setPixmap(pixmap5)
        if key == Qt.Key_7:
            button.move(button.x() - 10,button.y() - 10)
        if key == Qt.Key_9:
            button.move(button.x() + 10, button.y() - 10)
        if key == Qt.Key_3:
            button.move(button.x() + 10, button.y() + 10)
        if key == Qt.Key_1:
            button.move(button.x() - 10, button.y() + 10)
        if button.x() > 700:
            button.move(button.x() - 700, button.y())
        if button.x() < -100:
            button.move(button.x() + 700, button.y())
        if button.y() > 700:
            button.move(button.x(), button.y() - 700)
        if button.y() < -100:
            button.move(button.x(), button.y() + 700)
        if key == Qt.Key_Space:
            bullet.setPixmap(pixmap7)
            self.timer = QTimer(window)
            bullet.move(x + 45, y + 12)
            self.timer.setInterval(10)
            self.timer.timeout.connect(self.move_bullet)
            self.timer.start()

    def move_bullet(self):
        bullet.move(self.bullet.x(), self.bullet.y() - 1)

        if button.setPixmap(pixmap2):
            bullet.move(self.bullet.x() - 1, self.bullet.y())









if __name__ == '__main__':
    app = QApplication([])
    window = Game()
    window.setFixedSize(600, 600)

    map = QLabel(window)
    map.setFixedSize(600, 600)



    button = QLabel(window)
    button.setFixedSize(100, 100)
    pixmap1 = QPixmap('/Users/admin/PycharmProject/untitledBORIS/TanchikPryamo.png')
    pixmap2 = QPixmap('/Users/admin/PycharmProject/untitledBORIS/TanchikVlevo.png')
    pixmap3 = QPixmap('/Users/admin/PycharmProject/untitledBORIS/TanchikRight.png')
    pixmap4 = QPixmap('/Users/admin/PycharmProject/untitledBORIS/TanchikPryamo.png')
    pixmap5 = QPixmap('//Users/admin/PycharmProject/untitledBORIS/TanchikDown.png')
    pixmap6 = QPixmap('/Users/admin/PycharmProject/untitledBORIS/MAP.png')
    pixmap7 = QPixmap('/Users/admin/PycharmProject/untitledBORIS/SnaryadVpered.png')
    pixmap8 = QPixmap('/Users/admin/PycharmProject/untitledBORIS/SnaryadVlevo.png')
    button.setPixmap(pixmap1)
    timer = QTimer(window)
    map.setPixmap(pixmap6)
    bullet = QLabel(window)
    bullet.setFixedSize(15, 15)
    window.bullet = []
    window.bullet = bullet
    window.bullet.show()


    button.move(250, 250)
    button.show()
    map.show()
    button.setFocusPolicy(Qt.NoFocus)










    window.show()
    app.exec()