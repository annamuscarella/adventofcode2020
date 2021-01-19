

bags = {}

def getBags(input):
    global bags
    for line in input:
        color = line[0:line.index(" bags")]
        bags[color] = []
        if('contain no other' in line):
                bags[color] = None
        else:
            line = line.replace(color + " bags contain ", '')
            containedBags = line.split(',')
            for bag in containedBags:
                bag = bag.lstrip()
                amount = bag[0:bag.index(" ")]
                if not amount.isdigit():
                    amount = 0
                bag = bag.replace((str(amount) + " "), '')
                colorContained = bag[0:bag.index(" bag")]
                bags[color].append({'color': colorContained, 'amount': int(amount)})
    return bags

def containsShinyBag(bagColor):
    print(bagColor)
    if bags[bagColor] is not None:
        returnValue = False
        for bag in bags[bagColor]:
            if bag.get('color') == 'shiny gold':
                returnValue = True
            else:
                returnValue = returnValue or containsShinyBag(bag.get('color'))
        return returnValue
    else:
        return False

def howManyBagsContained(bagColor):
    if bags[bagColor] is not None:
        returnValue = 0
        for bag in bags[bagColor]:
            returnValue += bag.get('amount') * (howManyBagsContained(bag.get('color'))+1)
        return returnValue
    else:
        return 0

def main(): 
    global bags
    with open ("inputlist.txt", "r") as input:
        data = [line.strip() for line in input.readlines()]
        bags = getBags(data)
        amount = howManyBagsContained('shiny gold')
            
        print(amount)

if __name__ == "__main__":
    main()