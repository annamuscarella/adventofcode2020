
from seat import Seat

def main(): 
    with open ("inputlist.txt", "r") as input:
        seats = []
        for line in [line.strip() for line in input.readlines()]:
            seats.append(Seat(line))
        highestSeat = 0
        for seat in seats:
            seatNumber = seat.getSeatNumber()
            if highestSeat < seatNumber:
                highestSeat = seatNumber

        print(highestSeat)


if __name__ == "__main__":
    main()