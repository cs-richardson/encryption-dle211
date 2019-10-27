"""
This program will take the plaintext and the shift key from the user, and then
prints out the ciphertext.
Coded by Justin Le
"""

# Asks the user for the plaintext and the shift key
plainText = str(input("plaintext: "))
cipherText = ""
shift = int(input("shift: "))
while shift > 26:
    shift = shift - 26

# Creates the lowercase and uppercase alphabet and stores it in a variable
lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"
upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = lowerAlphabet + upperAlphabet

# Creates the lowercase and uppercase cipher based on the shift key and
# stores it in a variable
lowerCipher = lowerAlphabet[shift:] + lowerAlphabet[:shift]
upperCipher = upperAlphabet[shift:] + upperAlphabet[:shift]
cipher = lowerCipher + upperCipher

# Checks and shifts each letter in the plaintext
for i in range(len(plainText)):
    for j in range(len(alphabet)):
        if plainText[i] == alphabet[j]:
            cipherText = cipherText + cipher[j]
    if plainText[i] not in alphabet:
        cipherText = cipherText + plainText[i]

# Prints ciphertext
print("ciphertext: " + cipherText)
