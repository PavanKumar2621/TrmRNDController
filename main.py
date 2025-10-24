import sys
from PySide6.QtWidgets import *
from ui_trm_rnd_controller import TrmRNDController


if __name__ == "__main__":
    app = QApplication([])
    trmController = TrmRNDController()
    trmController.show()
    sys.exit(app.exec())
