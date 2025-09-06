from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import serial
import time
import serial.tools.list_ports
from datetime import datetime
import resources_rc


class SerialReader(QObject):
    data_received = Signal(bytes)
    error = Signal(str)

    def __init__(self, serial_port):
        super().__init__()
        self.serial_port = serial_port
        self._running = True

    def run(self):
        while self._running:
            try:
                if self.serial_port and self.serial_port.is_open and self.serial_port.in_waiting:
                    data = self.serial_port.read(self.serial_port.in_waiting)
                    if data:
                        self.data_received.emit(data)
                time.sleep(0.05)  # avoid busy loop
            except Exception as e:
                self.error.emit(str(e))
                break

    def stop(self):
        self._running = False

class Communication(QObject):
    data_received_signal = Signal(bytes)
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.serial_port = None
        self.reader_thread = None
        self.reader_worker = None

    def update_com_ports(self):
        self.ui.comPort.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.ui.comPort.addItem(port.device)
        QComboBox.showPopup(self.ui.comPort)

    def setConnection(self, com_port, baud_rate):
        try:
            if self.serial_port and self.serial_port.is_open:
                self.stop_reader()
                self.serial_port.close()
                print("Previous serial port closed.")

            self.serial_port = serial.Serial(port=com_port, baudrate=int(baud_rate), timeout=1)
            if self.serial_port.is_open:
                print("Serial port opened successfully")
                self.ui.connect.setText("Connected")
                self.ui.connect.setStyleSheet(
                    "QPushButton { background-color: green; color: black; border: none; height: 35px; border-radius: 5px; font-size: 16px; }"
                )
                QMessageBox.information(None, "Connection", f"Connected to {com_port} successfully!")
                self.ui.btnRND.setEnabled(True)   # Enable send button after connecting
                self.start_reader() 
            else:
                print("Failed to open serial port")
                self.ui.connect.setText("Connect")
                self.ui.connect.setStyleSheet(
                    "QPushButton { background-color: orange; color: black; border: none; height: 35px; border-radius: 5px; font-size: 16px; }"
                )
                QMessageBox.warning(None, "Connection", f"Failed to connect to {com_port}.")
                self.set_all_icons_off()
        except serial.SerialException as e:
            print(f"Serial error: {e}")
            self.ui.connect.setText("Connect")
            self.ui.connect.setStyleSheet(
                "QPushButton { background-color: orange; color: black; border: none; height: 35px; border-radius: 5px; font-size: 16px; }"
            )
            QMessageBox.warning(None, "Connection", f"Failed to connect to {com_port}.")
            self.set_all_icons_off()

    def toggleConnection(self, com_port, baud_rate):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            print("Serial port closed.")
            self.ui.connect.setText("Connect")
            self.ui.connect.setStyleSheet(
                "QPushButton { background-color: orange; color: black; border: none; height: 35px; border-radius: 5px; font-size: 16px; }"
            )
            QMessageBox.information(None, "Connection", f"Disconnected from {com_port}.")
            self.set_all_icons_off()
        else:
            self.setConnection(com_port, baud_rate)
    
    def start_reader(self):
        self.stop_reader()  # Ensure previous thread is stopped
        self.reader_thread = QThread()
        self.reader_worker = SerialReader(self.serial_port)
        self.reader_worker.moveToThread(self.reader_thread)
        self.reader_thread.started.connect(self.reader_worker.run)
        self.reader_worker.data_received.connect(self.on_data_received)
        self.reader_worker.error.connect(self.on_reader_error)
        self.reader_thread.start()

    def stop_reader(self):
        if self.reader_worker:
            self.reader_worker.stop()
        if self.reader_thread:
            self.reader_thread.quit()
            self.reader_thread.wait()
        self.reader_worker = None
        self.reader_thread = None

    def on_data_received(self, data):
        if data[0] == 0xAA and len(data) > 32: 
            self.consolePrint(data, length=len(data))
            self.data_received_signal.emit(data)
        else:
            print("Invalid data received", data)
            # QMessageBox.warning(None, "Error", f"Invalid data received.")

    # This method is now handled by the thread, but you can still call it manually if needed
    def receive_data(self, num_bytes=1024):
        if self.serial_port and self.serial_port.is_open:
            try:
                data = self.serial_port.read(num_bytes)
                print(f"Received data: {data}")
                return data
            except serial.SerialException as e:
                print(f"Error reading data: {e}")
                return None
        else:
            print("Serial port is not open")
            return None
        
    # Slot for reader errors
    def on_reader_error(self, error):
        print(f"Serial read error: {error}")
        # QMessageBox.warning(None, "Serial Error", error)
    
    def controlsRND(self):
        rblk_CTL = self.ui.rblkCTL.currentIndex()
        lblk_CTL = self.ui.lblkCTL.currentIndex()
        bite_CNT = self.ui.biteCNT.currentIndex()
        swlR_CTL = self.ui.swlRCTL.currentIndex()
        left_Prt = int(self.ui.leftPrt.isChecked())
        rightt_Prt = int(self.ui.righttPrt.isChecked())
        ch_Id = self.ui.chId.currentIndex() + 1  
        att = self.ui.attTxCh.currentIndex()
        phase = self.ui.phTxCh.currentIndex()

        # Pack 8 switch states into a single byte (bitwise)
        blk_sw = sum(self.ui.__getattribute__(f'blkSw{i}').currentIndex() << (i - 1) for i in range(1, 9))
        tr_ctcl = sum(self.ui.__getattribute__(f'trCTCL{i}').currentIndex() << (i - 1) for i in range(1, 9))

        bit_data_02 = (
            (swlR_CTL & 0b11) << 6 |
            (bite_CNT & 0b11) << 4 |
            (lblk_CTL & 0b11) << 2 |
            (rblk_CTL & 0b11)
        )

        bit_data_04 = (
            (rightt_Prt & 0b1111) << 4 |
            (left_Prt & 0b1111)
        )

        data = [ 0xAA, 0x00, ch_Id, 0x00, blk_sw, tr_ctcl, bit_data_02, bit_data_04, att, phase, 0xBB ]

        data_bytes = bytes(data)
        # print("Control data:", data_bytes.hex("-").upper())
        self.sendControl(data_bytes)

    def getStatus(self):
        data = [ 0x33, 0x01, 0x00, 0x00, 0x00, 0xBB ]
        # data = [0xAA, 0x01, 0x02, 0xBC, 0x0A, 0x23, 0x01, 0x56, 0x04, 0x89, 0x07, 0xF0, 0x00, 0xA2, 0x01, 0xB3, 0x02, 0xC4, 0x03, 0xD5, 0x04, 0xE6, 0x05, 0xF7, 0x06, 0xF8, 0x07, 0xF9, 0x08, 0x01, 0x00, 0x00, 0x00, 0xBB  ]

        data_bytes = bytes(data)
        self.sendControl(data_bytes)
      
    def get_bit_value(self, bit):
        byte_blk_Sw = 0
        for i, bit in enumerate(reversed(bit)):  # blkSw1 is LSB
            byte_blk_Sw |= (bit & 1) << i
            print(f"blkSw{i+1} = {bit}, byte_blk_Sw = {byte_blk_Sw:02X}")
        return byte_blk_Sw
    
    def set_all_icons_off(self):
        off_icon = QPixmap(u":/newPrefix/resources/Off.png")
        for label in [
            self.ui.fpLf1, self.ui.fpLf2, self.ui.fpLf3, self.ui.fpLf4,
            self.ui.fpLf5, self.ui.fpLf6, self.ui.fpLf7, self.ui.fpLf8,
            self.ui.fpRl1, self.ui.fpRl2, self.ui.fpRl3, self.ui.fpRl4,
            self.ui.fpRl5, self.ui.fpRl6, self.ui.fpRl7, self.ui.fpRl8,
        ]:
            label.setPixmap(off_icon)

        for label in [
            self.ui.leftTemp1, self.ui.rightTemp1, self.ui.leftTemp2,
            self.ui.rightTemp2, self.ui.psTemp, self.ui.fpgaTemp, self.ui.current,
            self.ui.v48M1, self.ui.v48M2, self.ui.v5Mon1, self.ui.v5Mon2, self.ui.v45Mon, self.ui.v45Mon2, self.ui.ontime
        ]:
            label.setText(".....")
        self.ui.textbox.clear()
    
    def handle_received_data(self, data):
        print(f"Processing received data: {data}")
        self._should_process = False

        fpRf = data[1]
        fpLf = data[2]
        tempLeft1 = data[3:5]
        tempRight1 = data[5:7]
        tempLeft2 = data[7:9]
        tempRight2 = data[9:11]
        tempPs = data[11:13]
        tempFPGA = data[13:15]
        current = data[15:17]
        v48Mon1 = data[17:19]
        v48Mon2 = data[19:21]
        v5Mon1 = data[21:23]
        v5Mon2 = data[23:25]
        v45Mon1 = data[25:27]
        v45Mon2 = data[27:29]
        onTime = data[29:33]

        self.updateField(tempLeft1, self.ui.leftTemp1)
        self.updateField(tempRight1, self.ui.rightTemp1)
        self.updateField(tempLeft2, self.ui.leftTemp2)
        self.updateField(tempRight2, self.ui.rightTemp2)
        self.updateField(tempPs, self.ui.psTemp)
        self.updateField(tempFPGA, self.ui.fpgaTemp)
        self.updateField(current, self.ui.current, suffix="A")
        self.updateField(v48Mon1, self.ui.v48M1, suffix="V")
        self.updateField(v48Mon2, self.ui.v48M2, suffix="V")
        self.updateField(v5Mon1, self.ui.v5Mon1, suffix="V")
        self.updateField(v5Mon2, self.ui.v5Mon2, suffix="V")
        self.updateField(v45Mon1, self.ui.v45Mon, suffix="V")
        self.updateField(v45Mon2, self.ui.v45Mon2, suffix="V")
        self.convertOnTime(onTime)
          
        self.updateIcons(fpRf, [
            self.ui.fpRl1, self.ui.fpRl2, self.ui.fpRl3, self.ui.fpRl4,
            self.ui.fpRl5, self.ui.fpRl6, self.ui.fpRl7, self.ui.fpRl8,
        ])
        self.updateIcons(fpLf, [
            self.ui.fpLf1, self.ui.fpLf2, self.ui.fpLf3, self.ui.fpLf4,
            self.ui.fpLf5, self.ui.fpLf6, self.ui.fpLf7, self.ui.fpLf8,
        ])
        
    def updateIcons(self, sys, labels):
        """ Updates multiple labels based on bit positions and prints the bit position. """
        for i, label in enumerate(labels):
            status = (sys >> i) & 1
            # print(f"Bit position {i}: {status}")
            self.update_status(label, status)

    def update_status(self, label, status):
        icon_path = u":/newPrefix/resources/Ok.png" if status else u":/newPrefix/resources/Error.png"
        pixmap = QPixmap(icon_path)
        if pixmap.isNull():
            print(f"Icon not found: {icon_path}")
        else:
            label.setPixmap(pixmap)

    def updateField(self, temps, label_field, suffix="°C"):
        first_byte = temps[0]                # 0xAB
        second_byte_4bits = temps[1] & 0x0F  # 0x3C & 0x0F = 0x0C

        combined = (first_byte << 4) | second_byte_4bits
        # self.ui.leftTemp1.setText(f"{combined:.2f}") # '2748.00'
        # self.ui.leftTemp1.setText(f"{combined / 100:.2f} °C") # '27.48'
        val = (combined * 5.0) / 4096.0
        label_field.setText(f"{val:.2f} {suffix}")

    def convertOnTime(self, packet_bytes):
        total_seconds = int.from_bytes(packet_bytes, "little") * 60
        days, remainder = divmod(total_seconds, 86400)   # 24*60*60
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.ui.ontime.setText(f"{days}d {hours}h {minutes}m")


    def sendControl(self, data):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.write(data)
            self.consolePrint(data)
            print("Control data sent ", data)
        else:
            print("Serial port is not open")
            QMessageBox.warning(None, "Error", "Serial port is not open.")

    def consolePrint(self, message, length=0):
        timestamp = datetime.now().strftime("%H:%M:%S")
        hex_message = message.hex("-").upper()
        sym = '<-'if length == 28 else '->'  
        formatted_message = f"{timestamp} {sym} {hex_message}"
        self.ui.textbox.append(formatted_message)