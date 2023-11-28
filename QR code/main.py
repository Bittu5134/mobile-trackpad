import qrcode
from PIL import Image

# Create the QR code
qr = qrcode.make("https://youtube.com/watch?v=dQw4w9WgXcQ")

# Resize the QR code without antialiasing
resized_qr = qr.resize((100, 50), Image.NEAREST)

# Convert the resized image to grayscale
resized_qr = resized_qr.convert("L")

# Convert the image to bytes
qr_bytes = resized_qr.tobytes()

# Map byte values to characters with ANSI color codes
new_qr = "".join("\033[97m█\033[0m" if i == 255 else "\033[30m█\033[0m" for i in qr_bytes)

index = 1

for i in qr_bytes:
    if i == 255:
        print("\033[97m█\033[0m", end="")
    else:
        print("\033[30m█\033[0m", end="")
    if index % 100 == 0:
        print()
    index += 1