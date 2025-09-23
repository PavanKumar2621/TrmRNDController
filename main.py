import sys
from PySide6.QtWidgets import *
from ui_trm_rnd_controller import TrmRNDController


if __name__ == "__main__":
    app = QApplication([])
    trmController = TrmRNDController()
    trmController.show()
    sys.exit(app.exec())


# # from PIL import Image

# # img = Image.open("IMG.png")
# # # Save as ICO with multiple sizes
# # img.save("IMG.ico", format="ICO", sizes=[(256, 256)]) 



# def convertOnTime( packet_bytes):
    
#     # packet_bytes: 6 bytes, use 6 bits from first 5, 2 bits from last
#     b0 = packet_bytes[0] & 0x3F
#     b1 = packet_bytes[1] & 0x3F
#     b2 = packet_bytes[2] & 0x3F
#     b3 = packet_bytes[3] & 0x3F
#     b4 = packet_bytes[4] & 0x3F
#     b5 = packet_bytes[5] & 0x03  # Only 2 bits from last byte

#     # Combine as little endian: b0 is lowest bits, b5 is highest
#     combined = (
#         (b5 << 30) |
#         (b4 << 24) |
#         (b3 << 18) |
#         (b2 << 12) |
#         (b1 << 6)  |
#         b0
#     )

#     total_seconds = combined * 60
#     days, remainder = divmod(total_seconds, 86400)
#     hours, remainder = divmod(remainder, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     return f"{days}d {hours}h {minutes}m"




# value =  27239 # total minutes

# b0 = (value >> 0)  & 0x3F
# b1 = (value >> 6)  & 0x3F
# b2 = (value >> 12) & 0x3F
# b3 = (value >> 18) & 0x3F
# b4 = (value >> 24) & 0x3F
# b5 = (value >> 30) & 0x03

# packet_bytes = bytes([b0, b1, b2, b3, b4, b5])
# print(", 0x".join(f"{b:02X}" for b in packet_bytes))  # filepath: c:\Users\HP\TrmRNDController\main.py
# print(convertOnTime( packet_bytes))  # Example usage    