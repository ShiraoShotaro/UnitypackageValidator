import os
from PySide2.QtWidgets import QFileDialog, QMessageBox
from PySide2 import QtCore, QtGui
from PySide2.QtUiTools import QUiLoader


##
# @brief グローバル設定を変更するためのuiクラス
class SettingsDialog():

    def __init__(self, parent=None):
        # UI初期化処理
        self.ui = QUiLoader().load(os.path.join(os.getcwd(), 'ui/AssetListAddress.ui'), parent)

    @classmethod
    def showDialog(cls, parent):
        dialog = SettingsDialog(parent)
        dialog.ui.exec()
