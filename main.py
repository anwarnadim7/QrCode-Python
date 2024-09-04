import qrcode
import os
import sys

# Data to be encoded
data = input("Please Enter Link to create QR Code : ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")

if sys.platform == "win32":
    # Windows
    os.startfile("qrcode.png")
elif sys.platform == "darwin":
    # macOS
    os.system("open qrcode.png")
else:
    # Linux or other
    os.system("xdg-open qrcode.png")