import readDataList

def GS():
    """Gale-Shapley Algorithm (p.117 in course book)"""

    men, women = readDataList.readDataList()
    pairs = {}  #dictionay with 'woman : man'-pairs
    p = men.copy()

    while len(p) > 0:
        m = p.pop(0)  #take out the first element of p (Person object)
        w = m.prefs.pop(0)  #the woman m prefers the most and hasn't proposed to yet (integer/index)

        if w not in pairs:  #if w doesn't have a partner
            pairs[w] = m.id
        else:
            #determine if w prefers m over her current partner mw
            tempWoman = 0  #woman with id = w
            womIndex = 0
            while tempWoman == 0:
                if women[womIndex].id == w:
                    tempWoman = women[womIndex]
                womIndex += 1

            mw = pairs[w]
            if tempWoman.prefs.index(m.id) < tempWoman.prefs.index(mw):
                del pairs[w]
                pairs[w] = m.id

                tempMan = 0  # man with id = mw
                manIndex = 0
                while tempMan == 0:
                    if men[manIndex].id == mw:
                        tempMan = men[manIndex]
                    manIndex += 1
                p.append(tempMan)
            else:
                p.append(m)

    return pairs

#RUN ALGORITHM
result = GS()

#SORT COUPLES ACCORDING TO WOMEN
result = sorted(result.items(), key=lambda kv: kv[0])
for p in result:
    print(p[1] + 1)


