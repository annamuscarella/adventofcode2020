import math
class Seat:
    AMOUNT_OF_ROWS=128
    AMOUNT_OF_COLS=8

    def __init__(self, input):
        self.seatCode = str(input)
        self.row = self.__getSeatRow()
        self.col = self.__getSeatColumn()

    def __getSeatRow(self):
        return self.__getNumber(Seat.AMOUNT_OF_ROWS, 'F', 'B')

    def __getSeatColumn(self):
        #return 1
        return self.__getNumber(Seat.AMOUNT_OF_COLS, 'L', 'R')

    def __getNumber(self, amount, charLower, charHigher):
        lowerBorder = 0
        higherBorder = amount - 1
        for i in self.seatCode:
            if i == charLower or i == charHigher:
                middle = (higherBorder - lowerBorder) / 2 + lowerBorder
                if i == charLower:
                    higherBorder = math.floor(middle)
                elif i == charHigher:
                    lowerBorder = math.ceil(middle)
        return lowerBorder

    def getSeatNumber(self):
        return self.row * 8 + self.col

    