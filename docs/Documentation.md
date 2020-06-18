  # ciphers_collections documentation
  This is a official documentation of the **ciphers_collections** library in Python

  ## Step 1. Install and imoprt library
  1. Download crypt.py
  2. Create a new file
  3. Import the ciphers_collections library by writing `import crypt` in the new file
  4. Once this is done, use any of the following commands

 
  ## Step 2. Use Ciphers commands
### Caesar cipher  
**Doesn't encrypt symbols other than letters**  
- Encrypt message by caesar cipher  
`caesar_encrypt(message you want to encrypt, transition of letters (number) )`     

- Decrypt message by caesar cipher  
`caesar_decrypt(message you want to decrypt, transition of letters (number) )`   
### Rail fence cipher  
- Encrypt message by fence cipher  
`  fence_cipher_encrypt(message you want to encrypt, height of fence(number))`  

- Decrypt message by fence cipher  
`  fence_cipher_decrypt(message you want to decrypt, height of fence(number))` 

### Playfair cipher  
**If message is uneven it will append X in the end**  
**You can only use letters in message**  

- Encrypt message by playfair cipher  
`  playfair_encrypt(message you want to encrypt, key)`  

- Decrypt message by playfair cipher  
`  playfair_decrypt(message you want to decrypt, key)`  
### Bacon's cipher  
**You can only use letters in message**
- Encrypt message by bacon's cipher (26 letter version)  
`  bacon_encrypt(message you want to encrypt)`  

- Decrypt message by bacon's cipher  
`  bacon_decrypt(message you want to decrypt)`   

### Bifid cipher  
**You can only use letters in message**
- Encrypt message by bifid cipher  
`  bifid_encrypt(message you want to encrypt)`  

- Decrypt message by bifid cipher  
`  bifid_decrypt(message you want to decrypt)`  

### Vernam cipher  
**You can only use letters in message**  
**Key must be equal or longer than message (Spaces don't count)**
- Encrypt message by vernam cipher  
`  vernam_encrypt(message you want to encrypt, key)`  

- Decrypt message by vernam cipher  
`  vernam_decrypt(message you want to decrypt, key)` 

### Vigenere cipher  
**You can only use letters in message**
- Encrypt message by vigenere cipher  
`  vigenere_encrypt(message you want to encrypt, key)`  

- Decrypt message by vigenere cipher  
`  vigenere_decrypt(message you want to decrypt, key)` 
 
