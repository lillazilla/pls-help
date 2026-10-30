from operator import truediv

#LS
#PA5a
#write letters sideways in asterisks
def main():
    msg = "n"
    msg = str(input("Input message: "))
    length = len(msg)

    if length <1:
        return

    #check for valid letters
    for i in range(length):
        letter = msg[i]
        if letter == "h" or letter == "H":
            h()
        elif letter == "d" or letter == "D":
            d()
        elif letter == "e" or letter == "E":
            e()
        elif letter == "l" or letter == "L":
            l()
        elif letter == "o" or letter == "O":
            o()
        elif letter == "r" or letter == "R":
            r()
        elif letter == "w" or letter == "W":
            w()
        else:
            blank()
    pass

#funcs for letters
def h():
    print("\n")
    print("*******")
    print("   *   ")
    print("   *   ")
    print("   *   ")
    print("*******")
    print("\n")

def blank():
    print("\n\n")

def d():
    print("\n")
    print("*******")
    print("*     *")
    print("*     *")
    print(" *   * ")
    print("  ***  ")
    print("\n")

def l():
    print("\n")
    print("*******")
    print("*      ")
    print("*      ")
    print("*      ")
    print("*      ")
    print("\n")

def e():
    print("\n")
    print("*******")
    print("*  *  *")
    print("*  *  *")
    print("*  *  *")
    print("*  *  *")
    print("\n")

def o():
    print("\n")
    print("*******")
    print("*     *")
    print("*     *")
    print("*     *")
    print("*******")
    print("\n")

def r():
    print("\n")
    print("*******")
    print("   *  *")
    print("  **  *")
    print(" * ****")
    print("*      ")
    print("\n")

def w():
    print("\n")
    print("*******")
    print("*      ")
    print("****   ")
    print("*      ")
    print("*******")
    print("\n")

if __name__ == "__main__":
    main()