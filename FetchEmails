import re

f = open("email.txt", "a")

#Get the emails from test.csv and place them in email.txt file.

try:
    file = open("test.csv")
    for line in file:
        line = line.strip()
        emails = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+\.[0-9a-zA-z]+", line)
        if(len(emails) > 0):
            print(emails)
            f.write(emails[0] + "\n")


    
 
except FileNotFoundError as e:
    print(e)


f.close()
