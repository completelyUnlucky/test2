from PyQt5.QtCore import Qt  # это нужно для отключения фокуса
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QTimer


class Bullet:
    def __init__(self, window, direction, pos):
        self.pos = pos
        self.direction = direction
        self.speed = 2

        self.bullet = QPushButton(window)
        self.bullet.resize(10, 10)
        self.bullet.move(pos[0], pos[1])
        self.bullet.show()

        self.timer = QTimer(window)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.move)

    def move(self):
        self.bullet.move(self.bullet.x()+self.direction[0]*self.speed, self.bullet.y() + self.direction[1]*self.speed)
        if 0 > self.bullet.x() > 600 or 0 > self.bullet.y() > 600:
            self.bullet.deleteLater()
            self.__del__()

    def __del__(self):
        pass


class Game(QMainWindow):
    def __init__(self):
        super(Game, self).__init__()

        self.resize(600, 600)
        self.tank = QPushButton(self)
        self.tank.resize(50, 50)
        self.tank.move(275, 275)
        self.bullet = []
        self.tank.setFocusPolicy(Qt.NoFocus)



    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_F:
            # if len(self.bullet) < 3:
            self.bullet.append(Bullet(self, (1, 0), (self.tank.x(), self.tank.y())))
            self.bullet[-1].bullet.setFocusPolicy(Qt.NoFocus)
            self.bullet[-1].timer.start()
        if key == Qt.Key_Right:
            self.tank.move(self.tank.x() + 5, self.tank.y())
        if key == Qt.Key_Left:
            self.tank.move(self.tank.x() - 5, self.tank.y())
        if key == Qt.Key_Up:
            self.tank.move(self.tank.x(), self.tank.y() - 5)
        if key == Qt.Key_Down:
            self.tank.move(self.tank.x(), self.tank.y() + 5)

if __name__ == "__main__":
    app = QApplication([])
    win = Game()
    win.show()
    app.exec()
