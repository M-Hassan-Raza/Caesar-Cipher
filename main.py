"""This module contains the main function for the program."""


def main():
    """Main function for the program."""
    plaintext = input("Enter the plaintext to encrypt")
    key = input("Enter the key of the cipher")

    if plaintext is None or plaintext == "":
        return "Empty string can't be encoded"
    if (key is None) or (key == 0) or (not isinstance(key, int)):
        return "Empty key can't be encoded"

    return calculate_cipher(plaintext, key)


def calculate_cipher(plaintext_string, key):
    """Takes in a key and a string, returns the cipher"""
    cipher = ""
    for char in plaintext_string:
        if char == " ":
            cipher += " "
        elif (ord(char) < 65 or (ord(char) > 90 and ord(char) < 97)) or (
            (ord(char) < 97 and ord(char) > 90) or ord(char) <= 122
        ):
            cipher += " "
        cipher += chr((ord(char) - 97 + key) % 26 + 97)

    return cipher


if __name__ == "__main__":
    main()
