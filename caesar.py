# -*- coding: utf-8 -*-
"""Caesar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OD-DBAGXCNxAk2R2cdprkuMLCS9HNX4O
"""

def caesar_cipher(text, key, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr(((ord(char) - shift + key * mode) % 26) + shift)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Pilih operasi (1: Enkripsi, 2: Dekripsi, 0: Keluar): ")

        if choice == "0":
            break

        if choice not in ("1", "2"):
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 0.")
            continue

        text = input("Masukkan teks: ")
        key = int(input("Masukkan kunci (angka pergeseran): "))

        if choice == "1":
            encrypted_text = caesar_cipher(text, key, 1)
            print(f"Teks terenkripsi: {encrypted_text}")
        elif choice == "2":
            decrypted_text = caesar_cipher(text, key, -1)
            print(f"Teks terdekripsi: {decrypted_text}")

if __name__ == "__main__":
    main()