def main():
    """Main function for the program."""
    plaintext = input("Enter the plaintext to encrypt: ")
    key = input("Enter the key of the cipher: ")
    if plaintext is None or plaintext == "":
        print("Empty string can't be encoded")
        return
    if not key.isdigit():
        print("Key must be a positive integer")
        return

    key = int(key)
    print(calculate_cipher(plaintext, key))


def calculate_cipher(plaintext_string, key):
    """Takes in a key and a string, returns the cipher"""
    cipher = ""
    for char in plaintext_string:
        if char == " ":
            cipher += " "
        elif not char.isalpha():
            cipher += char
        elif char.islower():
            cipher += chr((ord(char) - ord("a") + key) % 26 + ord("a"))
        else:
            cipher += chr((ord(char) - ord("A") + key) % 26 + ord("A"))

    return cipher


if __name__ == "__main__":
    main()
