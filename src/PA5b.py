
#TODO: Document this function
def main():
    cont = True
    while cont:
        print("Enter a stream of non-negative numbers (negative when finished): ", end="")
        average = avg()
        print(f"The average is: {average:.2f}")
        val = input("Do you want to compute another average (y/n)? ")
        if val == "n" or val == "N":
            cont = False
    pass

def avg():
    value = 0
    sum = 0
    count = 0
    while value >= 0:
        value = float(input())
        if value >= 0:
            sum = sum+value
            count = count+1
    if count > 0:
        avgs = sum/count
        return avgs
    else:
        return 0

if __name__ == '__main__':
    main()