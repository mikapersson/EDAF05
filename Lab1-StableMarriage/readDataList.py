import sys
import person

def readDataList():  #original readData file
    """Read input into lists of men and women (handles messy input)"""

    men = []
    women = []
    N = int(sys.stdin.readline())  #number of pairs

    input = sys.stdin.readlines()  #contains every individual and preferences in a list (string)
    input = ''.join(input).replace('\n', ' ')  #string representation of the input (nicer string)
    input = list(map(int, input.split(' ')[:-1]))  #int-list representation of the input
    input = [input[i]-1 for i in range(len(input))]  #subtract 1 from every element to avoid index-problems

    ids = input[::N+1]  #collect id's
    del input[::N+1]  #remove id's from input-list
    preferences = [input[n:n+N] for n in range(0, len(input), N)]  #preferences (ordered)

    finished = []  #list of observed women
    for i in range(2*N):
        tempID = ids[i]
        tempPref = preferences[i]

        if tempID not in finished:
            tempWoman = person.Person(tempID, tempPref)
            women.append(tempWoman)
            finished.append(tempID)
        else:
            tempMan = person.Person(tempID, tempPref)
            men.append(tempMan)

    return men, women