#Heather Loree and Christina Roberts
"""Turning a regular message in to a secret code """

import string


CHAR_SET = string.printable[:-5]
SUBSTITUTION_CHARS = CHAR_SET[-3:]+CHAR_SET[:-3]

ENCRYPTION_DICT = {}
DECRYPTION_DICT = {}
for i,k in enumerate(CHAR_SET):
    v = SUBSTITUTION_CHARS[i]
    ENCRYPTION_DICT[k] = v
    DECRYPTION_DICT[v] = k

    for c in string.printable[-5:]:
        ENCRYPTION_DICT[c] = c
        DECRYPTION[c]= c 

TEST_MESSAGE = "I like Monty Python. They are very funny."
INPUT_FILE_NAME = "cryptopy_input.txt"
OUTPUT_FILE_NAME = "cryptopy_output.txt"

#Functions Section
def encrypt_msg(plaintext, encrypt_dict): 
    """Take a plaintext message and encrypt each character using the encryption
    dictionary provided. key translates to its associated value.
    Return the ciphertext"""
    ciphertext = []
    for k in plaintext:
        v = encrypt_dict[k]
        ciphertext.append(v)
    return ''.join(ciphertext)
    

def decrypt_msg(ciphertext, decrypt_dict): 
    """Take a ciphertext message and decrypt each character using the decryption
    dictionary provided. value translates to its associated key.
    Return the plaintext"""
    plaintext = []
    for k in ciphertext:
        v = decrypt_dict[k]
        plaintext.append(v)
    return ''.join(plaintext)


##INPUT OUTPUT SECTION
#ciphertext = encrypt_msg(CHAR_SET, ENCRYPTION_DICT)
#print(TEST_MESSAGE) #ORIGINAL

#print(ciphertext)


#test_message = TEST_MESSAGE
#ciphertext = encrypt_msg(test_message, ENCRYPTION_DICT)
#plaintext = decrypt_msg(ciphertext, DECRYPTION_DICT)

#print(test_message)
#print(ciphertext)
#print(plaintext)
#print(plaintext == test_message)
                         
#message = input("Type the message to encrypt below:\n")
#ciphertext = encrypt_msg(message, ENCRYPTION_DICT)
#plaintext = decrypt_msg(message, DECRYPTION_DICT)
#print("This message encrypts to")
#print(ciphertext)
#print(" ")
#print ("This message decrypts to")
#print(plaintext)


##MAINSECT
if__name__= "__main__":
    ENCRYPT = False

    with open(INPUT_FILE_NAME, 'r') as input_file:
        message = input_file.read()

    if Encrypt:
        text_to_output = encrypt_msg(message, ENCRYPTION_DICT)

    else:
        test_to_output = decrypt_msg(message, DECRYPT_DICT)

    prit(text_to_output

    with open(OUTPUT_FILE_NAME, 'w') as output_file:
         output_file.write(text_to_output)
         

