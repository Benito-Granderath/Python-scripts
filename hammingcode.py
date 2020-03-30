#Bisher nur ein Dezimal zu Binär kovertierer
decimal = 49
is0 = False
decimaldivide = decimal
rest = []
binary = []
while is0 != True:
    rest.append(decimaldivide % 2)
    decimaldivide = int(decimaldivide / 2)
    if decimaldivide == 0:
        is0 = True
for i in reversed(rest):
    binary.append(i)

print(binary)
input()
