from libraryLetters import *


while True:
    print("Input word:")
    lett = input()

    if lett in libr:
        print(libr[lett])
    else:
        print("Not found")
