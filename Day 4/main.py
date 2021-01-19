
from passport import Passport

def main(): 
    with open ("inputlist.txt", "r") as input:
        data = [line.strip() for line in input.readlines()]
        passports = [Passport()]
        for line in data:
            attributes = line.split(" ")
            if len(attributes) > 0 and ':' in line:
                for attr in attributes:
                    keyvalue = attr.split(":")
                    currPassport = passports[len(passports)-1]
                    currPassport.setAttr(keyvalue[0],keyvalue[1])
            else:
                passports.append(Passport())

        
        amountOfRightPassports = 0
        for passport in passports:
            amountOfRightPassports += passport.isPassportValid()

        print("Amount of valid passports: " + str(amountOfRightPassports))


if __name__ == "__main__":
    main()