import re
f = open("email.txt", "a")
try:
    file = open("test.csv")
    for line in file:
        line = line.strip()
        emails = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+\.[0-9a-zA-z]+", line)
        if(len(emails) > 0):
            print(emails)
            for email in emails :
                f.write(email + "\n")
except FileNotFoundError as e:
    print(e)
f.close()
