"""new_list = [0, 1, 2]
new_list2 = []
new_list2.append('element 0')
                 
new_list.append("a string")


[2*x for x in range(10)]
my_message = ("Hello World!")
old = 'e'
new = '3'
new_string = my_message.replace(old,new)
new_string

help(my_message.replace)


new_string = my_message.replace('e','3')"""





#1337
""" receive message, eval message, convert to secret code 
TEST_MESSAGE = ('Hello World!')
TEST_SUBSTITUTIONS = [['e','3']]"""

SUBSTITUTIONS = [['a','4'], ['e','3'],['l','l'],['o','0'],['y','7']]


#FUNCTIONS SECTION
def encode_message(message,substitutions):
    """ Take a string message plug in sunstitutions in form of a list,make it lists
    of two (old_string, new_string)"""
    for s in substitutions:
        old = s[0]
        new = s[1]
        message = message.replace(old,new)
        #print("converted text = "+message)
   #print("leaving encode_message")
        
    return message
   
 

    

#TESTING SECTION
message = input("Type the message to be encoded here: ")

converted_text = encode_message(message, SUBSTITUTIONS )
#print("started with "+message)
#print("converted to "+converted_text)
print(converted_text)
      

