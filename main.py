import os
import sys
from PySide2.QtWidgets import QApplication
from src.ui_main import MainWindow

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # アプリケーション作成
    app = QApplication(sys.argv)
    # オブジェクト作成
    window = MainWindow()
    # MainWindowの表示_
    window.show()

    sys.exit(app.exec_())
