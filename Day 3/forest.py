class Forest:
    def __init__(self, input):
        self.forestArray = input

    def getAmountOfTreesInSlope(self, incrementX, incrementY):
        positionX = 0
        positionY = 0
        i = 0
        amountOfTrees=0
        while i < self.getForestLength()-1:
            positionX+=incrementX
            positionY+=incrementY
            if positionX >= self.getForestWidth():
                positionX -= self.getForestWidth()
            amountOfTrees+=self.isPositionTree(positionX, positionY)
            i+=incrementY
        print("AMOUNT OF TREES: " + str(amountOfTrees))
        return amountOfTrees

    def getForestWidth(self):
        return len(self.forestArray[0])

    def getForestLength(self):
        return len(self.forestArray)

    def isPositionTree(self,x,y):
        print("x:"+str(x) + ", y: " + str(y) )
        return self.forestArray[y][x] == '#'

    def getForestArray(self):
        return self.forestArray

    def setChar(self, x,y, charact):
        yChar = self.forestArray[int(y)]
        print(yChar)
        yChar[int(x)] = yChar[int(x)].replace('.', charact).replace('#', charact)
        self.forestArray[int(y)] = yChar