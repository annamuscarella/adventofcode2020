

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
    print(bagColor + " bags contain " + str(bags[bagColor]))
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

def main(): 
    global bags
    with open ("inputlist.txt", "r") as input:
        data = [line.strip() for line in input.readlines()]
        bags = getBags(data)
        shinyBags = []
        for i, bagColor in enumerate(bags.keys()):
                if containsShinyBag(bagColor):
                    shinyBags.append(bagColor)
            
        print(len(list(set(shinyBags))))

if __name__ == "__main__":
    main()