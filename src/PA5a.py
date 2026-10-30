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
    print("")
    print("*******")
    print("   *   ")
    print("   *   ")
    print("   *   ")
    print("*******")
    print("")

def blank():
    print("\n\n")

def d():
    print("")
    print("*******")
    print("*     *")
    print("*     *")
    print(" *   * ")
    print("  ***  ")
    print("")

def l():
    print("")
    print("*******")
    print("*      ")
    print("*      ")
    print("*      ")
    print("*      ")
    print("")

def e():
    print("")
    print("*******")
    print("*  *  *")
    print("*  *  *")
    print("*  *  *")
    print("*  *  *")
    print("")

def o():
    print("")
    print("*******")
    print("*     *")
    print("*     *")
    print("*     *")
    print("*******")
    print("")

def r():
    print("")
    print("*******")
    print("   *  *")
    print("  **  *")
    print(" * ****")
    print("*      ")
    print("")

def w():
    print("")
    print("*******")
    print("*      ")
    print("****   ")
    print("*      ")
    print("*******")
    print("")

if __name__ == "__main__":
    main()
