# -*- coding: utf-8 -*-
"""Hillchiper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v-8CUCokvELf9QcRv-iQmLC2CPTKBQX2
"""

import numpy as np

def text_to_matrix(text, n):
    # Konversi teks ke matriks huruf
    matrix = [ord(char) - ord('A') for char in text]
    # Menambahkan padding jika diperlukan
    while len(matrix) % n != 0:
        matrix.append(23)  # Huruf 'X' sebagai padding
    # Mengonversi matriks ke matriks n x n
    return np.array(matrix).reshape(-1, n)

def matrix_to_text(matrix):
    # Mengonversi matriks kembali ke teks
    return ''.join([chr(int(char) + ord('A')) for char in matrix.flatten()])

def encrypt(plain_text, key_matrix):
    n = len(key_matrix)
    plain_matrix = text_to_matrix(plain_text, n)
    # Mengenkripsi menggunakan kunci matriks
    encrypted_matrix = np.dot(plain_matrix, key_matrix) % 26
    # Mengonversi matriks hasil enkripsi ke teks
    encrypted_text = matrix_to_text(encrypted_matrix)
    return encrypted_text

def main():
    # Memasukkan teks dan kunci dari pengguna
    plain_text = input("Masukkan teks yang akan dienkripsi (huruf kapital): ")
    key = input("Masukkan kunci matriks (contoh: 1 2 3 4 untuk matriks 2x2): ")
    key_matrix = np.array(list(map(int, key.split()))).reshape(-1, len(key.split()))

    # Memastikan matriks kunci memiliki determinan yang tidak nol
    while np.linalg.det(key_matrix) == 0:
        print("Determinan matriks kunci tidak boleh nol. Silakan masukkan kunci lain.")
        key = input("Masukkan kunci matriks: ")
        key_matrix = np.array(list(map(int, key.split()))).reshape(-1, len(key.split()))

    # Mengenkripsi teks
    encrypted_text = encrypt(plain_text, key_matrix)
    print("Teks yang dienkripsi:", encrypted_text)

if __name__ == "__main__":
    main()