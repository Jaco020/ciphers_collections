#  made by Jaco, for cryptography learning
import string
low_letters = string.ascii_lowercase
up_letters = string.ascii_uppercase
all_letters = up_letters + low_letters
all_symbols = string.printable + " " + "\n"


def check_message(message):
    """Check if message is correct - used by some cipher functions"""
    exceptions = [" ", "\n"]
    for check in message:
        if check not in all_letters and check not in exceptions:
            print("Error - One of argument contain symbols other than 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' letters")
            exit()


def check_key_nr(number):
    """Check if key number is correct - used by functions that require key number"""
    if not isinstance(number, int):
        print("Error - key is not int")  # check if kye is Correct
        exit()


def check_index(active_array, item):
    """Check row and column index of 2d array"""
    for c in range(5):
        for r in range(5):
            if active_array[c][r] == item:
                return [c, r]


def reverse_array(active_array):
    """Reverse 2d array - used by playfair"""
    r_array = [["_" for xrow in range(5)] for ycolumn in range(5)]
    for c in range(5):
        for r in range(5):
            r_array[c][r] = active_array[r][c]
    return r_array


def delete_spaces(text):
    """ deletes \n and mark spaces"""
    text = text.replace("\n", " ")
    space_list = [i for i, letter in enumerate(text) if letter == " "]
    text = text.replace(" ", "")
    return text, space_list


def caesar_encrypt(text_encrypt, key_number):
    """ Encrypt message by caesar cipher
    caesar_encrypt(message you want to encrypt, transition of letters (number) )
    Doesn't encrypt symbols other than letters
    """
    check_key_nr(key_number)
    if key_number > 26:
        print("Alphabet is only 26 in length")
        exit()
    from collections import deque
    message = []
    text_encrypt = text_encrypt.upper()
    d = deque(up_letters)  # letter list
    d.rotate(-key_number)
    for letter in text_encrypt:
        if letter not in up_letters:
            message.append(all_symbols[all_symbols.find(letter)])
        else:
            true_location = up_letters.find(letter)
            message.append(d[true_location])
    return ''.join(message)


def caesar_decrypt(text_encrypt, key_number):
    """ Decrypt message by caesar cipher
    caesar_decrypt(message you want to decrypt, transition of letters (number) )
    Doesn't encrypt symbols other than letters
    """
    check_key_nr(key_number)
    if key_number > 26:
        print("Alphabet is only 26 in length")
        exit()
    from collections import deque
    message = []
    text_encrypt = text_encrypt.upper()
    d = deque(up_letters)  # letter list
    d.rotate(key_number)
    for letter in text_encrypt:
        if letter not in up_letters:
            message.append(all_symbols[all_symbols.find(letter)])
        else:
            true_location = up_letters.find(letter)
            message.append(d[true_location])
    return ''.join(message)


def fence_cipher_encrypt(text_encrypt, key_number):
    """ Encrypt message by fence cipher
    fence_cipher_encrypt(message you want to encrypt, height of fence(number))"""
    check_key_nr(key_number)

    message = []
    operation_nr, direction_nr, index = 0, 1, 0  # index is for text_encrypt
    text_length = len(text_encrypt)
    fence_array = [["_" for xrow in range(text_length)] for ycolumn in range(key_number)]  # generate array
    for x in range(text_length):  # x width
        fence_array[operation_nr][x] = text_encrypt[index]  # creating fence
        operation_nr += direction_nr
        index += 1

        if operation_nr == key_number - 1:
            direction_nr = -1
        if operation_nr == 0:  # determine to go down or up
            direction_nr = 1
    for row in fence_array:
        for column in row:
            if column != "_":
                message.append(column)
    return ''.join(message)


def fence_cipher_decrypt(text_encrypt, key_number):
    """ Decrypt message by fence cipher
    fence_cipher_decrypt(message you want to decrypt, height of fence(number))"""
    check_key_nr(key_number)

    message = []
    operation_nr, direction_nr = 0, 1
    text_length = len(text_encrypt)
    fence_array = [["_" for xrow in range(text_length)] for ycolumn in range(key_number)]  # generate array
#  ==================================================================================================
    for x in range(text_length):                                        # x width
        fence_array[operation_nr][x] = "*"                        # creating fence
        operation_nr += direction_nr

        if operation_nr == key_number-1:
            direction_nr = -1
        if operation_nr == 0:                                            # determine to go down or up
            direction_nr = 1
#  ==================================================================================================
    operation_nr = 0
    for i in range(key_number):
        for j in range(text_length):
            if fence_array[i][j] == '*':
                fence_array[i][j] = text_encrypt[operation_nr]                     # add letters to fence
                operation_nr += 1
#  ==================================================================================================
    operation_nr, direction_nr = 0, 1
    for x in range(text_length):
        message.append(fence_array[operation_nr][x])                       # reading a message in Zig-Zag
        operation_nr += direction_nr

        if operation_nr == key_number-1:
            direction_nr = -1
        if operation_nr == 0:
            direction_nr = 1

    return ''.join(message)


def playfair_encrypt(text_encrypt, key):
    """ Encrypt message by playfair cipher
    playfair_encrypt(message you want to encrypt, key)
    """
    check_message(text_encrypt)
    text_encrypt, space_cords = delete_spaces(text_encrypt)
    for check in key:
        if 1 < key.count(check):
            print("Wrong key - same letter can't occurs 2 times")  # check if key is Correct
            exit()
        elif check not in all_letters:
            print("Error - Key can only contain 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' letters")  # check if key is Correct
            exit()

    if int(len(text_encrypt)) % 2 != 0:
        text_encrypt = text_encrypt + "X"
    text_encrypt = text_encrypt.upper()
    key = key.upper()
    text_encrypt = text_encrypt.replace("J", "I")
    message = []
    correct_letters = []
    operation_nr = 0
    check_situation = False

    def mark_next_letter(active_array):
        """Mark the correct letter for fist and second situation - used by playfair"""
        letter_1 = check_index(active_array, text_encrypt[pair])[1]
        letter_2 = check_index(active_array, text_encrypt[pair + 1])[1]  # checks column position of pair
        if letter_1 == 4:
            letter_1 = -1
        if letter_2 == 4:
            letter_2 = -1
        message.append(active_array[y][letter_1 + 1])
        message.append(active_array[y][letter_2 + 1])

    for letter in key:
        correct_letters.append(letter)
    for letter in up_letters:  # proper list of letters and key
        if letter not in correct_letters and letter != "J":
            correct_letters.append(letter)

    array = [["_" for xrow in range(5)] for ycolumn in range(5)]
    for rindex in range(5):
        for cindex in range(5):  # creates 2d array
            array[rindex][cindex] = correct_letters[operation_nr]
            operation_nr += 1
    rev_array = reverse_array(array)
    for pair in range(0, len(text_encrypt), 2):  # check every pair of text
        for y in range(5):
            if text_encrypt[pair] in array[y] and text_encrypt[pair + 1] in array[y]:
                # ===== first situation ===== #
                mark_next_letter(array)
                check_situation = True
                break
            elif text_encrypt[pair] in rev_array[y] and text_encrypt[pair + 1] in rev_array[y] and not check_situation:
                # ===== second situation ===== #
                mark_next_letter(rev_array)
                check_situation = True
                break
            else:
                check_situation = False

        # ===== third situation ===== #
        if not check_situation:
            x1 = check_index(array, text_encrypt[pair])
            x2 = check_index(array, text_encrypt[pair + 1])
            message.append(array[x1[0]][x2[1]])
            message.append(array[x2[0]][x1[1]])

    for space in space_cords:
        message.insert(space, " ")
    return ''.join(message)


def playfair_decrypt(text_encrypt, key):
    """ Decrypt message by playfair cipher
    playfair_decrypt(message you want to decrypt, key)
    You can only use letters in message
    """
    check_message(text_encrypt)
    text_encrypt, space_cords = delete_spaces(text_encrypt)
    for check in key:
        if 1 < key.count(check):
            print("Wrong key - same letter can't occurs 2 times")  # check if key is Correct
            exit()
        elif check not in all_letters:
            print("Error - Key can only contain 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' letters")  # check if key is Correct
            exit()
    if int(len(text_encrypt)) % 2 != 0:
        text_encrypt = text_encrypt + "X"
    text_encrypt = text_encrypt.upper()
    key = key.upper()
    text_encrypt = text_encrypt.replace("J", "I")
    message = []
    correct_letters = []
    operation_nr = 0
    check_situation = False

    def mark_next_letter(active_array):
        """Mark the correct letter for fist and second situation - used by playfair"""
        letter_1 = check_index(active_array, text_encrypt[pair])[1]
        letter_2 = check_index(active_array, text_encrypt[pair + 1])[1]  # checks column position of pair
        if letter_1 == 0:
            letter_1 = 5
        if letter_2 == 0:
            letter_2 = 5
        message.append(active_array[y][letter_1 - 1])
        message.append(active_array[y][letter_2 - 1])

    for letter in key:
        correct_letters.append(letter)
    for letter in up_letters:  # proper list of letters and key
        if letter not in correct_letters and letter != "J":
            correct_letters.append(letter)

    array = [["_" for xrow in range(5)] for ycolumn in range(5)]
    for rindex in range(5):
        for cindex in range(5):  # creates 2d array
            array[rindex][cindex] = correct_letters[operation_nr]
            operation_nr += 1

    rev_array = reverse_array(array)
    for pair in range(0, len(text_encrypt), 2):  # check every pair of text
        for y in range(5):
            if text_encrypt[pair] in array[y] and text_encrypt[pair + 1] in array[y]:
                # ===== first situation ===== #
                mark_next_letter(array)
                check_situation = True
                break
            elif text_encrypt[pair] in rev_array[y] and text_encrypt[pair + 1] in rev_array[y] and not check_situation:
                # ===== second situation ===== #
                mark_next_letter(rev_array)
                check_situation = True
                break
            else:
                check_situation = False

        # ===== third situation ===== #
        if not check_situation:
            x1 = check_index(array, text_encrypt[pair])
            x2 = check_index(array, text_encrypt[pair + 1])
            message.append(array[x1[0]][x2[1]])
            message.append(array[x2[0]][x1[1]])
    for space in space_cords:
        message.insert(space, " ")
    return ''.join(message)


def bacon_encrypt(text_encrypt):
    """ Encrypt message by bacon's cipher (26 letter version)
    bacon_encrypt(message you want to encrypt)
    You can only use letters in message
    """
    check_message(text_encrypt)
    text_encrypt = text_encrypt.upper()
    message = []
    layout = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa', 'F': 'aabab', 'G': 'aabba',
              'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab', 'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab',
              'O': 'abbba', 'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb', 'U': 'babaa',
              'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}
    for letter in text_encrypt:
        if letter in layout:
            message.append(layout[letter])
        else:
            message.append(letter)
    return ''.join(message)


def bacon_decrypt(text_encrypt):
    """ Decrypt message by bacon's cipher (26 letter version)
        bacon_decrypt(message you want to decrypt)
        You can only use letters in message
        """
    check_message(text_encrypt)
    text_encrypt = text_encrypt.lower()

    message = []
    temporary_text = ""
    divide_text_encrypt = []
    layout = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa', 'F': 'aabab', 'G': 'aabba',
              'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab', 'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab',
              'O': 'abbba', 'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb', 'U': 'babaa',
              'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}
    for word in text_encrypt.split(" "):
        for count, item in enumerate(word, 1):
            temporary_text += item
            if count % 5 == 0:
                divide_text_encrypt.append(temporary_text)
                temporary_text = ""
        divide_text_encrypt.append(" ")
    for letter in divide_text_encrypt:
        for key_letter, value in layout.items():
            if value == letter:
                message.append(key_letter)
                break
        if letter == " ":
            message.append(" ")
    return ''.join(message)


def bifid_encrypt(text_encrypt):
    """ Encrypt message by bifid cipher
        bifid_encrypt(message you want to encrypt)
        You can only use letters in message
        """
    check_message(text_encrypt)
    text_encrypt = text_encrypt.upper()
    text_encrypt = text_encrypt.replace("J", "")
    up_letters_list = up_letters.replace("J", "")
    text_encrypt, space_list = delete_spaces(text_encrypt)

    message = []
    position_list = []
    temporary_list = []
    array = [[0 for xrow in range(5)] for ycolumn in range(5)]
    operation_nr = 0

    for column in range(5):
        for row in range(5):
            array[column][row] = up_letters_list[operation_nr]
            operation_nr += 1
    for letter in text_encrypt:
        position = check_index(array, letter)
        position_list.append(position[0])
        temporary_list.append(position[1])
    position_list = position_list + temporary_list

    for position in range(0, len(position_list), 2):
        encrypted_letter = array[position_list[position]][position_list[position+1]]  # second step in bifid cipher
        message.append(encrypted_letter)
    for space in space_list:
        message.insert(space, " ")
    return ''.join(message)


def bifid_decrypt(text_encrypt):
    """ Decrypt message by bifid cipher
        bifid_decrypt(message you want to decrypt)
        You can only use letters in message
        """
    check_message(text_encrypt)
    text_encrypt = text_encrypt.upper()
    text_encrypt = text_encrypt.replace("J", "")
    up_letters_list = up_letters.replace("J", "")
    text_encrypt, space_list = delete_spaces(text_encrypt)

    message = []
    position_list = []
    array = [[0 for xrow in range(5)] for ycolumn in range(5)]
    operation_nr = 0

    for column in range(5):
        for row in range(5):
            array[column][row] = up_letters_list[operation_nr]
            operation_nr += 1
    for letter in text_encrypt:
        position = check_index(array, letter)
        position_list.append(position[0])
        position_list.append(position[1])

    for position in range(len(text_encrypt)):
        encrypted_letter = array[position_list[position]][position_list[position + len(text_encrypt)]]  # second step in bifid cipher
        message.append(encrypted_letter)
    for space in space_list:
        message.insert(space, " ")
    return ''.join(message)


def vernam_encrypt(text_encrypt, key):
    """ Encrypt message by vernam cipher
        vernam_encrypt(message you want to encrypt, key word)
        You can only use letters in message
        Key must be equal or longer than message (Spaces don't count)
        """
    check_message(text_encrypt)
    check_message(key)
    text_encrypt, space_cords = delete_spaces(text_encrypt)
    key, key_space_cords = delete_spaces(key)
    if len(key) <= len(text_encrypt):
        print("Key must be equal or longer than message (Spaces don't count)")
        exit()
    text_encrypt = text_encrypt.upper()
    key = key.upper()
    message = []
    text_encrypt_cords = []
    key_cords = []
    for letter in range(len(text_encrypt)):
        text_encrypt_cords.append(up_letters.find(text_encrypt[letter]))
        key_cords.append(up_letters.find(key[letter]))
    for index in range(len(text_encrypt)):
        cord1 = text_encrypt_cords[index]
        cord2 = key_cords[index]
        total = cord1 + cord2
        if total > 25:
            if cord1 > cord2:
                difference = 25 - cord1
                total = -1 + (cord2 - difference)
            else:
                difference = 25 - cord2
                total = -1 + (cord1 - difference)
        message.append(up_letters[total])
    for space in space_cords:
        message.insert(space, " ")
    return ''.join(message)


def vernam_decrypt(text_encrypt, key):
    """ Decrypt message by vernam cipher
        vernam_decrypt(message you want to decrypt, key word)
        You can only use letters in message
        Key must be equal or longer than message (Spaces don't count)
        """
    check_message(text_encrypt)
    check_message(key)
    text_encrypt, space_cords = delete_spaces(text_encrypt)
    key, key_space_cords = delete_spaces(key)
    if len(key) <= len(text_encrypt):
        print("Key must be equal or longer than message (Spaces don't count)")
        exit()
    text_encrypt = text_encrypt.upper()
    key = key.upper()
    message = []
    text_encrypt_cords = []
    key_cords = []
    for letter in range(len(text_encrypt)):
        text_encrypt_cords.append(up_letters.find(text_encrypt[letter]))
        key_cords.append(up_letters.find(key[letter]))
    for index in range(len(text_encrypt)):
        cord1 = text_encrypt_cords[index]
        cord2 = key_cords[index]
        total = cord1 - cord2
        message.append(up_letters[total])
    for space in space_cords:
        message.insert(space, " ")
    return ''.join(message)


def vigenere_encrypt(text_encrypt, key):
    """ Encrypt message by vigenere cipher
        vigenere_encrypt(message you want to encrypt, key word)
        You can only use letters in message
        """
    check_message(text_encrypt)
    check_message(key)
    text_encrypt, space_cords = delete_spaces(text_encrypt)
    key, key_space_cords = delete_spaces(key)
    text_encrypt = text_encrypt.upper()
    key = key.upper()

    from collections import deque
    key_index = 0
    while len(key) <= len(text_encrypt):
        key += key[key_index]
        key_index += 1
        if key_index == len(key):
            key_index = 0

    d = deque(up_letters)  # letter list
    array = [["_" for xrow in range(26)] for ycolumn in range(26)]
    rotate_nr = -1
    message = []
    text_encrypt_cords = []
    key_cords = []
    for ycolumn in range(26):
        for xrow in range(26):
            array[ycolumn][xrow] = d[xrow]
        d.rotate(rotate_nr)
    for letter in range(len(text_encrypt)):
        text_encrypt_cords.append(up_letters.find(text_encrypt[letter]))
        key_cords.append(up_letters.find(key[letter]))

    for cord, letter in enumerate(text_encrypt):
        message.append(array[text_encrypt_cords[cord]][key_cords[cord]])
    for space in space_cords:
        message.insert(space, " ")
    return ''.join(message)


def vigenere_decrypt(text_encrypt, key):
    """ Decrypt message by vigenere cipher
        vigenere_decrypt(message you want to decrypt, key word)
        You can only use letters in message
        """
    check_message(text_encrypt)
    check_message(key)
    text_encrypt, space_cords = delete_spaces(text_encrypt)
    key, key_space_cords = delete_spaces(key)
    text_encrypt = text_encrypt.upper()
    key = key.upper()

    from collections import deque
    key_index = 0
    while len(key) <= len(text_encrypt):
        key += key[key_index]
        key_index += 1
        if key_index == len(key):
            key_index = 0

    d = deque(up_letters)  # letter list
    array = [["_" for xrow in range(26)] for ycolumn in range(26)]
    rotate_nr = -1
    message = []
    text_encrypt_cords = []
    key_cords = []
    for ycolumn in range(26):
        for xrow in range(26):
            array[ycolumn][xrow] = d[xrow]
        d.rotate(rotate_nr)
    for letter in range(len(text_encrypt)):
        text_encrypt_cords.append(up_letters.find(text_encrypt[letter]))
        key_cords.append(up_letters.find(key[letter]))

    for cord, letter in enumerate(text_encrypt):
        key_cord = int(key_cords[cord])
        key_array = array[key_cord]
        encrypted_cord = key_array.index(text_encrypt[cord])
        message.append(up_letters[encrypted_cord])
    for space in space_cords:
        message.insert(space, " ")
    return ''.join(message)


class EnigmaSetup:
    # rotor_list = [ I, II, III, IV, V, VI, VII, VIII ]
    rotor_list = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO"
                  , "ESOVPZJAYQUIRHXLNFTGKDCMWB", "VZBRGITYUPSDNHLXAWMJQOFECK", "JPGVOUMFYQBENHZRDKASXLICTW"
                  , "NZJHGRCXMYSWBOUFAIVLPEKQDT", "FKQHTLXOCBJSPDZRAMEWNIUYGV"]
    # notch_list = [ I, II, III, IV, V, VI, VII, VIII ]
    notch_list = ["Q", "E", "V", "J", "Z", "ZM", "ZM", "ZM"]
    # reflector_list = [ UKW-A, UKW-B, UKW-C ]
    reflector_list = ["EJMZALYXVBWFCRQUONTSPIKHGD", "YRUHQSLDPXNGOKMIEBFZCWVJAT", "FVPJIAOYEDRZXWGCTKUQSBNMHL"]

    def __init__(self, rotor1, rotor2, rotor3, reflector):
        self.rotor1 = EnigmaSetup.rotor_list[rotor1-1]
        self.rotor2 = EnigmaSetup.rotor_list[rotor2 - 1]
        self.rotor3 = EnigmaSetup.rotor_list[rotor3 - 1]

        self.notch2 = EnigmaSetup.notch_list[rotor2 - 1]
        self.notch3 = EnigmaSetup.notch_list[rotor3 - 1]

        self.reflector = EnigmaSetup.reflector_list[reflector-1]

    def enigma_cipher(self, message, key, ring_setting, plugboard):

        def check_values(cmessage, ckey, cring_setting, cplugboard):
            """Check if arguments are correct"""
            check_message(ckey)
            check_message(cring_setting)
            check_message(cplugboard)
            if len(key) != 3 or len(cring_setting) != 3:
                print("This is 3 rotor Enigma, key and ring setting must contain 3 letters")
                exit()
            for check in cplugboard:
                if 1 < cplugboard.count(check) and check != " ":
                    print("Wrong plugboard - same letter can't occurs 2 times")
                    exit()
            return cmessage.upper(), ckey.upper(), cring_setting.upper(), cplugboard.upper()
        message, key, ring_setting, plugboard = check_values(message, key, ring_setting, plugboard)
        coded_message = ""
        from collections import deque
        # rotor1 + alphabet1, rotor2 + alphabet2, rotor3 + alphabet3
        alphabet_list = [deque(up_letters), deque(up_letters), deque(up_letters)]
        rotor_list = [self.rotor1, self.rotor2, self.rotor3]
        reflector = {}

        # set reflector
        for i_letter in range(26):
            reflector[up_letters[i_letter]] = self.reflector[i_letter]

        # set ring settings
        for index, letter in enumerate(ring_setting):
            letter_pos = up_letters.find(letter)
            d_caesar_rotor = deque(caesar_encrypt(rotor_list[index], letter_pos))
            d_caesar_rotor.rotate(letter_pos)
            rotor_list[index] = d_caesar_rotor

        # set ring positions ---> key = ring_position
        for index, letter in enumerate(key):
            shift_up = up_letters.find(letter)
            alphabet_list[index].rotate(-shift_up)
            rotor_list[index].rotate(-shift_up)

        # Convert plugboard to dictionary
        plugboard = plugboard.upper().replace(" ", "")
        plugboard_dict = {}
        for pair in range(0, len(plugboard), 2):
            plugboard_dict[plugboard[pair]] = plugboard[pair + 1]
            plugboard_dict[plugboard[pair + 1]] = plugboard[pair]

        for letter in message:
            if letter not in up_letters:
                coded_message += letter
            else:
                # ========== Rotors are rotated before letter encryption =================

                if alphabet_list[2][0] in self.notch3:
                    if alphabet_list[1][0] in self.notch2:
                        # left rotor is rotated
                        rotor_list[0].rotate(-1)
                        alphabet_list[0].rotate(-1)
                    # middle rotor is rotated
                    rotor_list[1].rotate(-1)
                    alphabet_list[1].rotate(-1)
                else:
                    # Check double step sequence
                    if alphabet_list[1][0] in self.notch2:
                        rotor_list[1].rotate(-1)
                        alphabet_list[1].rotate(-1)
                        rotor_list[0].rotate(-1)
                        alphabet_list[0].rotate(-1)

                # Right rotor is rotated before each letter
                rotor_list[2].rotate(-1)
                alphabet_list[2].rotate(-1)
                # ============================================================================

                # Plugboard 1 switch
                if letter in plugboard_dict.keys():
                    letter = plugboard_dict[letter]

                letter_cord = up_letters.index(letter)

                # from letter to reflector - Wheel 3, Wheel 2, Wheel 1
                for current_rotor in range(2, -1, -1):
                    rotor_letter = rotor_list[current_rotor][letter_cord]
                    letter_cord = alphabet_list[current_rotor].index(rotor_letter)

                # ================== reflector  ================================
                reflector_key = up_letters[letter_cord]  # check letter in alphabet with rotor cords
                reflector_value = reflector[reflector_key]
                letter_cord = up_letters.find(reflector_value)
                # ================== reflector  ================================

                # from reflector to encrypted letter -  Wheel 1,  Wheel 2,  Wheel 3
                for current_rotor in range(3):
                    rotor_letter = alphabet_list[current_rotor][letter_cord]
                    letter_cord = rotor_list[current_rotor].index(rotor_letter)
                encrypted_letter = up_letters[letter_cord]

                # Plugboard 2 switch
                if encrypted_letter in plugboard_dict.keys():
                    encrypted_letter = plugboard_dict[up_letters[letter_cord]]

                coded_message += encrypted_letter
        return coded_message
