
from seat import Seat

def sortSeats(seatTouple):
        return seatTouple[0]

def main(): 
    with open ("inputlist.txt", "r") as input:
        seats = []
        for line in [line.strip() for line in input.readlines()]:
            seats.append(Seat(line))

        seatIds = []
        for seat in seats:
            seatIds.append((seat.getSeatNumber(), seat))
        seatIds.sort(key=sortSeats)
        #print(seatIds)

        freeSeats = []
        for i, seatId in enumerate(seatIds):
            if i < len(seatIds) -1:
                if seatIds[i-1][0] == seatId[0]-2 or seatIds[i+1][0] == seatId[0] + 2:
                    freeSeats.append(seatId[1])
        for freeSeat in freeSeats:
            print(freeSeat.row)
            print(freeSeat.col)
            print(freeSeat.getSeatNumber())
        print(str(freeSeats))


if __name__ == "__main__":
    main()