from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QTimer


class Bullet:
    def __init__(self, win):
        self.timer = QTimer(win)
        self.timer.setInterval(10)
        self.speed = 1
        self.pos = self.x, self.y = 270, 270
        self.size = self.length, self.width = 60, 60
        self.button = QPushButton()
        self.button.show()
        self.button.resize(self.length, self.width)
        self.button.move(self.x, self.y)
        self.timer.timeout.connect(self.move)
        self.dirrection = False
        self.timer.start()

    def move(self):
        if self.button.x() > 800:
            self.dirrection = True
        if self.button.x() < 0:
            self.dirrection = False
        if not self.dirrection:
            self.button.move(self.button.x() + 10, self.button.y())
        else:
            self.button.move(self.button.x() - 10, self.button.y())





if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    window.resize(800, 800)
    bullet = Bullet(window)

    window.show()
    app.exec()


