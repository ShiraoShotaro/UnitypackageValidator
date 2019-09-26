import os

from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

from .ui_settings import SettingsDialog


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        # UI初期化処理
        super(MainWindow, self).__init__(parent)
        self.ui = QUiLoader().load(os.path.join(os.getcwd(), 'ui/UnitypackageValidator.ui'))
        self.setCentralWidget(self.ui)
        self.setWindowTitle('Unitypackage Validator - version 0.0.1')

        self.ui.acSettingFile.triggered.connect(self.showSettingUI)

    def showSettingUI(self):
        SettingsDialog.showDialog(self)
