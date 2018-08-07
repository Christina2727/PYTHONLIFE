file_object = open('p4k_test.py','w')
text = "print('Hello from within the file')\n"
file_object.write(text)
file_object.write(text)
file_object.close()


"""file_object =open('p4k_test.py', 'r')
print(file_object.read())
file_object.close()


file_object.close()
file_object = open('p4k_test.py','r')
counter = 0
for line in file_object.readlines():
    counter = counter+1
    print(str(counter)+ " : "+line)

file_object.close"""


with open('p4k_test.py','r') as file_object:
    print(file_object.read())
    
