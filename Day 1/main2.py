
data = []

def main(): 
    with open ("inputlist.txt", "r") as input:
        global data
        data = input.readlines()
        transformArrayToNumbers()
        for n in data:
            for m in data:
                for l in data:
                    if n + m + l == 2020:
                        print("number1: " + str(n))
                        print("number2: " + str(m))
                        print("number3: " + str(l))
                        print("product: " + str(m * n * l))
                        return

def transformArrayToNumbers():
    global data
    i = 0
    for n in data:
        data[i] = int(n.replace('\n', ''))
        i+=1

if __name__ == "__main__":
    main()