Encryption Function (caesar_cipher_encrypt):

This function takes a text and a shift value as input.
It iterates through each character in the text. If the character is an alphabet letter, it calculates the new shifted character, preserving the case (uppercase or lowercase). Non-alphabet characters remain unchanged.
Decryption Function (caesar_cipher_decrypt):

This function works similarly to the encryption function but shifts characters in the opposite direction to reverse the encryption.
Main Function (main):

It prompts the user to choose between encryption and decryption.
It gets the message and shift value from the user.
Depending on the user's choice, it calls the appropriate function and displays the result.
The user is asked if they want to process another message, allowing the loop to continue or break based on their input.
You can run this program in a Python environment, and it will interactively guide you through encrypting and decrypting messages using the Caesar Cipher algorithm.
