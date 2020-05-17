from random import randint
from time import time


def recInversions(arr):
    tempInvs = 0
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        invs1 = recInversions(L)
        invs2 = recInversions(R)
        tempInvs = invs1 + invs2

        first = second = actual = 0  #indices for L, R, arr
        while first < len(L) and second < len(R):
            if L[first] < R[second]:
                arr[actual] = L[first]
                first += 1
            else:
                arr[actual] = R[second]
                notsame = first
                while notsame < len(L) and R[second] == L[notsame]:
                    notsame += 1
                if notsame != len(L):
                    tempInvs += len(L[notsame:])
                second += 1
            actual += 1

        # Checking if any element was left
        while first < len(L):
            arr[actual] = L[first]
            first += 1
            actual += 1

        while second < len(R):
            arr[actual] = R[second]
            second += 1
            actual += 1

    return tempInvs

def inversions(arr):
    if len(arr) > 1:
        return recInversions(arr)

#TESTING
N = 10**7
test = [randint(1,10) for i in range(4)]
rev = [i for i in range(N)]
reversed(rev)
print(test)
precise = [8,7,5,8]
stime = time()
invs = inversions(rev)
etime = time()
totTime = etime - stime
print(test)
print(invs)
print("Total time: ", totTime)







