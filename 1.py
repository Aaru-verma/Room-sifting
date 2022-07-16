studentName = [
    "Ankita kumari", "Anjali kumari", "Poonam", "Tina kumari", "Arpita lataye",
    "Sakshi zagade", "Chitra karwate", "Ankita pisal", "Jiza sarak", "Monika",
    "Priti meshram", "Aachuki raigar", "Jyoti patidar", "Amisha sharma", "Usha bisht",
    "Ishita", "Ishika", "Deepanjali", "Shivani karve", "Megha sharma",
    "Aarti kumari", "Kavitha", "Insha", "Jaya", "Janvi", "Komal", "Sweta verma", "Sanjana Jha"
    ]


roomNumber = [401,402,403,404,405,406]


import random


student = int(input("enter the number of students :-"))
dict1={}
i = 0
c = 0
k = 0
while i < len(studentName):
    j = 0
    list1 = []
    while j < student:
        if len(studentName) == c:
            break
        list1.append(studentName[c])
        if len(roomNumber) > k:
            pass
        else:
            dict1[random.choice(roomNumber)].append(studentName[c])
        j += 1
        c += 1
    if len(roomNumber) > k:
        dict1[roomNumber[k]] = list1
    i += student
    k += 1
print(dict1)










