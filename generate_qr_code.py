import qrcode

# URL вашей HTML-страницы
url = "http://localhost/form.html"  # Замените на URL, где будет размещена HTML-страница

# Создание QR-кода
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("data_input_qr.png")

print("QR-код создан и сохранён как 'data_input_qr.png'.")