################################################################################
## Designed by Pavan Kumar Madem
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from communication import Communication
# from controls import Controls
import rc_resources


class TrmRNDController(QWidget):  # Wrapper class
    def __init__(self, parent=None):
        super(TrmRNDController, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Initialize Communication  
        self.communication = Communication(self.ui) 


        # Toggle Controls
        self.ui.blkSwAll.currentIndexChanged.connect(lambda: self.changeBlkSwAllControls(self.ui.blkSwAll.currentIndex()))
        self.ui.trCTCLAll.currentIndexChanged.connect(lambda: self.changeTrCTCLAllControls(self.ui.trCTCLAll.currentIndex()))

        # Connect UI elements to communication methods
        self.ui.comPort.showPopup = self.communication.update_com_ports
        self.ui.comPort.mousePressEvent = lambda event: (self.communication.update_com_ports(), QComboBox.mousePressEvent(self.ui.comPort, event))
        self.ui.connect.clicked.connect(lambda: self.communication.toggleConnection(self.ui.comPort.currentText(), self.ui.baudRate.currentText()))        
        self.ui.btnGetStatus.clicked.connect(lambda: self.communication.getStatus())

        # Signal Connections
        self.communication.data_received_signal.connect(self.communication.handle_received_data)

        # Send Control
        self.ui.btnClear.clicked.connect(lambda: self.ui.textbox.clear())
        self.ui.btnRND.clicked.connect(lambda: self.communication.controlsRND())

    def changeBlkSwAllControls(self, index):
        for i in range(1, 9):
            getattr(self.ui, f'blkSw{i}').setCurrentIndex(index)

    def changeTrCTCLAllControls(self, index):
        for i in range(1, 9):
            getattr(self.ui, f'trCTCL{i}').setCurrentIndex(index)

    def closeEvent(self, event):
        if hasattr(self, 'communication') and self.communication:
            self.communication.stop_reader()
            if self.communication.serial_port and self.communication.serial_port.is_open:
                self.communication.serial_port.close()
        event.accept()  
 
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1111, 729)
        Form.setMinimumSize(QSize(1111, 729))
        Form.setMaximumSize(QSize(1111, 729))
        Form.setStyleSheet(u"\n"
"QGroupBox {\n"
"	border: 1px solid rgba(255, 255, 255, 0.3);\n"
"	border-radius: 10px;\n"
"	color: lightgreen;\n"
"}\n"
"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(14, 20, 27);\n"
"\n"
"")
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 10, 1091, 61))
        font = QFont()
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Larger text size for emphasis */\n"
"    font-weight: bold; /* Bold for a professional look */\n"
"    color: #36af8d; /* Dark gray text for a premium feel */\n"
"	background: none; /* Transparent background */\n"
"    border: 2px solid #00ADB5; /* Narrow surrounding border */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    padding: 5px 15px; /* Space inside the border */\n"
"    text-align: center; /* Center the text */\n"
"    letter-spacing: 1px; /* Slight spacing between letters */\n"
"}\n"
"")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(9, 80, 1091, 641))
        self.groupBox.setSizeIncrement(QSize(937, 428))
        self.groupBox.setStyleSheet(u"QCombobox {\n"
"color: white;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QLabel{\n"
"color: White;\n"
"}\n"
"/* Button styling */\n"
"QPushButton {\n"
"    background-color: orange;\n"
"    color: black;\n"
"    border: none;\n"
"    height: 35px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: darkorange;\n"
"}")
        self.radar_groupbox_12 = QGroupBox(self.groupBox)
        self.radar_groupbox_12.setObjectName(u"radar_groupbox_12")
        self.radar_groupbox_12.setGeometry(QRect(10, 10, 281, 181))
        self.radar_groupbox_12.setFont(font)
        self.radar_groupbox_12.setStyleSheet(u"QComboBox {\n"
"    color: white;\n"
"    background-color: #2a2f3b;\n"
"    border-radius: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 25px;  /* reserve space for arrow */\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* Drop-down list (popup) */\n"
"QComboBox QAbstractItemView {\n"
"    background: transparent;             /* remove backside background */\n"
"    color: white;\n"
"    selection-background-color: #323741;\n"
"    selection-color: white;\n"
"    border: none;                        /* remove border */\n"
"    outline: 0;\n"
"    padding-left: 8px;                   /* add space from left */\n"
"    padding-right: 5px;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"/* Hover effect on closed combo box */\n"
"QComboBox:hover {\n"
"    background-color: #323741;\n"
"}\n"
"\n"
"/* Drop-down arrow area (right side) */\n"
"QComboBox::drop-down {\n"
"    border: none;                        /* no border */\n"
"    width: 25px;\n"
"    subcontrol-origin: padding;\n"
"    subco"
                        "ntrol-position: top right;\n"
"    background: transparent;             /* keep transparent */\n"
"}\n"
"\n"
"/* Arrow image */\n"
"QComboBox::down-arrow {\n"
" \n"
"	image: url(:/newPrefix/resources/arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Button styling */\n"
"QPushButton {\n"
"    background-color: orange;\n"
"    color: black;\n"
"    border: none;\n"
"    height: 45px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: darkorange;\n"
"}\n"
"\n"
"")
        self.comPort = QComboBox(self.radar_groupbox_12)
        self.comPort.addItem("")
        self.comPort.addItem("")
        self.comPort.addItem("")
        self.comPort.setObjectName(u"comPort")
        self.comPort.setGeometry(QRect(131, 38, 111, 25))
        self.label_64 = QLabel(self.radar_groupbox_12)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(37, 38, 71, 26))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_64.setFont(font1)
        self.label_64.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.baudRate = QComboBox(self.radar_groupbox_12)
        self.baudRate.addItem("")
        self.baudRate.addItem("")
        self.baudRate.addItem("")
        self.baudRate.addItem("")
        self.baudRate.addItem("")
        self.baudRate.addItem("")
        self.baudRate.setObjectName(u"baudRate")
        self.baudRate.setGeometry(QRect(130, 82, 111, 25))
        self.label_70 = QLabel(self.radar_groupbox_12)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(36, 81, 81, 26))
        self.label_70.setFont(font1)
        self.label_70.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.connect = QPushButton(self.radar_groupbox_12)
        self.connect.setObjectName(u"connect")
        self.connect.setGeometry(QRect(90, 130, 101, 25))
        self.connect.setMaximumSize(QSize(16777215, 25))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(300, 9, 781, 140))
        self.textbox = QTextEdit(self.groupBox_2)
        self.textbox.setObjectName(u"textbox")
        self.textbox.setGeometry(QRect(10, 9, 761, 121))
        self.textbox.setStyleSheet(u"QTextEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Vertical scrollbar */\n"
"QScrollBar:vertical {\n"
"    background: #2a2f3b;           /* scrollbar background (dark) */\n"
"    width: 12px;                   /* adjust width */\n"
"    margin: 2px 0 2px 0;           /* top/bottom margin */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #555;              /* scrollbar handle color */\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #777;              /* handle color on hover */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;              /* remove top/bottom buttons */\n"
"    height: 0px;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-pag"
                        "e:vertical {\n"
"    background: none;              /* remove page areas */\n"
"}\n"
"\n"
"/* Horizontal scrollbar (if you want to style too) */\n"
"QScrollBar:horizontal {\n"
"    background: #2a2f3b;\n"
"    height: 12px;\n"
"    margin: 0 2px 0 2px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #555;\n"
"    min-width: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #777;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"    width: 0px;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.btnClear = QPushButton(self.groupBox)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(300, 160, 71, 25))
        self.btnClear.setMaximumSize(QSize(16777215, 25))
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 200, 741, 231))
        self.groupBox_3.setFont(font)
        self.radar_groupbox_15 = QGroupBox(self.groupBox_3)
        self.radar_groupbox_15.setObjectName(u"radar_groupbox_15")
        self.radar_groupbox_15.setGeometry(QRect(9, 21, 274, 200))
        self.radar_groupbox_15.setFont(font)
        self.radar_groupbox_15.setStyleSheet(u"QComboBox {\n"
"    color: white;\n"
"    background-color: #2a2f3b;\n"
"    border: 1px  #ccc;\n"
"    border-radius: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 1px;\n"
"    font-size: 12px;\n"
"}\n"
"/* Hover effect on closed combo box */\n"
"QComboBox:hover {\n"
"    background-color: #323741;\n"
"}\n"
"/* Drop-down arrow */\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"    subcontrol-origin: padding; \n"
"    subcontrol-position: top right;\n"
"    background: transparent;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    \n"
"	image: url(:/newPrefix/resources/arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Drop-down popup (list view) with dark theme */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2a2f3b;              /* dark background */\n"
"    color: white;                           /* white text */\n"
"    selection-background-color: #323741;    /* slightly lighter dark when selected */\n"
"   "
                        " selection-color: white;\n"
"    border: 1px solid #444;                 /* subtle dark border */\n"
"    padding: 5px;\n"
"    outline: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Vertical scrollbar inside combo popup */\n"
"QComboBox QAbstractItemView QScrollBar:vertical {\n"
"    background: #2a2f3b;           /* dark scrollbar track */\n"
"    width: 10px;\n"
"    margin: 2px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical {\n"
"    background: #555;              /* scrollbar handle */\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical:hover {\n"
"    background: #777;              /* lighter on hover */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::add-line:vertical,\n"
"QComboBox QAbstractItemView QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    height: 0px;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::a"
                        "dd-page:vertical,\n"
"QComboBox QAbstractItemView QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: orange;\n"
"color: black;\n"
"border: none;\n"
"height: 35px;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: darkorange;\n"
"}\n"
"\n"
"")
        self.label_75 = QLabel(self.radar_groupbox_15)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(12, 30, 51, 26))
        font2 = QFont()
        font2.setPointSize(9)
        self.label_75.setFont(font2)
        self.label_76 = QLabel(self.radar_groupbox_15)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(12, 60, 51, 26))
        self.label_76.setFont(font2)
        self.label_77 = QLabel(self.radar_groupbox_15)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(12, 118, 51, 26))
        self.label_77.setFont(font2)
        self.label_78 = QLabel(self.radar_groupbox_15)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(12, 90, 51, 26))
        self.label_78.setFont(font2)
        self.label_79 = QLabel(self.radar_groupbox_15)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(148, 59, 51, 26))
        self.label_79.setFont(font2)
        self.label_80 = QLabel(self.radar_groupbox_15)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(148, 88, 51, 26))
        self.label_80.setFont(font2)
        self.label_81 = QLabel(self.radar_groupbox_15)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(148, 118, 51, 26))
        self.label_81.setFont(font2)
        self.label_82 = QLabel(self.radar_groupbox_15)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(148, 29, 51, 26))
        self.label_82.setFont(font2)
        self.lblAttTx = QLabel(self.radar_groupbox_15)
        self.lblAttTx.setObjectName(u"lblAttTx")
        self.lblAttTx.setGeometry(QRect(60, 158, 51, 26))
        self.lblAttTx.setFont(font2)
        self.blkSw1 = QComboBox(self.radar_groupbox_15)
        self.blkSw1.addItem("")
        self.blkSw1.addItem("")
        self.blkSw1.setObjectName(u"blkSw1")
        self.blkSw1.setGeometry(QRect(70, 30, 62, 22))
        self.blkSw3 = QComboBox(self.radar_groupbox_15)
        self.blkSw3.addItem("")
        self.blkSw3.addItem("")
        self.blkSw3.setObjectName(u"blkSw3")
        self.blkSw3.setGeometry(QRect(70, 60, 62, 22))
        self.blkSw5 = QComboBox(self.radar_groupbox_15)
        self.blkSw5.addItem("")
        self.blkSw5.addItem("")
        self.blkSw5.setObjectName(u"blkSw5")
        self.blkSw5.setGeometry(QRect(70, 90, 62, 22))
        self.blkSw7 = QComboBox(self.radar_groupbox_15)
        self.blkSw7.addItem("")
        self.blkSw7.addItem("")
        self.blkSw7.setObjectName(u"blkSw7")
        self.blkSw7.setGeometry(QRect(70, 120, 62, 22))
        self.blkSw8 = QComboBox(self.radar_groupbox_15)
        self.blkSw8.addItem("")
        self.blkSw8.addItem("")
        self.blkSw8.setObjectName(u"blkSw8")
        self.blkSw8.setGeometry(QRect(200, 120, 62, 22))
        self.blkSw4 = QComboBox(self.radar_groupbox_15)
        self.blkSw4.addItem("")
        self.blkSw4.addItem("")
        self.blkSw4.setObjectName(u"blkSw4")
        self.blkSw4.setGeometry(QRect(200, 60, 62, 22))
        self.blkSw6 = QComboBox(self.radar_groupbox_15)
        self.blkSw6.addItem("")
        self.blkSw6.addItem("")
        self.blkSw6.setObjectName(u"blkSw6")
        self.blkSw6.setGeometry(QRect(200, 90, 62, 22))
        self.blkSw2 = QComboBox(self.radar_groupbox_15)
        self.blkSw2.addItem("")
        self.blkSw2.addItem("")
        self.blkSw2.setObjectName(u"blkSw2")
        self.blkSw2.setGeometry(QRect(200, 30, 62, 22))
        self.blkSwAll = QComboBox(self.radar_groupbox_15)
        self.blkSwAll.addItem("")
        self.blkSwAll.addItem("")
        self.blkSwAll.setObjectName(u"blkSwAll")
        self.blkSwAll.setGeometry(QRect(130, 160, 62, 22))
        self.radar_groupbox_16 = QGroupBox(self.groupBox_3)
        self.radar_groupbox_16.setObjectName(u"radar_groupbox_16")
        self.radar_groupbox_16.setGeometry(QRect(291, 21, 271, 200))
        self.radar_groupbox_16.setFont(font)
        self.radar_groupbox_16.setStyleSheet(u"QComboBox {\n"
"    color: white;\n"
"    background-color: #2a2f3b;\n"
"    border: 1px  #ccc;\n"
"    border-radius: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 1px;\n"
"    font-size: 12px;\n"
"}\n"
"/* Hover effect on closed combo box */\n"
"QComboBox:hover {\n"
"    background-color: #323741;\n"
"}\n"
"/* Drop-down arrow */\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"    subcontrol-origin: padding; \n"
"    subcontrol-position: top right;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"  \n"
"	image: url(:/newPrefix/resources/arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Drop-down popup (list view) with dark theme */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2a2f3b;              /* dark background */\n"
"    color: white;                           /* white text */\n"
"    selection-background-color: #323741;    /* slightly lighter dark when selected */\n"
"    selection-color: white;\n"
"    "
                        "border: 1px solid #444;                 /* subtle dark border */\n"
"    padding: 5px;\n"
"    outline: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Vertical scrollbar inside combo popup */\n"
"QComboBox QAbstractItemView QScrollBar:vertical {\n"
"    background: #2a2f3b;           /* dark scrollbar track */\n"
"    width: 10px;\n"
"    margin: 2px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical {\n"
"    background: #555;              /* scrollbar handle */\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical:hover {\n"
"    background: #777;              /* lighter on hover */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::add-line:vertical,\n"
"QComboBox QAbstractItemView QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    height: 0px;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::add-page:vertical,\n"
"QComboBox Q"
                        "AbstractItemView QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: orange;\n"
"color: black;\n"
"border: none;\n"
"height: 35px;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: darkorange;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"}\n"
"")
        self.label_84 = QLabel(self.radar_groupbox_16)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(15, 30, 44, 26))
        self.label_84.setFont(font2)
        self.label_85 = QLabel(self.radar_groupbox_16)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(15, 60, 44, 26))
        self.label_85.setFont(font2)
        self.label_86 = QLabel(self.radar_groupbox_16)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(15, 118, 44, 26))
        self.label_86.setFont(font2)
        self.label_87 = QLabel(self.radar_groupbox_16)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(15, 90, 44, 26))
        self.label_87.setFont(font2)
        self.label_88 = QLabel(self.radar_groupbox_16)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(146, 59, 44, 26))
        self.label_88.setFont(font2)
        self.label_89 = QLabel(self.radar_groupbox_16)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(146, 88, 44, 26))
        self.label_89.setFont(font2)
        self.label_90 = QLabel(self.radar_groupbox_16)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(146, 118, 44, 26))
        self.label_90.setFont(font2)
        self.label_91 = QLabel(self.radar_groupbox_16)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(146, 29, 44, 26))
        self.label_91.setFont(font2)
        self.lblAttRx = QLabel(self.radar_groupbox_16)
        self.lblAttRx.setObjectName(u"lblAttRx")
        self.lblAttRx.setGeometry(QRect(67, 158, 53, 26))
        self.lblAttRx.setFont(font2)
        self.trCTCL7 = QComboBox(self.radar_groupbox_16)
        self.trCTCL7.addItem("")
        self.trCTCL7.addItem("")
        self.trCTCL7.addItem("")
        self.trCTCL7.setObjectName(u"trCTCL7")
        self.trCTCL7.setGeometry(QRect(70, 120, 62, 22))
        self.trCTCL5 = QComboBox(self.radar_groupbox_16)
        self.trCTCL5.addItem("")
        self.trCTCL5.addItem("")
        self.trCTCL5.addItem("")
        self.trCTCL5.setObjectName(u"trCTCL5")
        self.trCTCL5.setGeometry(QRect(70, 90, 62, 22))
        self.trCTCL1 = QComboBox(self.radar_groupbox_16)
        self.trCTCL1.addItem("")
        self.trCTCL1.addItem("")
        self.trCTCL1.addItem("")
        self.trCTCL1.setObjectName(u"trCTCL1")
        self.trCTCL1.setGeometry(QRect(70, 30, 62, 22))
        self.trCTCL3 = QComboBox(self.radar_groupbox_16)
        self.trCTCL3.addItem("")
        self.trCTCL3.addItem("")
        self.trCTCL3.addItem("")
        self.trCTCL3.setObjectName(u"trCTCL3")
        self.trCTCL3.setGeometry(QRect(70, 60, 62, 22))
        self.trCTCL8 = QComboBox(self.radar_groupbox_16)
        self.trCTCL8.addItem("")
        self.trCTCL8.addItem("")
        self.trCTCL8.addItem("")
        self.trCTCL8.setObjectName(u"trCTCL8")
        self.trCTCL8.setGeometry(QRect(200, 120, 62, 22))
        self.trCTCL6 = QComboBox(self.radar_groupbox_16)
        self.trCTCL6.addItem("")
        self.trCTCL6.addItem("")
        self.trCTCL6.addItem("")
        self.trCTCL6.setObjectName(u"trCTCL6")
        self.trCTCL6.setGeometry(QRect(200, 90, 62, 22))
        self.trCTCL2 = QComboBox(self.radar_groupbox_16)
        self.trCTCL2.addItem("")
        self.trCTCL2.addItem("")
        self.trCTCL2.addItem("")
        self.trCTCL2.setObjectName(u"trCTCL2")
        self.trCTCL2.setGeometry(QRect(200, 30, 62, 22))
        self.trCTCL4 = QComboBox(self.radar_groupbox_16)
        self.trCTCL4.addItem("")
        self.trCTCL4.addItem("")
        self.trCTCL4.addItem("")
        self.trCTCL4.setObjectName(u"trCTCL4")
        self.trCTCL4.setGeometry(QRect(200, 60, 62, 22))
        self.trCTCLAll = QComboBox(self.radar_groupbox_16)
        self.trCTCLAll.addItem("")
        self.trCTCLAll.addItem("")
        self.trCTCLAll.addItem("")
        self.trCTCLAll.setObjectName(u"trCTCLAll")
        self.trCTCLAll.setGeometry(QRect(140, 160, 62, 22))
        self.radar_groupbox_31 = QGroupBox(self.groupBox_3)
        self.radar_groupbox_31.setObjectName(u"radar_groupbox_31")
        self.radar_groupbox_31.setGeometry(QRect(571, 21, 161, 200))
        self.radar_groupbox_31.setFont(font)
        self.radar_groupbox_31.setStyleSheet(u"QComboBox {\n"
"    color: white;\n"
"    background-color: #2a2f3b;\n"
"    border: 1px  #ccc;\n"
"    border-radius: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 1px;\n"
"    font-size: 12px;\n"
"}\n"
"/* Hover effect on closed combo box */\n"
"QComboBox:hover {\n"
"    background-color: #323741;\n"
"}\n"
"/* Drop-down arrow */\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"    subcontrol-origin: padding; \n"
"    subcontrol-position: top right;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/newPrefix/resources/arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Drop-down popup (list view) with dark theme */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2a2f3b;              /* dark background */\n"
"    color: white;                           /* white text */\n"
"    selection-background-color: #323741;    /* slightly lighter dark when selected */\n"
"    selection-color: white;\n"
"    border:"
                        " 1px solid #444;                 /* subtle dark border */\n"
"    padding: 5px;\n"
"    outline: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Vertical scrollbar inside combo popup */\n"
"QComboBox QAbstractItemView QScrollBar:vertical {\n"
"    background: #2a2f3b;           /* dark scrollbar track */\n"
"    width: 10px;\n"
"    margin: 2px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical {\n"
"    background: #555;              /* scrollbar handle */\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical:hover {\n"
"    background: #777;              /* lighter on hover */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::add-line:vertical,\n"
"QComboBox QAbstractItemView QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    height: 0px;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::add-page:vertical,\n"
"QComboBox QAbstrac"
                        "tItemView QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: orange;\n"
"color: black;\n"
"border: none;\n"
"height: 35px;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: darkorange;\n"
"}\n"
"\n"
"QLabel{\n"
"color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #333;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	image: url(:/newPrefix/resources/tickmark.png);\n"
"}\n"
"")
        self.label_189 = QLabel(self.radar_groupbox_31)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setGeometry(QRect(18, 65, 51, 26))
        self.label_189.setFont(font2)
        self.label_193 = QLabel(self.radar_groupbox_31)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setGeometry(QRect(18, 108, 51, 26))
        self.label_193.setFont(font2)
        self.label_194 = QLabel(self.radar_groupbox_31)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(15, 151, 61, 26))
        self.label_194.setFont(font2)
        self.label_197 = QLabel(self.radar_groupbox_31)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setGeometry(QRect(15, 25, 51, 26))
        self.label_197.setFont(font2)
        self.rblkCNTL = QComboBox(self.radar_groupbox_31)
        self.rblkCNTL.addItem("")
        self.rblkCNTL.addItem("")
        self.rblkCNTL.addItem("")
        self.rblkCNTL.addItem("")
        self.rblkCNTL.setObjectName(u"rblkCNTL")
        self.rblkCNTL.setGeometry(QRect(83, 67, 62, 22))
        self.biteCNTL = QComboBox(self.radar_groupbox_31)
        self.biteCNTL.addItem("")
        self.biteCNTL.addItem("")
        self.biteCNTL.addItem("")
        self.biteCNTL.addItem("")
        self.biteCNTL.setObjectName(u"biteCNTL")
        self.biteCNTL.setGeometry(QRect(83, 110, 62, 22))
        self.swlRCNTL = QComboBox(self.radar_groupbox_31)
        self.swlRCNTL.addItem("")
        self.swlRCNTL.addItem("")
        self.swlRCNTL.addItem("")
        self.swlRCNTL.addItem("")
        self.swlRCNTL.setObjectName(u"swlRCNTL")
        self.swlRCNTL.setGeometry(QRect(83, 153, 62, 22))
        self.lblkCNTL = QComboBox(self.radar_groupbox_31)
        self.lblkCNTL.addItem("")
        self.lblkCNTL.addItem("")
        self.lblkCNTL.addItem("")
        self.lblkCNTL.addItem("")
        self.lblkCNTL.setObjectName(u"lblkCNTL")
        self.lblkCNTL.setGeometry(QRect(83, 27, 62, 22))
        self.radar_groupbox_22 = QGroupBox(self.groupBox)
        self.radar_groupbox_22.setObjectName(u"radar_groupbox_22")
        self.radar_groupbox_22.setGeometry(QRect(10, 445, 861, 188))
        self.radar_groupbox_22.setFont(font)
        self.radar_groupbox_22.setStyleSheet(u"QComboBox {\n"
"    color: white;\n"
"    background-color: #2a2f3b;\n"
"    border-radius: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 25px;  /* reserve space for arrow */\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* Drop-down list (popup) */\n"
"QComboBox QAbstractItemView {\n"
"    background: transparent;             /* remove backside background */\n"
"    color: white;\n"
"    selection-background-color: #323741;\n"
"    selection-color: white;\n"
"    border: none;                        /* remove border */\n"
"    outline: 0;\n"
"    padding-left: 8px;                   /* add space from left */\n"
"    padding-right: 5px;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"/* Hover effect on closed combo box */\n"
"QComboBox:hover {\n"
"    background-color: #323741;\n"
"}\n"
"\n"
"/* Drop-down arrow area (right side) */\n"
"QComboBox::drop-down {\n"
"    border: none;                        /* no border */\n"
"    width: 25px;\n"
"    subcontrol-origin: padding;\n"
"    subco"
                        "ntrol-position: top right;\n"
"    background: transparent;             /* keep transparent */\n"
"}\n"
"\n"
"/* Arrow image */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/resources/arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Button styling */\n"
"QPushButton {\n"
"    background-color: orange;\n"
"    color: black;\n"
"    border: none;\n"
"    height: 35px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: darkorange;\n"
"}\n"
"\n"
"")
        self.radar_groupbox_23 = QGroupBox(self.radar_groupbox_22)
        self.radar_groupbox_23.setObjectName(u"radar_groupbox_23")
        self.radar_groupbox_23.setGeometry(QRect(10, 18, 251, 161))
        self.radar_groupbox_23.setFont(font)
        self.radar_groupbox_23.setStyleSheet(u"QComboBox {\n"
"    color: white;\n"
"    background-color: #2a2f3b;\n"
"    border-radius: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 25px;  /* reserve space for arrow */\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* Drop-down list (popup) */\n"
"QComboBox QAbstractItemView {\n"
"    background: transparent;             /* remove backside background */\n"
"    color: white;\n"
"    selection-background-color: #323741;\n"
"    selection-color: white;\n"
"    border: none;                        /* remove border */\n"
"    outline: 0;\n"
"    padding-left: 8px;                   /* add space from left */\n"
"    padding-right: 5px;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"/* Hover effect on closed combo box */\n"
"QComboBox:hover {\n"
"    background-color: #323741;\n"
"}\n"
"\n"
"/* Drop-down arrow area (right side) */\n"
"QComboBox::drop-down {\n"
"    border: none;                        /* no border */\n"
"    width: 25px;\n"
"    subcontrol-origin: padding;\n"
"    subco"
                        "ntrol-position: top right;\n"
"    background: transparent;             /* keep transparent */\n"
"}\n"
"\n"
"/* Arrow image */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/resources/arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Button styling */\n"
"QPushButton {\n"
"    background-color: orange;\n"
"    color: black;\n"
"    border: none;\n"
"    height: 35px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: darkorange;\n"
"}\n"
"\n"
"")
        self.label_129 = QLabel(self.radar_groupbox_23)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setGeometry(QRect(20, 55, 31, 26))
        self.label_129.setFont(font2)
        self.label_130 = QLabel(self.radar_groupbox_23)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setGeometry(QRect(20, 88, 31, 26))
        self.label_130.setFont(font2)
        self.label_131 = QLabel(self.radar_groupbox_23)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setGeometry(QRect(20, 21, 31, 26))
        self.label_131.setFont(font2)
        self.label_132 = QLabel(self.radar_groupbox_23)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setGeometry(QRect(20, 122, 31, 26))
        self.label_132.setFont(font2)
        self.fpLf3 = QLabel(self.radar_groupbox_23)
        self.fpLf3.setObjectName(u"fpLf3")
        self.fpLf3.setGeometry(QRect(80, 55, 25, 25))
        self.fpLf3.setFont(font2)
        self.fpLf3.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpLf3.setScaledContents(True)
        self.fpLf5 = QLabel(self.radar_groupbox_23)
        self.fpLf5.setObjectName(u"fpLf5")
        self.fpLf5.setGeometry(QRect(80, 88, 25, 25))
        self.fpLf5.setFont(font2)
        self.fpLf5.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpLf5.setScaledContents(True)
        self.fpLf1 = QLabel(self.radar_groupbox_23)
        self.fpLf1.setObjectName(u"fpLf1")
        self.fpLf1.setGeometry(QRect(80, 21, 25, 25))
        self.fpLf1.setFont(font2)
        self.fpLf1.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpLf1.setScaledContents(True)
        self.fpLf7 = QLabel(self.radar_groupbox_23)
        self.fpLf7.setObjectName(u"fpLf7")
        self.fpLf7.setGeometry(QRect(80, 122, 25, 25))
        self.fpLf7.setFont(font2)
        self.fpLf7.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpLf7.setScaledContents(True)
        self.fpLf8 = QLabel(self.radar_groupbox_23)
        self.fpLf8.setObjectName(u"fpLf8")
        self.fpLf8.setGeometry(QRect(200, 121, 25, 25))
        self.fpLf8.setFont(font2)
        self.fpLf8.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpLf8.setScaledContents(True)
        self.label_138 = QLabel(self.radar_groupbox_23)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setGeometry(QRect(140, 121, 31, 26))
        self.label_138.setFont(font2)
        self.fpLf4 = QLabel(self.radar_groupbox_23)
        self.fpLf4.setObjectName(u"fpLf4")
        self.fpLf4.setGeometry(QRect(200, 54, 25, 25))
        self.fpLf4.setFont(font2)
        self.fpLf4.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpLf4.setScaledContents(True)
        self.fpLf2 = QLabel(self.radar_groupbox_23)
        self.fpLf2.setObjectName(u"fpLf2")
        self.fpLf2.setGeometry(QRect(200, 20, 25, 25))
        self.fpLf2.setFont(font2)
        self.fpLf2.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpLf2.setScaledContents(True)
        self.label_141 = QLabel(self.radar_groupbox_23)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setGeometry(QRect(140, 87, 31, 26))
        self.label_141.setFont(font2)
        self.fpLf6 = QLabel(self.radar_groupbox_23)
        self.fpLf6.setObjectName(u"fpLf6")
        self.fpLf6.setGeometry(QRect(200, 87, 25, 25))
        self.fpLf6.setFont(font2)
        self.fpLf6.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpLf6.setScaledContents(True)
        self.label_143 = QLabel(self.radar_groupbox_23)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setGeometry(QRect(140, 20, 31, 26))
        self.label_143.setFont(font2)
        self.label_144 = QLabel(self.radar_groupbox_23)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setGeometry(QRect(140, 54, 31, 26))
        self.label_144.setFont(font2)
        self.radar_groupbox_26 = QGroupBox(self.radar_groupbox_22)
        self.radar_groupbox_26.setObjectName(u"radar_groupbox_26")
        self.radar_groupbox_26.setGeometry(QRect(530, 18, 321, 161))
        self.radar_groupbox_26.setFont(font)
        self.radar_groupbox_26.setStyleSheet(u"QComboBox {\n"
"    color: white;\n"
"    background-color: #2a2f3b;\n"
"    border-radius: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 25px;  /* reserve space for arrow */\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* Drop-down list (popup) */\n"
"QComboBox QAbstractItemView {\n"
"    background: transparent;             /* remove backside background */\n"
"    color: white;\n"
"    selection-background-color: #323741;\n"
"    selection-color: white;\n"
"    border: none;                        /* remove border */\n"
"    outline: 0;\n"
"    padding-left: 8px;                   /* add space from left */\n"
"    padding-right: 5px;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"/* Hover effect on closed combo box */\n"
"QComboBox:hover {\n"
"    background-color: #323741;\n"
"}\n"
"\n"
"/* Drop-down arrow area (right side) */\n"
"QComboBox::drop-down {\n"
"    border: none;                        /* no border */\n"
"    width: 25px;\n"
"    subcontrol-origin: padding;\n"
"    subco"
                        "ntrol-position: top right;\n"
"    background: transparent;             /* keep transparent */\n"
"}\n"
"\n"
"/* Arrow image */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/resources/arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Button styling */\n"
"QPushButton {\n"
"    background-color: orange;\n"
"    color: black;\n"
"    border: none;\n"
"    height: 35px;\n"
"    border-radius: 5px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: darkorange;\n"
"}\n"
"\n"
"")
        self.label_173 = QLabel(self.radar_groupbox_26)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setGeometry(QRect(25, 72, 81, 26))
        self.label_173.setFont(font2)
        self.label_173.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rightTemp1 = QLabel(self.radar_groupbox_26)
        self.rightTemp1.setObjectName(u"rightTemp1")
        self.rightTemp1.setGeometry(QRect(110, 72, 41, 26))
        self.rightTemp1.setFont(font2)
        self.leftTemp1 = QLabel(self.radar_groupbox_26)
        self.leftTemp1.setObjectName(u"leftTemp1")
        self.leftTemp1.setGeometry(QRect(110, 31, 41, 26))
        self.leftTemp1.setFont(font2)
        self.psTemp = QLabel(self.radar_groupbox_26)
        self.psTemp.setObjectName(u"psTemp")
        self.psTemp.setGeometry(QRect(110, 114, 41, 26))
        self.psTemp.setFont(font2)
        self.label_177 = QLabel(self.radar_groupbox_26)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setGeometry(QRect(25, 31, 71, 26))
        self.label_177.setFont(font2)
        self.label_177.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_178 = QLabel(self.radar_groupbox_26)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setGeometry(QRect(25, 114, 61, 26))
        self.label_178.setFont(font2)
        self.label_178.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_179 = QLabel(self.radar_groupbox_26)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setGeometry(QRect(170, 72, 81, 26))
        self.label_179.setFont(font2)
        self.label_179.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rightTemp2 = QLabel(self.radar_groupbox_26)
        self.rightTemp2.setObjectName(u"rightTemp2")
        self.rightTemp2.setGeometry(QRect(260, 72, 41, 26))
        self.rightTemp2.setFont(font2)
        self.leftTemp2 = QLabel(self.radar_groupbox_26)
        self.leftTemp2.setObjectName(u"leftTemp2")
        self.leftTemp2.setGeometry(QRect(260, 31, 41, 26))
        self.leftTemp2.setFont(font2)
        self.fpgaTemp = QLabel(self.radar_groupbox_26)
        self.fpgaTemp.setObjectName(u"fpgaTemp")
        self.fpgaTemp.setGeometry(QRect(260, 114, 41, 26))
        self.fpgaTemp.setFont(font2)
        self.label_183 = QLabel(self.radar_groupbox_26)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setGeometry(QRect(170, 31, 71, 26))
        self.label_183.setFont(font2)
        self.label_183.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_184 = QLabel(self.radar_groupbox_26)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setGeometry(QRect(170, 114, 81, 26))
        self.label_184.setFont(font2)
        self.label_184.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.radar_groupbox_24 = QGroupBox(self.radar_groupbox_22)
        self.radar_groupbox_24.setObjectName(u"radar_groupbox_24")
        self.radar_groupbox_24.setGeometry(QRect(270, 18, 251, 161))
        self.radar_groupbox_24.setFont(font)
        self.radar_groupbox_24.setStyleSheet(u"QComboBox {\n"
"    color: white;\n"
"    background-color: #2a2f3b;\n"
"    border-radius: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 25px;  /* reserve space for arrow */\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* Drop-down list (popup) */\n"
"QComboBox QAbstractItemView {\n"
"    background: transparent;             /* remove backside background */\n"
"    color: white;\n"
"    selection-background-color: #323741;\n"
"    selection-color: white;\n"
"    border: none;                        /* remove border */\n"
"    outline: 0;\n"
"    padding-left: 8px;                   /* add space from left */\n"
"    padding-right: 5px;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"/* Hover effect on closed combo box */\n"
"QComboBox:hover {\n"
"    background-color: #323741;\n"
"}\n"
"\n"
"/* Drop-down arrow area (right side) */\n"
"QComboBox::drop-down {\n"
"    border: none;                        /* no border */\n"
"    width: 25px;\n"
"    subcontrol-origin: padding;\n"
"    subco"
                        "ntrol-position: top right;\n"
"    background: transparent;             /* keep transparent */\n"
"}\n"
"\n"
"/* Arrow image */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/resources/arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Button styling */\n"
"QPushButton {\n"
"    background-color: orange;\n"
"    color: black;\n"
"    border: none;\n"
"    height: 35px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: darkorange;\n"
"}\n"
"\n"
"")
        self.fpRl3 = QLabel(self.radar_groupbox_24)
        self.fpRl3.setObjectName(u"fpRl3")
        self.fpRl3.setGeometry(QRect(80, 55, 25, 25))
        self.fpRl3.setFont(font2)
        self.fpRl3.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpRl3.setScaledContents(True)
        self.fpRl5 = QLabel(self.radar_groupbox_24)
        self.fpRl5.setObjectName(u"fpRl5")
        self.fpRl5.setGeometry(QRect(80, 88, 25, 25))
        self.fpRl5.setFont(font2)
        self.fpRl5.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpRl5.setScaledContents(True)
        self.fpRl1 = QLabel(self.radar_groupbox_24)
        self.fpRl1.setObjectName(u"fpRl1")
        self.fpRl1.setGeometry(QRect(80, 21, 25, 25))
        self.fpRl1.setFont(font2)
        self.fpRl1.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpRl1.setScaledContents(True)
        self.fpRl7 = QLabel(self.radar_groupbox_24)
        self.fpRl7.setObjectName(u"fpRl7")
        self.fpRl7.setGeometry(QRect(80, 122, 25, 25))
        self.fpRl7.setFont(font2)
        self.fpRl7.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpRl7.setScaledContents(True)
        self.fpRl8 = QLabel(self.radar_groupbox_24)
        self.fpRl8.setObjectName(u"fpRl8")
        self.fpRl8.setGeometry(QRect(200, 121, 25, 25))
        self.fpRl8.setFont(font2)
        self.fpRl8.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpRl8.setScaledContents(True)
        self.fpRl4 = QLabel(self.radar_groupbox_24)
        self.fpRl4.setObjectName(u"fpRl4")
        self.fpRl4.setGeometry(QRect(200, 54, 25, 25))
        self.fpRl4.setFont(font2)
        self.fpRl4.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpRl4.setScaledContents(True)
        self.fpRl2 = QLabel(self.radar_groupbox_24)
        self.fpRl2.setObjectName(u"fpRl2")
        self.fpRl2.setGeometry(QRect(200, 20, 25, 25))
        self.fpRl2.setFont(font2)
        self.fpRl2.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpRl2.setScaledContents(True)
        self.fpRl6 = QLabel(self.radar_groupbox_24)
        self.fpRl6.setObjectName(u"fpRl6")
        self.fpRl6.setGeometry(QRect(200, 87, 25, 25))
        self.fpRl6.setFont(font2)
        self.fpRl6.setPixmap(QPixmap(u":/newPrefix/resources/Off.png"))
        self.fpRl6.setScaledContents(True)
        self.label_145 = QLabel(self.radar_groupbox_24)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setGeometry(QRect(140, 120, 31, 26))
        self.label_145.setFont(font2)
        self.label_146 = QLabel(self.radar_groupbox_24)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setGeometry(QRect(140, 53, 31, 26))
        self.label_146.setFont(font2)
        self.label_147 = QLabel(self.radar_groupbox_24)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setGeometry(QRect(140, 19, 31, 26))
        self.label_147.setFont(font2)
        self.label_148 = QLabel(self.radar_groupbox_24)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setGeometry(QRect(140, 86, 31, 26))
        self.label_148.setFont(font2)
        self.label_154 = QLabel(self.radar_groupbox_24)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setGeometry(QRect(20, 54, 31, 26))
        self.label_154.setFont(font2)
        self.label_157 = QLabel(self.radar_groupbox_24)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setGeometry(QRect(20, 121, 31, 26))
        self.label_157.setFont(font2)
        self.label_159 = QLabel(self.radar_groupbox_24)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setGeometry(QRect(20, 87, 31, 26))
        self.label_159.setFont(font2)
        self.label_160 = QLabel(self.radar_groupbox_24)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setGeometry(QRect(20, 20, 31, 26))
        self.label_160.setFont(font2)
        self.radar_groupbox_25 = QGroupBox(self.groupBox)
        self.radar_groupbox_25.setObjectName(u"radar_groupbox_25")
        self.radar_groupbox_25.setGeometry(QRect(880, 380, 201, 253))
        self.radar_groupbox_25.setFont(font)
        self.radar_groupbox_25.setStyleSheet(u"QComboBox {\n"
"    color: white;\n"
"    background-color: #2a2f3b;\n"
"    border-radius: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 25px;  /* reserve space for arrow */\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* Drop-down list (popup) */\n"
"QComboBox QAbstractItemView {\n"
"    background: transparent;             /* remove backside background */\n"
"    color: white;\n"
"    selection-background-color: #323741;\n"
"    selection-color: white;\n"
"    border: none;                        /* remove border */\n"
"    outline: 0;\n"
"    padding-left: 8px;                   /* add space from left */\n"
"    padding-right: 5px;\n"
"    border-radius: 5px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"/* Hover effect on closed combo box */\n"
"QComboBox:hover {\n"
"    background-color: #323741;\n"
"}\n"
"\n"
"/* Drop-down arrow area (right side) */\n"
"QComboBox::drop-down {\n"
"    border: none;                        /* no border */\n"
"    width: 25px;\n"
"    subcontrol-origin: padding;\n"
"    subco"
                        "ntrol-position: top right;\n"
"    background: transparent;             /* keep transparent */\n"
"}\n"
"\n"
"/* Arrow image */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/resources/arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Button styling */\n"
"QPushButton {\n"
"    background-color: orange;\n"
"    color: black;\n"
"    border: none;\n"
"    height: 35px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: darkorange;\n"
"}\n"
"\n"
"")
        self.label_161 = QLabel(self.radar_groupbox_25)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setGeometry(QRect(31, 59, 61, 16))
        self.label_161.setFont(font2)
        self.label_161.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_165 = QLabel(self.radar_groupbox_25)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setGeometry(QRect(10, 25, 91, 21))
        self.label_165.setFont(font2)
        self.label_165.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_166 = QLabel(self.radar_groupbox_25)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setGeometry(QRect(31, 92, 61, 16))
        self.label_166.setFont(font2)
        self.label_166.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_167 = QLabel(self.radar_groupbox_25)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setGeometry(QRect(34, 160, 58, 16))
        self.label_167.setFont(font2)
        self.label_167.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_171 = QLabel(self.radar_groupbox_25)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setGeometry(QRect(34, 128, 58, 16))
        self.label_171.setFont(font2)
        self.label_171.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_172 = QLabel(self.radar_groupbox_25)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setGeometry(QRect(11, 192, 84, 16))
        self.label_172.setFont(font2)
        self.label_172.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v5Mon1 = QLabel(self.radar_groupbox_25)
        self.v5Mon1.setObjectName(u"v5Mon1")
        self.v5Mon1.setGeometry(QRect(130, 125, 61, 21))
        self.v5Mon1.setFont(font2)
        self.v5Mon2 = QLabel(self.radar_groupbox_25)
        self.v5Mon2.setObjectName(u"v5Mon2")
        self.v5Mon2.setGeometry(QRect(130, 158, 61, 21))
        self.v5Mon2.setFont(font2)
        self.v45Mon = QLabel(self.radar_groupbox_25)
        self.v45Mon.setObjectName(u"v45Mon")
        self.v45Mon.setGeometry(QRect(130, 189, 61, 21))
        self.v45Mon.setFont(font2)
        self.current = QLabel(self.radar_groupbox_25)
        self.current.setObjectName(u"current")
        self.current.setGeometry(QRect(130, 25, 61, 21))
        self.current.setFont(font2)
        self.v48M1 = QLabel(self.radar_groupbox_25)
        self.v48M1.setObjectName(u"v48M1")
        self.v48M1.setGeometry(QRect(130, 56, 61, 21))
        self.v48M1.setFont(font2)
        self.v48M2 = QLabel(self.radar_groupbox_25)
        self.v48M2.setObjectName(u"v48M2")
        self.v48M2.setGeometry(QRect(130, 89, 61, 21))
        self.v48M2.setFont(font2)
        self.label_174 = QLabel(self.radar_groupbox_25)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setGeometry(QRect(34, 224, 60, 16))
        self.label_174.setFont(font2)
        self.label_174.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v45Mon2 = QLabel(self.radar_groupbox_25)
        self.v45Mon2.setObjectName(u"v45Mon2")
        self.v45Mon2.setGeometry(QRect(130, 220, 61, 21))
        self.v45Mon2.setFont(font2)
        self.radar_groupbox_32 = QGroupBox(self.groupBox)
        self.radar_groupbox_32.setObjectName(u"radar_groupbox_32")
        self.radar_groupbox_32.setGeometry(QRect(760, 190, 321, 181))
        self.radar_groupbox_32.setFont(font)
        self.radar_groupbox_32.setStyleSheet(u"QComboBox {\n"
"    color: white;\n"
"    background-color: #2a2f3b;\n"
"    border: 1px  #ccc;\n"
"    border-radius: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 1px;\n"
"    font-size: 12px;\n"
"}\n"
"/* Hover effect on closed combo box */\n"
"QComboBox:hover {\n"
"    background-color: #323741;\n"
"}\n"
"/* Drop-down arrow */\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"    subcontrol-origin: padding; \n"
"    subcontrol-position: top right;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/newPrefix/resources/arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Drop-down popup (list view) with dark theme */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2a2f3b;              /* dark background */\n"
"    color: white;                           /* white text */\n"
"    selection-background-color: #323741;    /* slightly lighter dark when selected */\n"
"    selection-color: white;\n"
"    border:"
                        " 1px solid #444;                 /* subtle dark border */\n"
"    padding: 5px;\n"
"    outline: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Vertical scrollbar inside combo popup */\n"
"QComboBox QAbstractItemView QScrollBar:vertical {\n"
"    background: #2a2f3b;           /* dark scrollbar track */\n"
"    width: 10px;\n"
"    margin: 2px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical {\n"
"    background: #555;              /* scrollbar handle */\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical:hover {\n"
"    background: #777;              /* lighter on hover */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::add-line:vertical,\n"
"QComboBox QAbstractItemView QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    height: 0px;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::add-page:vertical,\n"
"QComboBox QAbstrac"
                        "tItemView QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: orange;\n"
"color: black;\n"
"border: none;\n"
"height: 35px;\n"
"border-radius: 5px;\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: darkorange;\n"
"}\n"
"\n"
"QLabel{\n"
"color: white;\n"
"}\n"
"QCheckBox {\n"
"     color: white;\n"	
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #333;\n"
"    color: white;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	image: url(:/newPrefix/resources/tickmark.png);\n"
"}\n"
"")
        self.chId = QComboBox(self.radar_groupbox_32)
        self.chId.addItem("")
        self.chId.addItem("")
        self.chId.addItem("")
        self.chId.addItem("")
        self.chId.addItem("")
        self.chId.addItem("")
        self.chId.addItem("")
        self.chId.addItem("")
        self.chId.addItem("")
        self.chId.addItem("")
        self.chId.setObjectName(u"chId")
        self.chId.setGeometry(QRect(150, 19, 77, 22))
        self.label_69 = QLabel(self.radar_groupbox_32)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(90, 20, 51, 21))
        font3 = QFont()
        font3.setPointSize(10)
        self.label_69.setFont(font3)
        self.label_69.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.leftPrt = QCheckBox(self.radar_groupbox_32)
        self.leftPrt.setObjectName(u"leftPrt")
        self.leftPrt.setGeometry(QRect(30, 62, 81, 20))
        self.righttPrt = QCheckBox(self.radar_groupbox_32)
        self.righttPrt.setObjectName(u"righttPrt")
        self.righttPrt.setGeometry(QRect(30, 101, 81, 20))
        self.btnRND = QPushButton(self.radar_groupbox_32)
        self.btnRND.setObjectName(u"btnRND")
        self.btnRND.setGeometry(QRect(120, 142, 91, 25))
        self.btnRND.setMaximumSize(QSize(16777215, 25))
        self.attTxCh = QComboBox(self.radar_groupbox_32)
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.addItem("")
        self.attTxCh.setObjectName(u"attTxCh")
        self.attTxCh.setGeometry(QRect(210, 61, 77, 22))
        self.label_83 = QLabel(self.radar_groupbox_32)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(160, 60, 31, 26))
        self.label_83.setFont(font2)
        self.label_111 = QLabel(self.radar_groupbox_32)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(150, 100, 41, 26))
        self.label_111.setFont(font2)
        self.label_111.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.phTxCh = QComboBox(self.radar_groupbox_32)
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.addItem("")
        self.phTxCh.setObjectName(u"phTxCh")
        self.phTxCh.setGeometry(QRect(210, 101, 77, 22))
        self.btnGetStatus = QPushButton(self.groupBox)
        self.btnGetStatus.setObjectName(u"btnGetStatus")
        self.btnGetStatus.setGeometry(QRect(976, 157, 101, 25))
        self.btnGetStatus.setMaximumSize(QSize(16777215, 25))
        font4 = QFont()
        self.btnGetStatus.setFont(font4)
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(758, 381, 114, 54))
        self.groupBox_4.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Segoe UI\";\n"
"}")
        self.ontime = QLabel(self.groupBox_4)
        self.ontime.setObjectName(u"ontime")
        self.ontime.setGeometry(QRect(9, 24, 95, 21))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        self.ontime.setFont(font5)
        self.ontime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_71 = QLabel(Form)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(20, 20, 80, 41))
        self.label_71.setFont(font1)
        self.label_71.setPixmap(QPixmap(u":/newPrefix/resources/amp-icon.png"))
        self.label_71.setScaledContents(True)
        self.label_72 = QLabel(Form)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(1020, 20, 75, 47))
        self.label_72.setFont(font1)
        self.label_72.setPixmap(QPixmap(u":/newPrefix/resources/falconx-icon.png"))
        self.label_72.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"TRMM CONTROLLER", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"TRMM CONTROLLER", None))
        self.groupBox.setTitle("")
        self.radar_groupbox_12.setTitle(QCoreApplication.translate("Form", u"COMMUNICTION", None))
        self.comPort.setItemText(0, QCoreApplication.translate("Form", u"COM1", None))
        self.comPort.setItemText(1, QCoreApplication.translate("Form", u"COM2", None))
        self.comPort.setItemText(2, QCoreApplication.translate("Form", u"COM3", None))

        self.comPort.setCurrentText(QCoreApplication.translate("Form", u"COM1", None))
        self.label_64.setText(QCoreApplication.translate("Form", u"Com Port", None))
        self.baudRate.setItemText(0, QCoreApplication.translate("Form", u"9600", None))
        self.baudRate.setItemText(1, QCoreApplication.translate("Form", u"14400", None))
        self.baudRate.setItemText(2, QCoreApplication.translate("Form", u"19200", None))
        self.baudRate.setItemText(3, QCoreApplication.translate("Form", u"38400", None))
        self.baudRate.setItemText(4, QCoreApplication.translate("Form", u"57600", None))
        self.baudRate.setItemText(5, QCoreApplication.translate("Form", u"115200", None))

        self.baudRate.setCurrentText(QCoreApplication.translate("Form", u"115200", None))
        self.label_70.setText(QCoreApplication.translate("Form", u"Baud Rate", None))
        self.connect.setText(QCoreApplication.translate("Form", u"Connect", None))
        self.groupBox_2.setTitle("")
        self.textbox.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10px;\"><br /></p></body></html>", None))
        self.btnClear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"CONTROLS", None))
        self.radar_groupbox_15.setTitle(QCoreApplication.translate("Form", u"BLK SWITCH", None))
        self.label_75.setText(QCoreApplication.translate("Form", u"BLK SW1", None))
        self.label_76.setText(QCoreApplication.translate("Form", u"BLK SW3", None))
        self.label_77.setText(QCoreApplication.translate("Form", u"BLK SW7", None))
        self.label_78.setText(QCoreApplication.translate("Form", u"BLK SW5", None))
        self.label_79.setText(QCoreApplication.translate("Form", u"BLK SW4", None))
        self.label_80.setText(QCoreApplication.translate("Form", u"BLK SW6", None))
        self.label_81.setText(QCoreApplication.translate("Form", u"BLK SW8", None))
        self.label_82.setText(QCoreApplication.translate("Form", u"BLK SW2", None))
        self.lblAttTx.setText(QCoreApplication.translate("Form", u"ALL SW'S", None))
        self.blkSw1.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.blkSw1.setItemText(1, QCoreApplication.translate("Form", u"1", None))

        self.blkSw3.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.blkSw3.setItemText(1, QCoreApplication.translate("Form", u"1", None))

        self.blkSw5.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.blkSw5.setItemText(1, QCoreApplication.translate("Form", u"1", None))

        self.blkSw7.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.blkSw7.setItemText(1, QCoreApplication.translate("Form", u"1", None))

        self.blkSw8.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.blkSw8.setItemText(1, QCoreApplication.translate("Form", u"1", None))

        self.blkSw4.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.blkSw4.setItemText(1, QCoreApplication.translate("Form", u"1", None))

        self.blkSw6.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.blkSw6.setItemText(1, QCoreApplication.translate("Form", u"1", None))

        self.blkSw2.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.blkSw2.setItemText(1, QCoreApplication.translate("Form", u"1", None))

        self.blkSwAll.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.blkSwAll.setItemText(1, QCoreApplication.translate("Form", u"1", None))

        self.radar_groupbox_16.setTitle(QCoreApplication.translate("Form", u"TR CTL", None))
        self.label_84.setText(QCoreApplication.translate("Form", u"TR CTL1", None))
        self.label_85.setText(QCoreApplication.translate("Form", u"TR CTL3", None))
        self.label_86.setText(QCoreApplication.translate("Form", u"TR CTL7", None))
        self.label_87.setText(QCoreApplication.translate("Form", u"TR CTL5", None))
        self.label_88.setText(QCoreApplication.translate("Form", u"TR CTL4", None))
        self.label_89.setText(QCoreApplication.translate("Form", u"TR CTL6", None))
        self.label_90.setText(QCoreApplication.translate("Form", u"TR CTL8", None))
        self.label_91.setText(QCoreApplication.translate("Form", u"TR CTL2", None))
        self.lblAttRx.setText(QCoreApplication.translate("Form", u"ALL CTL'S", None))
        self.trCTCL7.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.trCTCL7.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.trCTCL7.setItemText(2, QCoreApplication.translate("Form", u"PRT", None))

        self.trCTCL5.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.trCTCL5.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.trCTCL5.setItemText(2, QCoreApplication.translate("Form", u"PRT", None))

        self.trCTCL1.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.trCTCL1.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.trCTCL1.setItemText(2, QCoreApplication.translate("Form", u"PRT", None))

        self.trCTCL3.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.trCTCL3.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.trCTCL3.setItemText(2, QCoreApplication.translate("Form", u"PRT", None))

        self.trCTCL8.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.trCTCL8.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.trCTCL8.setItemText(2, QCoreApplication.translate("Form", u"PRT", None))

        self.trCTCL6.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.trCTCL6.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.trCTCL6.setItemText(2, QCoreApplication.translate("Form", u"PRT", None))

        self.trCTCL2.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.trCTCL2.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.trCTCL2.setItemText(2, QCoreApplication.translate("Form", u"PRT", None))

        self.trCTCL4.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.trCTCL4.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.trCTCL4.setItemText(2, QCoreApplication.translate("Form", u"PRT", None))

        self.trCTCLAll.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.trCTCLAll.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.trCTCLAll.setItemText(2, QCoreApplication.translate("Form", u"PRT", None))

        self.radar_groupbox_31.setTitle(QCoreApplication.translate("Form", u"CTLS", None))
        self.label_189.setText(QCoreApplication.translate("Form", u"RBLK CTL", None))
        self.label_193.setText(QCoreApplication.translate("Form", u"BITE CNT", None))
        self.label_194.setText(QCoreApplication.translate("Form", u"SWL RCTL", None))
        self.label_197.setText(QCoreApplication.translate("Form", u"LBLK CTL", None))
        self.rblkCNTL.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.rblkCNTL.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.rblkCNTL.setItemText(2, QCoreApplication.translate("Form", u"2", None))
        self.rblkCNTL.setItemText(3, QCoreApplication.translate("Form", u"3", None))

        self.biteCNTL.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.biteCNTL.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.biteCNTL.setItemText(2, QCoreApplication.translate("Form", u"2", None))
        self.biteCNTL.setItemText(3, QCoreApplication.translate("Form", u"3", None))

        self.swlRCNTL.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.swlRCNTL.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.swlRCNTL.setItemText(2, QCoreApplication.translate("Form", u"2", None))
        self.swlRCNTL.setItemText(3, QCoreApplication.translate("Form", u"3", None))

        self.lblkCNTL.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.lblkCNTL.setItemText(1, QCoreApplication.translate("Form", u"1", None))
        self.lblkCNTL.setItemText(2, QCoreApplication.translate("Form", u"2", None))
        self.lblkCNTL.setItemText(3, QCoreApplication.translate("Form", u"3", None))

        self.radar_groupbox_22.setTitle(QCoreApplication.translate("Form", u"HEALTH STATUS", None))
        self.radar_groupbox_23.setTitle(QCoreApplication.translate("Form", u"FORWARD POWER LEFT", None))
        self.label_129.setText(QCoreApplication.translate("Form", u"FP 3", None))
        self.label_130.setText(QCoreApplication.translate("Form", u"FP 5", None))
        self.label_131.setText(QCoreApplication.translate("Form", u"FP 1", None))
        self.label_132.setText(QCoreApplication.translate("Form", u"FP 7", None))
        self.fpLf3.setText("")
        self.fpLf5.setText("")
        self.fpLf1.setText("")
        self.fpLf7.setText("")
        self.fpLf8.setText("")
        self.label_138.setText(QCoreApplication.translate("Form", u"FP 8", None))
        self.fpLf4.setText("")
        self.fpLf2.setText("")
        self.label_141.setText(QCoreApplication.translate("Form", u"FP 6", None))
        self.fpLf6.setText("")
        self.label_143.setText(QCoreApplication.translate("Form", u"FP 2", None))
        self.label_144.setText(QCoreApplication.translate("Form", u"FP 4", None))
        self.radar_groupbox_26.setTitle(QCoreApplication.translate("Form", u"TEMPERATURES", None))
        self.label_173.setText(QCoreApplication.translate("Form", u"Temp 1 Right :", None))
        self.rightTemp1.setText(QCoreApplication.translate("Form", u".....", None))
        self.leftTemp1.setText(QCoreApplication.translate("Form", u".....", None))
        self.psTemp.setText(QCoreApplication.translate("Form", u".....", None))
        self.label_177.setText(QCoreApplication.translate("Form", u"Temp 1 Left :", None))
        self.label_178.setText(QCoreApplication.translate("Form", u"Temp 1 PS :", None))
        self.label_179.setText(QCoreApplication.translate("Form", u"Temp 2 Right :", None))
        self.rightTemp2.setText(QCoreApplication.translate("Form", u".....", None))
        self.leftTemp2.setText(QCoreApplication.translate("Form", u".....", None))
        self.fpgaTemp.setText(QCoreApplication.translate("Form", u".....", None))
        self.label_183.setText(QCoreApplication.translate("Form", u"Temp 2 Left :", None))
        self.label_184.setText(QCoreApplication.translate("Form", u"Temp 2 FPGA :", None))
        self.radar_groupbox_24.setTitle(QCoreApplication.translate("Form", u"FORWARD POWER RIGHT", None))
        self.fpRl3.setText("")
        self.fpRl5.setText("")
        self.fpRl1.setText("")
        self.fpRl7.setText("")
        self.fpRl8.setText("")
        self.fpRl4.setText("")
        self.fpRl2.setText("")
        self.fpRl6.setText("")
        self.label_145.setText(QCoreApplication.translate("Form", u"FP 8", None))
        self.label_146.setText(QCoreApplication.translate("Form", u"FP 4", None))
        self.label_147.setText(QCoreApplication.translate("Form", u"FP 2", None))
        self.label_148.setText(QCoreApplication.translate("Form", u"FP 6", None))
        self.label_154.setText(QCoreApplication.translate("Form", u"FP 3", None))
        self.label_157.setText(QCoreApplication.translate("Form", u"FP 7", None))
        self.label_159.setText(QCoreApplication.translate("Form", u"FP 5", None))
        self.label_160.setText(QCoreApplication.translate("Form", u"FP 1", None))
        self.radar_groupbox_25.setTitle(QCoreApplication.translate("Form", u"HEALTH MONITOR", None))
        self.label_161.setText(QCoreApplication.translate("Form", u"48V Mon1 :", None))
        self.label_165.setText(QCoreApplication.translate("Form", u"Input Cur Mon :", None))
        self.label_166.setText(QCoreApplication.translate("Form", u"48V Mon2 :", None))
        self.label_167.setText(QCoreApplication.translate("Form", u"5V Mon2 :", None))
        self.label_171.setText(QCoreApplication.translate("Form", u"5V Mon1 :", None))
        self.label_172.setText(QCoreApplication.translate("Form", u"Input Volt\u00a0Mon :", None))
        self.v5Mon1.setText(QCoreApplication.translate("Form", u".....", None))
        self.v5Mon2.setText(QCoreApplication.translate("Form", u".....", None))
        self.v45Mon.setText(QCoreApplication.translate("Form", u".....", None))
        self.current.setText(QCoreApplication.translate("Form", u".....", None))
        self.v48M1.setText(QCoreApplication.translate("Form", u".....", None))
        self.v48M2.setText(QCoreApplication.translate("Form", u".....", None))
        self.label_174.setText(QCoreApplication.translate("Form", u"45V Mon2 :", None))
        self.v45Mon2.setText(QCoreApplication.translate("Form", u".....", None))
        self.radar_groupbox_32.setTitle(QCoreApplication.translate("Form", u"CH CTLS", None))
        self.chId.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.chId.setItemText(1, QCoreApplication.translate("Form", u"2", None))
        self.chId.setItemText(2, QCoreApplication.translate("Form", u"3", None))
        self.chId.setItemText(3, QCoreApplication.translate("Form", u"4", None))
        self.chId.setItemText(4, QCoreApplication.translate("Form", u"5", None))
        self.chId.setItemText(5, QCoreApplication.translate("Form", u"6", None))
        self.chId.setItemText(6, QCoreApplication.translate("Form", u"7", None))
        self.chId.setItemText(7, QCoreApplication.translate("Form", u"8", None))
        self.chId.setItemText(8, QCoreApplication.translate("Form", u"ALL ON", None))
        self.chId.setItemText(9, QCoreApplication.translate("Form", u"ALL OFF", None))

        self.chId.setCurrentText(QCoreApplication.translate("Form", u"1", None))
        self.label_69.setText(QCoreApplication.translate("Form", u"CH ID", None))
        self.leftPrt.setText(QCoreApplication.translate("Form", u"LEFT PRT", None))
        self.righttPrt.setText(QCoreApplication.translate("Form", u"RIGHT PRT", None))
        self.btnRND.setText(QCoreApplication.translate("Form", u"Send", None))
        self.attTxCh.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.attTxCh.setItemText(1, QCoreApplication.translate("Form", u"0.5", None))
        self.attTxCh.setItemText(2, QCoreApplication.translate("Form", u"1", None))
        self.attTxCh.setItemText(3, QCoreApplication.translate("Form", u"1.5", None))
        self.attTxCh.setItemText(4, QCoreApplication.translate("Form", u"2", None))
        self.attTxCh.setItemText(5, QCoreApplication.translate("Form", u"2.5", None))
        self.attTxCh.setItemText(6, QCoreApplication.translate("Form", u"3", None))
        self.attTxCh.setItemText(7, QCoreApplication.translate("Form", u"3.5", None))
        self.attTxCh.setItemText(8, QCoreApplication.translate("Form", u"4", None))
        self.attTxCh.setItemText(9, QCoreApplication.translate("Form", u"4.5", None))
        self.attTxCh.setItemText(10, QCoreApplication.translate("Form", u"5", None))
        self.attTxCh.setItemText(11, QCoreApplication.translate("Form", u"5.5", None))
        self.attTxCh.setItemText(12, QCoreApplication.translate("Form", u"6", None))
        self.attTxCh.setItemText(13, QCoreApplication.translate("Form", u"6.5", None))
        self.attTxCh.setItemText(14, QCoreApplication.translate("Form", u"7", None))
        self.attTxCh.setItemText(15, QCoreApplication.translate("Form", u"7.5", None))
        self.attTxCh.setItemText(16, QCoreApplication.translate("Form", u"8", None))
        self.attTxCh.setItemText(17, QCoreApplication.translate("Form", u"8.5", None))
        self.attTxCh.setItemText(18, QCoreApplication.translate("Form", u"9", None))
        self.attTxCh.setItemText(19, QCoreApplication.translate("Form", u"9.5", None))
        self.attTxCh.setItemText(20, QCoreApplication.translate("Form", u"10", None))
        self.attTxCh.setItemText(21, QCoreApplication.translate("Form", u"10.5", None))
        self.attTxCh.setItemText(22, QCoreApplication.translate("Form", u"11", None))
        self.attTxCh.setItemText(23, QCoreApplication.translate("Form", u"11.5", None))
        self.attTxCh.setItemText(24, QCoreApplication.translate("Form", u"12", None))
        self.attTxCh.setItemText(25, QCoreApplication.translate("Form", u"12.5", None))
        self.attTxCh.setItemText(26, QCoreApplication.translate("Form", u"13", None))
        self.attTxCh.setItemText(27, QCoreApplication.translate("Form", u"13.5", None))
        self.attTxCh.setItemText(28, QCoreApplication.translate("Form", u"14", None))
        self.attTxCh.setItemText(29, QCoreApplication.translate("Form", u"14.5", None))
        self.attTxCh.setItemText(30, QCoreApplication.translate("Form", u"15", None))
        self.attTxCh.setItemText(31, QCoreApplication.translate("Form", u"15.5", None))
        self.attTxCh.setItemText(32, QCoreApplication.translate("Form", u"16", None))
        self.attTxCh.setItemText(33, QCoreApplication.translate("Form", u"16.5", None))
        self.attTxCh.setItemText(34, QCoreApplication.translate("Form", u"17", None))
        self.attTxCh.setItemText(35, QCoreApplication.translate("Form", u"17.5", None))
        self.attTxCh.setItemText(36, QCoreApplication.translate("Form", u"18", None))
        self.attTxCh.setItemText(37, QCoreApplication.translate("Form", u"18.5", None))
        self.attTxCh.setItemText(38, QCoreApplication.translate("Form", u"19", None))
        self.attTxCh.setItemText(39, QCoreApplication.translate("Form", u"19.5", None))
        self.attTxCh.setItemText(40, QCoreApplication.translate("Form", u"20", None))
        self.attTxCh.setItemText(41, QCoreApplication.translate("Form", u"20.5", None))
        self.attTxCh.setItemText(42, QCoreApplication.translate("Form", u"21", None))
        self.attTxCh.setItemText(43, QCoreApplication.translate("Form", u"21.5", None))
        self.attTxCh.setItemText(44, QCoreApplication.translate("Form", u"22", None))
        self.attTxCh.setItemText(45, QCoreApplication.translate("Form", u"22.5", None))
        self.attTxCh.setItemText(46, QCoreApplication.translate("Form", u"23", None))
        self.attTxCh.setItemText(47, QCoreApplication.translate("Form", u"23.5", None))
        self.attTxCh.setItemText(48, QCoreApplication.translate("Form", u"24", None))
        self.attTxCh.setItemText(49, QCoreApplication.translate("Form", u"24.5", None))
        self.attTxCh.setItemText(50, QCoreApplication.translate("Form", u"25", None))
        self.attTxCh.setItemText(51, QCoreApplication.translate("Form", u"25.5", None))
        self.attTxCh.setItemText(52, QCoreApplication.translate("Form", u"26", None))
        self.attTxCh.setItemText(53, QCoreApplication.translate("Form", u"26.5", None))
        self.attTxCh.setItemText(54, QCoreApplication.translate("Form", u"27", None))
        self.attTxCh.setItemText(55, QCoreApplication.translate("Form", u"27.5", None))
        self.attTxCh.setItemText(56, QCoreApplication.translate("Form", u"28", None))
        self.attTxCh.setItemText(57, QCoreApplication.translate("Form", u"28.5", None))
        self.attTxCh.setItemText(58, QCoreApplication.translate("Form", u"29", None))
        self.attTxCh.setItemText(59, QCoreApplication.translate("Form", u"29.5", None))
        self.attTxCh.setItemText(60, QCoreApplication.translate("Form", u"30", None))
        self.attTxCh.setItemText(61, QCoreApplication.translate("Form", u"30.5", None))
        self.attTxCh.setItemText(62, QCoreApplication.translate("Form", u"31", None))
        self.attTxCh.setItemText(63, QCoreApplication.translate("Form", u"31.5", None))

        self.attTxCh.setCurrentText(QCoreApplication.translate("Form", u"0", None))
        self.label_83.setText(QCoreApplication.translate("Form", u"ATTN", None))
        self.label_111.setText(QCoreApplication.translate("Form", u"PHASE", None))
        self.phTxCh.setItemText(0, QCoreApplication.translate("Form", u"0", None))
        self.phTxCh.setItemText(1, QCoreApplication.translate("Form", u"5.625", None))
        self.phTxCh.setItemText(2, QCoreApplication.translate("Form", u"11.25", None))
        self.phTxCh.setItemText(3, QCoreApplication.translate("Form", u"16.875", None))
        self.phTxCh.setItemText(4, QCoreApplication.translate("Form", u"22.5", None))
        self.phTxCh.setItemText(5, QCoreApplication.translate("Form", u"28.125", None))
        self.phTxCh.setItemText(6, QCoreApplication.translate("Form", u"33.75", None))
        self.phTxCh.setItemText(7, QCoreApplication.translate("Form", u"39.375", None))
        self.phTxCh.setItemText(8, QCoreApplication.translate("Form", u"45", None))
        self.phTxCh.setItemText(9, QCoreApplication.translate("Form", u"50.625", None))
        self.phTxCh.setItemText(10, QCoreApplication.translate("Form", u"56.25", None))
        self.phTxCh.setItemText(11, QCoreApplication.translate("Form", u"61.875", None))
        self.phTxCh.setItemText(12, QCoreApplication.translate("Form", u"67.5", None))
        self.phTxCh.setItemText(13, QCoreApplication.translate("Form", u"73.125", None))
        self.phTxCh.setItemText(14, QCoreApplication.translate("Form", u"78.75", None))
        self.phTxCh.setItemText(15, QCoreApplication.translate("Form", u"84.375", None))
        self.phTxCh.setItemText(16, QCoreApplication.translate("Form", u"90", None))
        self.phTxCh.setItemText(17, QCoreApplication.translate("Form", u"95.625", None))
        self.phTxCh.setItemText(18, QCoreApplication.translate("Form", u"101.25", None))
        self.phTxCh.setItemText(19, QCoreApplication.translate("Form", u"106.875", None))
        self.phTxCh.setItemText(20, QCoreApplication.translate("Form", u"112.5", None))
        self.phTxCh.setItemText(21, QCoreApplication.translate("Form", u"118.125", None))
        self.phTxCh.setItemText(22, QCoreApplication.translate("Form", u"123.75", None))
        self.phTxCh.setItemText(23, QCoreApplication.translate("Form", u"129.375", None))
        self.phTxCh.setItemText(24, QCoreApplication.translate("Form", u"135", None))
        self.phTxCh.setItemText(25, QCoreApplication.translate("Form", u"140.625", None))
        self.phTxCh.setItemText(26, QCoreApplication.translate("Form", u"146.25", None))
        self.phTxCh.setItemText(27, QCoreApplication.translate("Form", u"151.875", None))
        self.phTxCh.setItemText(28, QCoreApplication.translate("Form", u"157.5", None))
        self.phTxCh.setItemText(29, QCoreApplication.translate("Form", u"163.125", None))
        self.phTxCh.setItemText(30, QCoreApplication.translate("Form", u"168.75", None))
        self.phTxCh.setItemText(31, QCoreApplication.translate("Form", u"174.375", None))
        self.phTxCh.setItemText(32, QCoreApplication.translate("Form", u"180", None))
        self.phTxCh.setItemText(33, QCoreApplication.translate("Form", u"180.625", None))
        self.phTxCh.setItemText(34, QCoreApplication.translate("Form", u"191.25", None))
        self.phTxCh.setItemText(35, QCoreApplication.translate("Form", u"196.875", None))
        self.phTxCh.setItemText(36, QCoreApplication.translate("Form", u"202.5", None))
        self.phTxCh.setItemText(37, QCoreApplication.translate("Form", u"208.125", None))
        self.phTxCh.setItemText(38, QCoreApplication.translate("Form", u"213.75", None))
        self.phTxCh.setItemText(39, QCoreApplication.translate("Form", u"219.375", None))
        self.phTxCh.setItemText(40, QCoreApplication.translate("Form", u"225", None))
        self.phTxCh.setItemText(41, QCoreApplication.translate("Form", u"230.625", None))
        self.phTxCh.setItemText(42, QCoreApplication.translate("Form", u"236.25", None))
        self.phTxCh.setItemText(43, QCoreApplication.translate("Form", u"241.875", None))
        self.phTxCh.setItemText(44, QCoreApplication.translate("Form", u"247.5", None))
        self.phTxCh.setItemText(45, QCoreApplication.translate("Form", u"253.125", None))
        self.phTxCh.setItemText(46, QCoreApplication.translate("Form", u"258.75", None))
        self.phTxCh.setItemText(47, QCoreApplication.translate("Form", u"264.375", None))
        self.phTxCh.setItemText(48, QCoreApplication.translate("Form", u"270", None))
        self.phTxCh.setItemText(49, QCoreApplication.translate("Form", u"275.625", None))
        self.phTxCh.setItemText(50, QCoreApplication.translate("Form", u"281.25", None))
        self.phTxCh.setItemText(51, QCoreApplication.translate("Form", u"286.875", None))
        self.phTxCh.setItemText(52, QCoreApplication.translate("Form", u"292.5", None))
        self.phTxCh.setItemText(53, QCoreApplication.translate("Form", u"298.125", None))
        self.phTxCh.setItemText(54, QCoreApplication.translate("Form", u"303.75", None))
        self.phTxCh.setItemText(55, QCoreApplication.translate("Form", u"309.375", None))
        self.phTxCh.setItemText(56, QCoreApplication.translate("Form", u"315", None))
        self.phTxCh.setItemText(57, QCoreApplication.translate("Form", u"320.625", None))
        self.phTxCh.setItemText(58, QCoreApplication.translate("Form", u"326.25", None))
        self.phTxCh.setItemText(59, QCoreApplication.translate("Form", u"331.875", None))
        self.phTxCh.setItemText(60, QCoreApplication.translate("Form", u"337.5", None))
        self.phTxCh.setItemText(61, QCoreApplication.translate("Form", u"343.125", None))
        self.phTxCh.setItemText(62, QCoreApplication.translate("Form", u"348.75", None))
        self.phTxCh.setItemText(63, QCoreApplication.translate("Form", u"354.375", None))

        self.phTxCh.setCurrentText(QCoreApplication.translate("Form", u"0", None))
        self.btnGetStatus.setText(QCoreApplication.translate("Form", u"Get Status", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"ON TIME", None))
        self.ontime.setText(QCoreApplication.translate("Form", u"..........", None))
        self.label_71.setText("")
        self.label_72.setText("")
    # retranslateUi

