def main(): 
    with open ("inputlist.txt", "r") as input:
        data = [line.strip() for line in input.readlines()]
        lines = {}
        for i,line in enumerate(data):
            lines[i] = {'operation': str(line[0:line.index(' ')]), 'number': str(line[line.index(' ')+1:len(line)]), 'used': False}
        ldo = lines.copy()
        for i in range(len(lines)):
            lines = ldo.copy()
            ln = lines[i]
            if ln['operation'] == 'nop':
                ln['operation'] = 'jmp'
            elif ln['operation'] == 'jmp':
                ln['operation'] = 'nop'
            data[i] = ln
            if callOperation(lines, 0,0) < 0:
                print("GOT IT")

        
        print("Acc Task 1: " + str(callOperation(lines, 0,0)))

def callOperation(lines, lineIdx, acc):
    if lineIdx >= len(lines):
        print("FINISHED")
        return -1
    currOperation = lines[lineIdx]
    newLineIdx = lineIdx
    if currOperation['used']:
        return acc
    if currOperation['operation'] == 'acc':
        acc += int(currOperation['number'])
        newLineIdx += 1
    elif currOperation['operation'] == 'jmp':
        newLineIdx += int(currOperation['number'])
    elif currOperation['operation'] == 'nop':
        newLineIdx += 1

    currOperation['used'] = True
    lines[lineIdx] = currOperation
    return callOperation(lines, newLineIdx, acc)

if __name__ == "__main__":
    main()