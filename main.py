from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QHBoxLayout, QMessageBox, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])#сворюємо додаток

from card_window import main_line

main_win = QWidget()#створюємо вікно
main_win.setWindowTitle("Memory Card")#назва вікна
main_win.resize(600, 500)#розмір
main_win.move(350, 150)
main_win.setLayout(main_line)
main_win.show()
app.exec_()