
from password import Password

def main(): 
    with open ("inputlist.txt", "r") as input:
        data = input.readlines()
        amountOfRightPasswords = 0
        for n in data:
            password = transformInput(n)
            print(password.toString())
            if password.isPasswordCorrectPt2():
                amountOfRightPasswords+=1
        print("Amount of right passwords: " + str(amountOfRightPasswords))

def transformInput(input):
    minus = input.find('-')
    minAmnt = input[0:minus]
    space = input.find(' ')
    maxAmnt=input[minus+1:space]
    colon = input.find(':')
    letter=input[space+1:colon]
    colon_space = input.find(': ')
    password=input[colon_space+1:len(input)]
    password = Password(minAmnt, maxAmnt, letter, password)
    return password


if __name__ == "__main__":
    main()