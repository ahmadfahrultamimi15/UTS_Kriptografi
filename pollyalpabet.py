# -*- coding: utf-8 -*-
"""pollyalpabet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o4QiqQG6jCHwWsxK41Dpz4FcoyoGE3Bn
"""

import random

def generate_random_alphabet():
    # Membuat alfabet acak
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(alphabet)
    return ''.join(alphabet)

def polyalphabetic_encrypt(plain_text, key):
    # Membuat tabel alfabet acak berdasarkan kunci
    key_alphabet = generate_random_alphabet()

    # Inisialisasi variabel untuk menyimpan teks terenkripsi
    encrypted_text = ""

    for char in plain_text:
        # Periksa apakah karakter merupakan huruf
        if char.isalpha():
            # Tentukan alfabet acak untuk karakter kunci
            key_char = key_alphabet[ord(key[0].upper()) - 65]

            # Enkripsi karakter
            if char.isupper():
                encrypted_text += chr((ord(char) + ord(key_char) - 130) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + ord(key_char) - 194) % 26 + 97)
        else:
            # Jika karakter bukan huruf, tambahkan ke teks terenkripsi tanpa perubahan
            encrypted_text += char

    return encrypted_text

# Input plain text
plain_text = input("Masukkan plain text untuk dienkripsi: ")
# Input kunci
key = input("Masukkan kunci: ")

# Enkripsi plain text
encrypted_text = polyalphabetic_encrypt(plain_text, key)

# Menampilkan hasil enkripsi
print("\nTeks Awal:", plain_text)
print("Kunci:", key)
print("Teks Terenkripsi:", encrypted_text)