from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QThread, pyqtSignal
from main import Receive_and_process
from sys import exit
from sys import argv

class Worker(QThread):
    finished = pyqtSignal()

    def run(self):
        # Запуск функции в фоновом потоке
        Receive_and_process.main()
        # Сообщить, что работа завершена
        self.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt App")
        self.setFixedSize(638, 638)  # Устанавливаем фиксированный размер окна

        # Установка фонового изображения
        background_label = QLabel(self)
        background_pixmap = QPixmap("gui_photo/back.png")
        background_label.setPixmap(background_pixmap)
        background_label.setScaledContents(True)
        background_label.setGeometry(0, 0, 638, 638)
        
        # Создание кнопок меню
        self.menu = Menu(self)
        self.menu.create_buttons()

        # Запуск Receive_and_process.main через QThread
        self.worker = Worker()
        self.worker.finished.connect(self.on_worker_finished)
        self.worker.start()

    def on_worker_finished(self):
        print("Фоновая работа завершена")

class Menu():
    def __init__(self, main_window):
        self.main_window = main_window

    def create_buttons(self):
        button_image = QPixmap("gui_photo/Jarvis main.png").scaled(90, 90)
        button_main = QPushButton("", self.main_window)
        button_main.setIcon(QIcon(button_image))
        button_main.setIconSize(button_image.size())
        button_main.setFlat(True)
        button_main.setGeometry(109, 638-90-18, 90, 90)
        button_main.clicked.connect(self.on_button_click)

        button_image = QPixmap("gui_photo/commands_button.png").scaled(90, 90)
        button_commands = QPushButton("", self.main_window)
        button_commands.setIcon(QIcon(button_image))
        button_commands.setIconSize(button_image.size())
        button_commands.setFlat(True)
        button_commands.setGeometry(219, 638-90-32, 90, 90)
        button_commands.clicked.connect(self.on_button_click2)

        button_image = QPixmap("gui_photo/plugins.png").scaled(90, 90)
        button_plugins = QPushButton("", self.main_window)
        button_plugins.setIcon(QIcon(button_image))
        button_plugins.setIconSize(button_image.size())
        button_plugins.setFlat(True)
        button_plugins.setGeometry(329, 638-90-32, 90, 90)
        button_plugins.clicked.connect(self.on_button_click3)

        button_image = QPixmap("gui_photo/seetings.png").scaled(90, 90)
        button_settings = QPushButton("", self.main_window)
        button_settings.setIcon(QIcon(button_image))
        button_settings.setIconSize(button_image.size())
        button_settings.setFlat(True)
        button_settings.setGeometry(439, 638-90-18, 90, 90)
        button_settings.clicked.connect(self.on_button_click4)

    def on_button_click(self):
        print("Главная страница")

    def on_button_click2(self):
        print("Дерево команд")
    
    def on_button_click3(self):
        print("Плагины")
    
    def on_button_click4(self):
        print("Настройки")

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())
