import qrcode

data = input("Enter the data to encode in the QR code: ")

QR = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

QR.add_data(data)
QR.make(fit=True)

img = QR.make_image(fill_color="white", back_color="blue")
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'.")
