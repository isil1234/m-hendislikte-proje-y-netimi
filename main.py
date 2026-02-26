from crypto_utils import encrypt_file, decrypt_file

def menu():
    print("\n===== CipherFile Dosya Şifreleme Uygulaması =====")
    print("1 - Dosya Şifrele")
    print("2 - Dosya Çöz")
    print("3 - Çıkış")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Seçiminizi girin: ")

        if choice == "1":
            file_path = input("Şifrelenecek dosya adı: ")
            password = input("Şifre: ")
            encrypt_file(file_path, password)

        elif choice == "2":
            file_path = input("Çözülecek dosya (.enc): ")
            password = input("Şifre: ")
            decrypt_file(file_path, password)

        elif choice == "3":
            print("Programdan çıkılıyor...")
            break

        else:
            print("❌ Geçersiz seçim.")