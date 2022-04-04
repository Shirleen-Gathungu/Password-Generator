# Mini Project -Random password Generator!

#Importing the relevant modules
import random
#All uppercase password
password=""
for i in range(10):
    i=chr(random.randint(65, 90)).lower()
    password=str(password) +i
    print(password)

    # Upper and lowercase password
    password=""
    for i in range(5):
        i=chr(random.randint(65, 90)).lower()
        password=str(password)+ i + i +i
        print(password)






