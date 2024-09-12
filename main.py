import qrcode
import tkinter as tk
from tkinter import simpledialog


# Функция для создания QR-кода
def create_qr_code(phone_number):
    # Создаём QR-код с текстом (например, номер телефона)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(phone_number)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("phone_qr.png")


# Функция для запроса номера телефона
def ask_for_phone_number():
    ROOT = tk.Tk()
    ROOT.withdraw()  # Скрыть основное окно
    phone_number = simpledialog.askstring("Input", "Введите номер телефона:")
    if phone_number:
        create_qr_code(phone_number)
        print("QR-код создан и сохранён как 'phone_qr.png'.")


# Запуск запроса номера телефона
ask_for_phone_number()