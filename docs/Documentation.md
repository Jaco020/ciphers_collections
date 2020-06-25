  # ciphers_collections documentation
  This is a official documentation of the **ciphers_collections** library in Python

  ## Step 1. Install and imoprt library
  1. Download crypt.py
  2. Create a new file
  3. Import the ciphers_collections library by writing `import crypt` in the new file
  4. Once this is done, use any of the following commands

 
  ## Step 2. Use Ciphers commands
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
### Caesar cipher  
**Doesn't encrypt symbols other than letters**  
- Encrypt message by caesar cipher  
`caesar_encrypt(message you want to encrypt, transition of letters (number) )`     

- Decrypt message by caesar cipher  
`caesar_decrypt(message you want to decrypt, transition of letters (number) )` 
 ### ENIGMA
To use enigma cipher, first you need is to set your own settings.  
`setup = EnigmaSetup(selected rotor, selected rotor, selected rotor, selected reflector)` 

See example [here](https://github.com/Jaco020/ciphers_collections/blob/master/exampl/Enigma.md)  

1. #### Rotor Settings  
    You need to select three of eight avaiable rotors
    
    |Rotor | Alphabet | Option number|  
    | --- | --- | --- |
    |I| EKMFLGDQVZNTOWYHXUSPAIBRCJ|   1|  
    |II| AJDKSIRUXBLHWTMCQGZNPYFVOE|    2|  
    |III| BDFHJLCPRTXVZNYEIWGAKMUSQO | 3|  
    |IV| ESOVPZJAYQUIRHXLNFTGKDCMWB    |	4|  
    |V| VZBRGITYUPSDNHLXAWMJQOFECK 	 |5|  
    |VI| JPGVOUMFYQBENHZRDKASXLICTW 	 |6|  
    |VII	|NZJHGRCXMYSWBOUFAIVLPEKQDT 	|7|    
    |VIII |FKQHTLXOCBJSPDZRAMEWNIUYGV  |8|  
2. #### Reflector Settings  
    You need to select one of three avaiable reflectors
    
    |Reflector | Alphabet | Option number|  
    | --- | --- | --- |
    |UKW-A| EKMFLGDQVZNTOWYHXUSPAIBRCJ|   1|  
    |UKW-B| AJDKSIRUXBLHWTMCQGZNPYFVOE|    2|  
    |UKW-C| BDFHJLCPRTXVZNYEIWGAKMUSQO | 3|  
    
3. #### Final Settings  
    If we choose this setup `setup = EnigmaSetup(2,4,3,2)`  
    Settings will be following:  
    | Selected Option | Meaining |    
    | --- | --- |  
    |2| ROTOR II in 1 position |  
    |4| ROTOR IV in 2 position |  
    |3| ROTOR III in 3 position |   
    |2| UKW-B Reflector |  
4. #### Encrypt and Decrypt message:
    The Enigma machine is a symmetric encryption machine.  
    Which means that it can be used to both encrypt or decrypt a message using the same settings  
    `setup = EnigmaSetup(2,4,3,2)`   
    `setup.enigma_cipher("Message to encrypt", "3 letter key", "Ring setting*", "Plugboard*")` 
    * Ring setting - e.g. - "BAA"
    * Pluboard - e.g. - "AW ER" If you don't want plugboard, leave it blank ("")
### Playfair cipher  
**If message is uneven it will append X in the end**  
**You can only use letters in message**  

- Encrypt message by playfair cipher  
`  playfair_encrypt(message you want to encrypt, key)`  

- Decrypt message by playfair cipher  
`  playfair_decrypt(message you want to decrypt, key)`  
### Rail fence cipher  
- Encrypt message by fence cipher  
`  fence_cipher_encrypt(message you want to encrypt, height of fence(number))`  

- Decrypt message by fence cipher  
`  fence_cipher_decrypt(message you want to decrypt, height of fence(number))` 
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
