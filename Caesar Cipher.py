def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) + shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) + shift_amount - 97) % 26 + 97)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) - shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) - shift_amount - 97) % 26 + 97)
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        print("Caesar Cipher Program")
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")
            continue
        
        text = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == 'e':
            encrypted_text = caesar_cipher_encrypt(text, shift)
            print(f"Encrypted Message: {encrypted_text}")
        else:
            decrypted_text = caesar_cipher_decrypt(text, shift)
            print(f"Decrypted Message: {decrypted_text}")
        
        again = input("Do you want to encrypt/decrypt another message? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
e