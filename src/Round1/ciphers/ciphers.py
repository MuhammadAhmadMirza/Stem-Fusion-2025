import os
import base64

def get_input_text(input_file):
    if os.path.exists(input_file):
        with open(input_file, 'r') as f:
            return f.read()
    else:
        return input_file

def output_result(result):
    """
    Prompts the user to choose whether to print the result to the console
    or to save it to a file. If saving, writes the result to the specified file path.
    """
    choice = input("Print result to console (c) or save to file (f)? ")
    if choice.lower() == 'c':
        print(result)
    elif choice.lower() == 'f':
        file_path = input("Enter file path to save result: ")
        with open(file_path, "w") as f:
            f.write(result)
        print("Result saved to", file_path)
        
def reverse_cipher(input_file):
    """
    Reverse Cipher Decryption:
    Reads text from the input_file and reverses it.
    Since encryption was done by reversing the text, decryption is simply reversing it again.
    The key parameter is ignored for this cipher.
    """
    text = get_input_text(input_file)
    result = text[::-1]
    output_result(result)
    
def substitution_cipher(input_file, key):
    """
    Substitution Cipher Decryption:
    Reads text from the input_file and decrypts it using a substitution cipher.
    The key should be a 26-character string representing the mapping for A-Z.
    Each letter in the ciphertext is replaced by the corresponding letter from the key
    based on its alphabetical position.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = get_input_text(input_file)
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                index = ord(char) - ord('A') # the ord() returns the ASCII value of the character, -A will give the index of the character in the alphabet
                result += key[index] # result will hold the decrypted text taken from the key
            else:
                index = ord(char.upper()) - ord('A')
                result += key[index].lower()
        else:
            result += char
    output_result(result)
    
def vigenere_cipher(input_file, key):
    """
    Vigenère Cipher Decryption:
    Reads text from the input_file and decrypts it using the Vigenère cipher.
    The key is a string where each character determines the shift for the corresponding
    letter in the ciphertext. Decryption subtracts the shift value (derived from the key letter)
    from each letter of the ciphertext modulo 26.
    """
    text = get_input_text(input_file)
    key = key.upper()
    result = ""
    j = 0
    for char in text:
        if char.isalpha():
            # to determine the shift value, we subtract the ASCII value of the key character from 'A'
            # j % len(key) ensures that we loop back to the beginning of the key if it is shorter than the text
            shift = ord(key[j % len(key)]) - ord('A') 
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                result += decrypted_char
            else:
                decrypted_char = chr((ord(char.upper()) - ord('A') - shift) % 26 + ord('A')).lower()
                result += decrypted_char
            j += 1
        else:
            result += char
    output_result(result)
    
def caesar_cipher(input_file, key):
    """
    Caesar Cipher Decryption:
    Reads text from the input_file and decrypts it using the Caesar cipher.
    The key must be an integer indicating the number of positions each letter was shifted.
    Decryption is performed by shifting letters backward by the key value modulo 26.
    """
    text = get_input_text(input_file)
    try:
        shift = int(key)
    except ValueError:
        print("Key must be an integer for Caesar cipher.")
        return
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
            # to get the result we subtract the ASCII value of 'A' from the ASCII value of the character and then subtract the shift value
            # to get the new ASCII value of the character
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
    output_result(result)
    
def modulo_cipher(input_file, key):
    """
    Modulo Cipher Decryption:
    Reads text from the input_file and decrypts it using a multiplicative cipher modulo 26.
    The key should be an integer 'a' that was used to multiply each letter's numeric value during encryption.
    Decryption involves computing the modular inverse of 'a' modulo 26 and then multiplying each
    letter's numeric value by this inverse.
    """
    text = get_input_text(input_file)
    try:
        a = int(key)
    except ValueError:
        print("Key must be an integer for modulo cipher.")
        return
    # a modular inverse is a number 'inv' such that (key * inv) % 26 == 1
    inv = None # will store the modular inverse of the key modulo 26
    for x in range(1, 26):
        if (a * x) % 26 == 1:
            inv = x
            break
    if inv is None:
        print("Key has no modular inverse modulo 26.")
        return
    result = ""
    for char in text:
        # to decrypt, we multiply the numeric value of the character by the modular inverse of the key modulo 26
        if char.isalpha():
            if char.isupper():
                num = ord(char) - ord('A')
                result += chr((num * inv) % 26 + ord('A'))
            else:
                num = ord(char) - ord('a')
                result += chr((num * inv) % 26 + ord('a'))
        else:
            result += char
    output_result(result)

def base64_decode(input_file, key):
    """
    Base64 Decoding:
    Reads Base64-encoded text from the input_file and decodes it using the base64 module.
    The key parameter is not used for Base64 decoding.
    """
    encoded = get_input_text(input_file).strip()
    decoded_bytes = base64.b64decode(encoded)
    try:
        result = decoded_bytes.decode('utf-8')
    except UnicodeDecodeError:
        result = decoded_bytes.decode('latin1')
    output_result(result)
    
def rot_cipher(input_file, key=None):
    """
    ROT Cipher Decryption:
    Reads text from the input_file and decrypts it using a rotation cipher.
    If key is not provided, defaults to 13 (ROT13).
    Decryption is performed by rotating letters backward by the key value modulo 26.
    """
    text = get_input_text(input_file)
    if key is None:
        shift = 13
    else:
        try:
            shift = int(key)
        except ValueError:
            print("Key must be an integer for ROT cipher.")
            return
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
    output_result(result)
