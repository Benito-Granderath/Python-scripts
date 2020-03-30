import random
import time
import os
x = 0
Fuchs_Hungrig = False
K = 1000
F = 40
Genug_Futter = True
Naturkatastrophe = 5
Tag = 0
A = 0
B = 0


while Genug_Futter:
    if F >= K:
        Genug_Futter = False
    time.sleep(1)
    A = K
    if Naturkatastrophe == 1:
        K = K - K / 2
        F = F - F / 2
        print("Es ist eine Naturkatastrophe geschehen! ")
    Naturkatastrophe = random.randint(1, 100)
    Fuchs_Hungrig = False
    x = x + 0.25
    if x.is_integer():
        Fuchs_Hungrig = True
    if Fuchs_Hungrig:
        K = K - ((F * K) / random.randint(150, 350))
    K = K * random.randint(101, 111)/100
    F = F * random.randint(101, 103)/100
    Tag = Tag + 1
    B = K
    E = open("Daten.txt", "a+")
    E.write(str(Tag) + ", ")
    E.close()
    D = open("Daten.txt", "a+")
    D.write(str(round(F)) + "\n")
    D.close()
    x1 = open("Daten2.txt", "a+")
    x1.write(str(Tag) + ", ")
    x1.close()
    x2 = open("Daten2.txt", "a+")
    x2.write(str(round(K)) + "\n")
    x2.close()
    print("Tag " + str(round(Tag)), end="")
    if not Fuchs_Hungrig:
        print(": Die Füchse sind satt.                                                    ", end="")
    else:
        print(": Die Füchse waren aus Hunger auf Jagd und haben ", end="")
        print(round(A - K), end="")
        print(" Kaninchen geschnappt.    ", end="")
    print(" Es sind noch " + str(round(F)) + " Füchse und " + str(round(K)) + " Kaninchen übrig!")


print("Es ist nicht genug Futter für die Füchse übrig!")
time.sleep(1)


