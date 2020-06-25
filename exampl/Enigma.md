## ENIGMA - examples
### 1. Basic settings, no plugboard, classic ring setting  

```python
import crypt
message_to_encrypt = "This is secret message"  
key = "ENI"  
ring = "AAA"  
plug = ""  
setup = EnigmaSetup(1,2,3,2)  
encrypted_message = setup.enigma_cipher(message_to_encrypt, key, ring, plug)
print(encrypted_message)
```
Settings will be following:    
| Selected option | Meaning |    
| --- | --- |  
|1| ROTOR I in 1 position |  
|2| ROTOR II in 2 position |  
|3| ROTOR III in 3 position |   
|2| UKW-B Reflector |
|ENI| Key - rotors starting position |
|AAA| Rotors settings |
|""| No plugboard |

### 2. Other Enigma setup with plugboard

```python
import crypt
message_to_encrypt = "This is secret message"  
key = "QVR"  
ring = "MKL"  
plug = "BQ CR DI"  
setup = EnigmaSetup(5,6,1,3)  
encrypted_message = setup.enigma_cipher(message_to_encrypt, key, ring, plug)
print(encrypted_message)
```  
Settings will be following:    
| Selected option | Meaning |    
| --- | --- |  
|5| ROTOR V in 1 position |  
|6| ROTOR VI in 2 position |  
|1| ROTOR I in 3 position |   
|3| UKW-C Reflector |
|QVR| Key - rotors starting position |
|MKL| Rotors settings |
|BQ CR DI| B will be replaced with a Q and the letter Q with a B, and so on |

