import re

class Passport:
    def __init__(self):
        self.values = {}


    def setAttr(self, key, value):
        self.values[key] = str(value)

    def isPassportValid(self):
        requiredFields = ['byr', 'iyr', 'eyr', 'hcl', 'ecl', 'pid','hgt']
        returnValue = True
        try:
            for field in requiredFields:
                returnValue = returnValue and bool(self.isAttrValid(field,self.values[field]))
                if returnValue == False:
                    print("FALSE, " + field + ": " + self.values[field])
                    break
        except KeyError:
            return False
        else:
            return returnValue

    def printPassport(self):
        returnStr = ""
        for i in self.values:
            returnStr = returnStr + i + ":" + self.values[i] + " "
        return returnStr

    def isAttrValid(self, key, value):
        if key == 'byr':
            result =  bool(1920 <= int(value) <= 2002)
            return result

        elif key == 'iyr':
            result = bool(2010 <= int(value) <= 2020)
            return result

        elif key == 'eyr':
            result =  bool(2020 <= int(value) <= 2030)
            return result

        elif key == 'hgt':
            if value[-2:] == "in" and 59 <= int(value[:-2]) <= 76:
                return True
            elif value[-2:] == "cm" and 150 <= int(value[:-2]) <= 193:
                return True
            else:
                return False

        elif key == 'hcl':
            regexResult = bool(re.match('^#([0-9]|[a-f])*$', str(value)))
            if regexResult == False:
                print('Value: ' + value + ", Result: " + str(regexResult))
            return bool(regexResult)  and len(value) == 7

        elif key == 'ecl':
            availableColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if value in availableColors:
                return True
            else: 
                return False

        elif key == 'pid':
            return bool(re.match(r'^\d{9}$', value))
            