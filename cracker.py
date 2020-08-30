import zipfile as zippi
import itertools
import string
import hashlib

file = zippi.ZipFile(r"C:\Users\Kartexx\Desktop\CRACKED.zip")

def cracker(zip, pwd):
    try:
        print(pwd)
        zip.extractall(pwd=str.encode(pwd))
        print("Success! " + pwd)
    except:
        pass

def dictionary():
    plist = open(r"C:\Users\Kartexx\Desktop\realhuman_phill.txt", 'r', encoding="utf8")
    for lines in plist:
        pwd = lines.strip('\n')
        cracker(file, pwd)
    plist.close()

def generate_rainbowtable():
    plist = open(r"C:\Users\Kartexx\Desktop\realhuman_phill.txt", 'r', encoding="utf8")
    output = open("rainbowtable.txt", 'w', encoding="utf8")
    for lines in plist:
        pwd = lines.strip('\n')
        hash = hashlib.sha512(str.encode(pwd))
        output.write(hash.hexdigest() + ' - ' + pwd + "\n")
        print(pwd)
    output.close()
    plist.close()

def crackHash(hash):
    rainbowtable = open("rainbowtable.txt", encoding="utf8")
    for line in rainbowtable:
        hashpwd = line.split(' - ', 1)
        if hash == hashpwd[0]:
            print(hashpwd[1])

def bruteforce():
    attempts = string.digits
    for i in range(4,5):
        for j in map(''.join, itertools.product(attempts, repeat=i)):
            cracker(file, j)