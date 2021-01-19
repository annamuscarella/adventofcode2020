def main(): 
    with open ("inputlist.txt", "r") as input:
        data = [line.strip() for line in input.readlines()]
        lines = {}
        for i,line in enumerate(data):
            if(i >= 25):
                a = i - 25
                if checkIfNumberIsValid(data, i, a):
                    break
                else:
                    print("INVALID NUMBER:" + str(data[i]))


def checkIfNumberIsValid(data, i, a):
    for a in range(a, i-2):
        _sum = data[a] + data[a+1]
        if _sum == data[i]:
            return True
        elif a == (i-2):
            return False


if __name__ == "__main__":
    main()