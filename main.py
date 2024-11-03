from crypto_lib import encrypt, decrypt

# Definir la clave y el texto a encriptar
key = "PATO"
text_to_encrypt = "123.45ABCD"

# Encriptar
encrypted = encrypt(text_to_encrypt, key)
print("Texto encriptado:", encrypted)

# Desencriptar
decrypted = decrypt(encrypted, key)
print("Texto desencriptado:", decrypted)