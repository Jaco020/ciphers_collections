#  made by Jaco, for cryptography learning
import string
low_letters = string.ascii_lowercase
up_letters = string.ascii_uppercase
all_letters = up_letters + low_letters
all_symbols = string.printable + " " + "\n"


def check_message(message):
    """Check if message is correct - used by all other cipher functions"""
    for check in message:
        if check not in all_letters:
            print("Error - Message can only contain 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' letters")  # check if message is Correct
            exit()


def check_key_nr(number):
    """Check if key number is correct - used by functions that require key number"""
    if number != int:
        print("Error - key is not int")  # check if message is Correct
        exit()


def check_index(active_array, item):
    """Check row and column index of 2d array - used by playfair"""
    for r in range(5):
        for c in range(5):
            if active_array[r][c] == item:
                return [r, c]


def reverse_array(active_array):
    """Reverse 2d array - used by playfair"""
    r_array = [["_" for xcolumn in range(5)] for yrow in range(5)]
    for r in range(5):
        for c in range(5):
            r_array[r][c] = active_array[c][r]
    return r_array


def caesar_encrypt(text_encrypt, key_number):
    """ Encrypt message by caesar cipher
    caesar_encrypt(message you want to encrypt, transition of letters (number) )"""
    check_message(text_encrypt)
    check_key_nr(key_number)
    if key_number > 26:
        print("Alphabet is only 26 in length")
        exit()
    message = []
    for letter in text_encrypt:
        if -1 != up_letters.find(letter):
            location = up_letters.find(letter)
            if location == 25:
                location = -1
            message.append(up_letters[location+key_number])
        elif -1 != low_letters.find(letter):
            location = low_letters.find(letter)
            if location == 25:
                location = -1
            message.append(low_letters[location + key_number])
        else:
            message.append(all_symbols[all_symbols.find(letter)])
    return ''.join(message)


def caesar_decrypt(text_encrypt, key_number):
    """ Decrypt message by caesar cipher
    caesar_decrypt(message you want to decrypt, transition of letters (number) )"""
    check_message(text_encrypt)
    check_key_nr(key_number)
    if key_number >= 26:
        print("Trans number is higher than one cycle")
        exit()
    message = []
    key_number = 0 - key_number
    for letter in text_encrypt:
        if -1 != up_letters.find(letter):
            location = up_letters.find(letter)
            if location == 0:
                location = 26
            message.append(up_letters[location+key_number])
        elif -1 != low_letters.find(letter):
            location = low_letters.find(letter)
            if location == 0:
                location = 26
            message.append(low_letters[location + key_number])
        else:
            message.append(all_symbols[all_symbols.find(letter)])
    return ''.join(message)


def fence_cipher_encrypt(text_encrypt, key_number):
    """ Encrypt message by fence cipher
    fence_cipher_encrypt(message you want to encrypt, height of fence(number))"""
    check_message(text_encrypt)
    check_key_nr(key_number)

    message = []
    operation_nr, direction_nr, index = 0, 1, 0  # index is for text_encrypt
    text_length = int(len(text_encrypt))
    fence_array = [["_" for xcolumn in range(text_length)] for yrow in range(key_number)]  # generate array
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
    check_message(text_encrypt)
    check_key_nr(key_number)

    message = []
    operation_nr, direction_nr = 0, 1
    text_length = int(len(text_encrypt))
    fence_array = [["_" for xcolumn in range(text_length)] for yrow in range(key_number)]  # generate array
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
    for check in [" ", "\n", "\t"]:
        text_encrypt = text_encrypt.replace(check, "")
    check_message(text_encrypt)
    for check in key:
        if 1 < key.count(check):
            print("Wrong key - same letter can't occurs 2 times")  # check if key is Correct
            exit()
        elif check not in all_letters:
            print("Error - Key can only contain 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' letters")  # check if key is Correct
            exit()

    text_encrypt = text_encrypt.upper()
    key = key.upper()
    text_encrypt = text_encrypt.replace("J", "I")
    message = []
    correct_letters = []
    operation_nr = 0
    check_situation = False

    def mark_next_letter(active_array):
        """Mark the correct letter for fist and second situation - used by playfair"""
        letter_1 = check_index(active_array, text_encrypt[operation_nr])[1]
        letter_2 = check_index(active_array, text_encrypt[operation_nr + 1])[1]  # checks column position of pair
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

    array = [["_" for xcolumn in range(5)] for yrow in range(5)]
    for rindex in range(5):
        for cindex in range(5):  # creates 2d array
            array[rindex][cindex] = correct_letters[operation_nr]
            operation_nr += 1
    operation_nr = 0
    rev_array = reverse_array(array)
    for pair in range(int(len(text_encrypt) / 2)):  # check every pair of text
        for y in range(5):
            if text_encrypt[operation_nr] in array[y] and text_encrypt[operation_nr + 1] in array[y]:
                # ===== first situation ===== #
                mark_next_letter(array)
                check_situation = True
                break
            elif text_encrypt[operation_nr] in rev_array[y] and text_encrypt[operation_nr + 1] in rev_array[y] and not check_situation:
                # ===== second situation ===== #
                mark_next_letter(rev_array)
                check_situation = True
                break
            else:
                check_situation = False

        # ===== third situation ===== #
        if not check_situation:
            x1 = check_index(array, text_encrypt[operation_nr])
            x2 = check_index(array, text_encrypt[operation_nr + 1])
            message.append(array[x1[0]][x2[1]])
            message.append(array[x2[0]][x1[1]])

        operation_nr += 2  # check another pair
    return ''.join(message)


def playfair_decrypt(text_encrypt, key):
    """ Decrypt message by playfair cipher
    playfair_decrypt(message you want to decrypt, key)
    """
    for check in [" ", "\n", "\t"]:
        text_encrypt = text_encrypt.replace(check, "")
    check_message(text_encrypt)
    for check in key:
        if 1 < key.count(check):
            print("Wrong key - same letter can't occurs 2 times")  # check if key is Correct
            exit()
        elif check not in all_letters:
            print("Error - Key can only contain 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' letters")  # check if key is Correct
            exit()

    text_encrypt = text_encrypt.upper()
    key = key.upper()
    text_encrypt = text_encrypt.replace("J", "I")
    message = []
    correct_letters = []
    operation_nr = 0
    check_situation = False

    def mark_next_letter(active_array):
        """Mark the correct letter for fist and second situation - used by playfair"""
        letter_1 = check_index(active_array, text_encrypt[operation_nr])[1]
        letter_2 = check_index(active_array, text_encrypt[operation_nr + 1])[1]  # checks column position of pair
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

    array = [["_" for xcolumn in range(5)] for yrow in range(5)]
    for rindex in range(5):
        for cindex in range(5):  # creates 2d array
            array[rindex][cindex] = correct_letters[operation_nr]
            operation_nr += 1

    operation_nr = 0
    rev_array = reverse_array(array)
    for pair in range(int(len(text_encrypt) / 2)):  # check every pair of text
        for y in range(5):
            if text_encrypt[operation_nr] in array[y] and text_encrypt[operation_nr + 1] in array[y]:
                # ===== first situation ===== #
                mark_next_letter(array)
                check_situation = True
                break
            elif text_encrypt[operation_nr] in rev_array[y] and text_encrypt[operation_nr + 1] in rev_array[y] and not check_situation:
                # ===== second situation ===== #
                mark_next_letter(rev_array)
                check_situation = True
                break
            else:
                check_situation = False

        # ===== third situation ===== #
        if not check_situation:
            x1 = check_index(array, text_encrypt[operation_nr])
            x2 = check_index(array, text_encrypt[operation_nr + 1])
            message.append(array[x1[0]][x2[1]])
            message.append(array[x2[0]][x1[1]])

        operation_nr += 2  # check another pair
    return ''.join(message)
