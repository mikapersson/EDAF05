import readDataList
import time

def GS():
    """Gale-Shapley Algorithm (p.117 in course book)"""

    #print("GS start")
    tstart = time.time()
    #print("Read data start")
    men, women, readTime= readDataList.readDataList()
    #print("Read data finished")
    pairs = {}  #dictionay with 'woman : man'-pairs (just indices)
    p = men.copy()

    while len(p) > 0:
        m = p.pop(0)  #take out the first element of p (Person object)
        w = m.prefs.pop(0)  #the woman m prefers the most and hasn't proposed to yet (int/index)

        if w not in pairs:  #if w doesn't have a partner
            pairs[w] = m.id
        else:
            #determine if w prefers m over her current partner mw
            mw = men[pairs[w]]
            if women[w].prefs[m.id] < women[w].prefs[mw.id]:
                del pairs[w]
                pairs[w] = m.id
                p.append(mw)
            else:
                p.append(m)

    tend = time.time()
    resTime = tend - tstart
    #print("GS finished")
    return pairs, resTime, readTime

#RUN ALGORITHM
result, algTime, readTime = GS()

#SORT COUPLES ACCORDING TO WOMEN
sortTS = time.time()
result = sorted(result.items(), key=lambda kv: kv[0])
sortTE = time.time()
sortTime = sortTE - sortTS

#for p in result:
#    print(p[1] + 1)  #increment id (no need to keep track of indexes anymore)

#COMMENT THIS WHEN TESTING THE PROGRAM
print("TIMES: read data - {} ; algorithm - {} ; sort map - {}".format(readTime, algTime, sortTime))
print("Total time: ", readTime+algTime+sortTime)


