#Heather Loree and Christina Roberts
"""Turning a regular message in to a secret code """

import string


#variable char_set assignment to string.printable and chop off last 5 elements
CHAR_SET = string.printable[:-5]
#create variable substitution_char assign take last 3 characters and put them on front of list,
#chop off last 3 characters from end 
SUBSTITUTION_CHARS = CHAR_SET[-3:]+CHAR_SET[:-3]
#print out output in program to user to show the original alphanbet we are using
# then skip to new line and print out the "secret code" version, can be used as decoding table
#print(CHAR_SET[:62]+'\n'+SUBSTITUTION_CHARS[:62])

ENCRYPTION_DICT = {}
DECRYPTION_DICT = {}
for i,k in enumerate(CHAR_SET):
    v = SUBSTITUTION_CHARS[i]
    ENCRYPTION_DICT[k] = v
    DECRYPTION_DICT[v] = k

TEST_MESSAGE = "I like Monty Python. They are very funny."


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
                         
message = input("Type the message to encrypt below:\n")
ciphertext = encrypt_msg(message, ENCRYPTION_DICT)
plaintext = decrypt_msg(message, DECRYPTION_DICT)
print("This message encrypts to")
print(ciphertext)
print(" ")
print ("This message decrypts to")
print(plaintext)


