from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QLabel, QBoxLayout, QHBoxLayout, QLayout, \
    QVBoxLayout, QWidget

def click(button):
    label = QLabel(button)
    label.move(30, 30)
    label.setFixedSize(30, 30)
    label.setStyleSheet("background-color: red")
    label.
    button.repaint()

if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    window.setFixedSize(600, 600)

    button = QWidget()
    button.move(260, 260)
    button.setFixedSize(80, 80)
    window.layout().addWidget(button)
    button.setStyleSheet("background-color: green")

    label = QLabel(button)
    label.move(10, 10)
    label.setFixedSize(30, 30)
    label.setStyleSheet("background-color: red")


    b = QPushButton()
    b.move(400, 400)
    b.setFixedSize(100, 100)
    window.layout().addWidget(b)
    b.clicked.connect(lambda : click(button))









    window.show()
    app.exec()