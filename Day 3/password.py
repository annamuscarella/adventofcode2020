class Password:
    def __init__(self, minAmnt, maxAmnt, letter, passwrd):
        self.minAmnt = int(minAmnt)
        self.maxAmnt = int(maxAmnt)
        self.letter = letter
        self.passwrd = passwrd

    def isPasswordCorrect(self):
        amnt = self.passwrd.count(self.letter)
        if(self.minAmnt <= amnt <= self.maxAmnt):
            return True
        return False
    
    def isPasswordCorrectPt2(self):
        return (self.passwrd[self.minAmnt]==self.letter) != (self.passwrd[self.maxAmnt]==self.letter)


    def toString(self):
        return "minAmnt: " + str(self.minAmnt) + ", maxAmnt: " + str(self.maxAmnt) + ", letter: " + self.letter + ", password: " + self.passwrd + ", isValid: " + str(self.isPasswordCorrectPt2())