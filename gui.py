import tkinter as tk
from tkinter import filedialog, messagebox
from crypto_utils import encrypt_file, decrypt_file

selected_file = ""

def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    file_label.config(text=selected_file)

def encrypt_action():
    if not selected_file:
        messagebox.showerror("Hata", "Lütfen dosya seçin.")
        return
    
    password = password_entry.get()
    if not password:
        messagebox.showerror("Hata", "Lütfen şifre girin.")
        return

    encrypt_file(selected_file, password)
    messagebox.showinfo("Başarılı", "Dosya şifrelendi.")

def decrypt_action():
    if not selected_file:
        messagebox.showerror("Hata", "Lütfen dosya seçin.")
        return
    
    password = password_entry.get()
    if not password:
        messagebox.showerror("Hata", "Lütfen şifre girin.")
        return

    decrypt_file(selected_file, password)
    messagebox.showinfo("Başarılı", "Dosya çözüldü.")

# Ana pencere
window = tk.Tk()
window.title("CipherFile - Dosya Şifreleme")
window.geometry("500x300")

title_label = tk.Label(window, text="CipherFile GUI", font=("Arial", 16))
title_label.pack(pady=10)

select_button = tk.Button(window, text="Dosya Seç", command=select_file)
select_button.pack(pady=5)

file_label = tk.Label(window, text="Henüz dosya seçilmedi", wraplength=400)
file_label.pack(pady=5)

password_label = tk.Label(window, text="Şifre:")
password_label.pack()

password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=5)

encrypt_button = tk.Button(window, text="Şifrele", command=encrypt_action)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(window, text="Çöz", command=decrypt_action)
decrypt_button.pack(pady=5)

window.mainloop()
