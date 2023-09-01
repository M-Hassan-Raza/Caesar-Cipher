"""This module contains the main function for the program."""

def main():
    """Main function for the program."""
    

def calculate_cipher(plaintext_string, key):
    """Takes in a key and a string, returns the cipher """
    cipher = ""
    plaintext_string = plaintext_string.strip(" ")
    for char in plaintext_string:
        cipher += chr((ord(char) - 97 + key) % 26 + 97)

    return cipher