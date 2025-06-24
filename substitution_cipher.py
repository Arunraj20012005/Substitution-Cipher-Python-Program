import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "

chars = list(chars)

key = chars.copy()

random.shuffle(key)

plain_text = input("Enter the plain text: ")
cipher_text = ""

for i in plain_text:
    index = chars.index(i)
    cipher_text += key[index]

print(f"Your plaintext is {plain_text}")

print(f"Your ciphertext is {cipher_text}")


cipher_text = input("Enter the cipher text: ")
plain_text = ""

for i in cipher_text:
    index = key.index(i)
    plain_text += chars[index]

print(f"Your ciphertext is {cipher_text}")

print(f"Your plaintext is {plain_text}")
