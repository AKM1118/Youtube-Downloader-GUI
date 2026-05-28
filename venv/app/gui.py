# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIcmGUfN.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import file_info

from PySide6.QtCore import QFile, QIODevice

from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow

from PySide6.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загружаем UI
        loader = QUiLoader()
        ui_file_obj = QFile("venv/app/GUI.ui")
        ui_file_obj.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file_obj)
        self.setCentralWidget(self.ui)
        self.setBaseSize(794,582)
        #print(self.ui.GetInfo)
        ui_file_obj.close()

        # Загружаем UI файл
        """
        loader = QUiLoader()
        ui_file_obj = QFile("venv/app/GUI.ui")
        ui_file_obj.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file_obj, self)
        print(self.ui)
        ui_file_obj.close()
        """
        # Подключаем кнопку
        self.ui.GetInfo.clicked.connect(self.on_button_click)
    
    def on_button_click(self):
        """Обработчик нажатия кнопки"""
        # Извлекаем текст из LineEdit
        text = self.ui.URLedit.text()
        self.ui.Result.clear()
        self.ui.Result.appendPlainText(file_info.get_formats(text))
        # Показываем результат
        QMessageBox.information(self, "Информация", f"Введено: {text}")

if __name__ == "__main__":
    # test
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    print("Application closed")