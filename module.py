import qrcode

data = "https://maps.app.goo.gl/8u194Rvgn8UmDe9i7"

qr = qrcode.make(data)
qr.save("qrcode.png")

print("QR code generated successfully!")