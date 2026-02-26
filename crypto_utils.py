from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password: str) -> bytes:
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_file(file_path: str, password: str):
    key = generate_key(password)
    fernet = Fernet(key)

    try:
        with open(file_path, "rb") as file:
            data = file.read()

        encrypted_data = fernet.encrypt(data)

        with open(file_path + ".enc", "wb") as file:
            file.write(encrypted_data)

        print("✅ Dosya başarıyla şifrelendi.")
        print("Oluşturulan dosya:", file_path + ".enc")

    except FileNotFoundError:
        print("❌ Dosya bulunamadı.")

def decrypt_file(file_path: str, password: str):
    key = generate_key(password)
    fernet = Fernet(key)

    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        output_file = "decrypted_" + file_path.replace(".enc", "")

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print("✅ Dosya başarıyla çözüldü.")
        print("Oluşturulan dosya:", output_file)

    except FileNotFoundError:
        print("❌ Dosya bulunamadı.")
    except:
        print("❌ Hatalı şifre veya bozuk dosya.")
        