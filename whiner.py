from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint


app = QApplication([])
main_win = QWidget()
main_win.resize(1000, -1)
button = QPushButton('Згеренувати')
text = QLabel('Натисніть щоб дізнатися переможця')
winner = QLabel('?')

winner = QLabel('Переможець:')
v_line = QVBoxLayout()
v_line.addWidget(winner, alignment = Qt.AlignCenter)
v_line.addWidget(button, alignment = Qt.AlignCenter)
v_line.addWidget(text, alignment = Qt.AlignCenter)
main_win.setLayout(v_line)

def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))

button.clicked.connect(show_winner)


main_win.show()
app.exec_()