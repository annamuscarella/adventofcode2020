


def main(): 
    with open ("inputlist.txt", "r") as input:
        data = [line.strip() for line in input.readlines()]
        count = 0
        currGroup = []
        for i,line in enumerate(data):
            if len(line) > 0:
                currGroup.append(line)
            if len(line) == 0 or i >= len(data) -1: 
                print("group end")
                print(currGroup, end="\n")
                amountOfQuestionsAnsweresYes = 0

                #iterate over all answers of first person
                for answer in currGroup[0]:
                    isAnsweredByAll = True
                    for person in currGroup:
                        if answer in person:
                            continue
                        else:
                            isAnsweredByAll = False
                            break
                    if isAnsweredByAll:
                        amountOfQuestionsAnsweresYes += 1
                        for i,person in enumerate(currGroup):
                            currGroup[i]=person.replace(answer, '')

                print("Questions answered: " + str(amountOfQuestionsAnsweresYes), "currGroup: " + str(currGroup))
                count += amountOfQuestionsAnsweresYes
                currGroup = []
    print("COUNT: " + str(count))
            


if __name__ == "__main__":
    main()