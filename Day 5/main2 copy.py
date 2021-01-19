
from seat import Seat

def main(): 
    with open ("inputlist.txt", "r") as input:
        seats = []
        for line in [line.strip() for line in input.readlines()]:
            seats.append(Seat(line))

        plane = [[0 for i in range(Seat.AMOUNT_OF_COLS)] for i in range(Seat.AMOUNT_OF_ROWS)]
        seatIds = []
        for seat in seats:
            plane[seat.row][seat.col] = 'X'
            seatIds.append(seat.getSeatNumber())
        seatIds.sort()

        for r, row in enumerate(plane):
            for i, singleseat in enumerate(row):
                if str(singleseat) == '0':
                    try: 
                        mySeatIdx = seatIds.index(i * 8 + r)
                        print(mySeatIdx)
                        if seatIds[mySeatIdx - 1] == mySeatIdx -1 and seatIds[mySeatIdx + 1] == mySeatIdx + 1:
                            print("MySeat: " + i * 8 + r)
                    except ValueError:
                        print("Value does not exist")

if __name__ == "__main__":
    main()