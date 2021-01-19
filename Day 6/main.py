


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
                for person in currGroup:
                    for answer in person:
                        amountOfQuestionsAnsweresYes += 1
                        #delete from other persons answers
                        for i, person in enumerate(currGroup):
                            currGroup[i] = person.replace(answer, '')
                print("Questions answered: " + str(amountOfQuestionsAnsweresYes), "currGroup: " + str(currGroup))
                count += amountOfQuestionsAnsweresYes
                currGroup = []
    print("COUNT: " + str(count))
            


if __name__ == "__main__":
    main()