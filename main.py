import sys
from PySide6.QtWidgets import *
from ui_trm_rnd_controller import TrmRNDController


if __name__ == "__main__":
    app = QApplication([])
    trmController = TrmRNDController()
    trmController.show()
    sys.exit(app.exec())

# rb2 =1
# rb1 =1

# rblk_CTL =( rb2 <<1) | rb1

# print(rblk_CTL)