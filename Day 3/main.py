
from forest import Forest

def main(): 
    with open ("inputlist.txt", "r") as input:
        data = [line.strip() for line in input.readlines()]
        forest = Forest(data)
        slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
        result = 1
        for n in slopes:
            print("Slope " + str(n[0]) + ", " + str(n[1]))
            result = result * forest.getAmountOfTreesInSlope(n[0], n[1])
        print("RESULT: " + str(result))


if __name__ == "__main__":
    main()