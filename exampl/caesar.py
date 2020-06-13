import crypt

message = "This is secret message"
encrypt = crypt.caesar_encrypt(message, 3)
print(encrypt)
decrypt = crypt.caesar_decrypt(encrypt, 3)
print(decrypt)
