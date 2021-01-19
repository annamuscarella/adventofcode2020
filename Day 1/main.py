
data = []

def main(): 
    with open ("inputlist.txt", "r") as input:
        global data
        data = input.readlines()
        transformArrayToNumbers()
        index = 0
        for n in data:
            checkIfNextNumberIsGreater(n, index)
            index += 1
        print(data)

def checkIfNextNumberIsGreater(n,i):
    global data
    if i > len(data) - 1:
        return
    if (data[i] + n) == 2020:
        print("number1: " + str(n))
        print("number2: " + str(data[i]))
        print("product: " + str(data[i] * n))
    else:
        checkIfNextNumberIsGreater(n, i + 1)

def transformArrayToNumbers():
    global data
    i = 0
    for n in data:
        data[i] = int(n.replace('\n', ''))
        print(data[i])
        i+=1

if __name__ == "__main__":
    main()