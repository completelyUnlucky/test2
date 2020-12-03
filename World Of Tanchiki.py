from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QTimer


class Bullet:
    def __init__(self, window):
        self.timer = QTimer(window)
        self.timer.setInterval(20)
        self.speed = 4
        self.pos = self.x, self.y = 240, 240
        self.size = self.length, self.width = 100, 100
        self.button = QPushButton(window)
        self.button.show()
        self.button.resize(self.length, self.width)
        self.button.move(self.x, self.y)
        self.timer.timeout.connect(self.move)
        self.dirrections = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
        self.dir_num = 0
        self.timer.start()

    def move(self):
        if self.dir_num == 4:
            self.dir_num = 0
        self.button.move(self.button.x() + self.dirrections[self.dir_num][0] * self.speed,
                         self.button.y() + self.dirrections[self.dir_num][1] * self.speed)
        if self.button.x() < 0 or self.button.x() > 700 or self.button.y() < 0 or self.button.y() > 700:
            self.dir_num += 1


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    window.resize(800, 800)
    window.bullet = Bullet(window)

    window.show()
    app.exec()


