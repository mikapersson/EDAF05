from functools import lru_cache
import matplotlib.pyplot as plt
import numpy as np
from time import time

"""Small program for testing cache memory when computing Fibonacci numbers"""

N = int(input("Choose Fibonacci number: "))
its = int(input("Number of iterations: "))
fibonacci_cache = {}


def fibonacci(n):
    """
    Compute the n:th fibonacci number with the explicit cache 'fibonacci_cache'.
    """
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value


@lru_cache(maxsize=N)
def lru_fibonacci(n):
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    else:
        value = lru_fibonacci(n-1) + lru_fibonacci(n-2)
    return value


iteration = np.arange(0, its)
times_exfib = [0]*its
times_lrufib = [0]*its
for i in range(its):
    exfibstart = time()
    for ef in range(1, N):
        fibonacci(ef)
    exfibend = time()
    exfibtotal = exfibend-exfibstart
    times_exfib[i] = exfibtotal

    lrufibstart = time()
    for lru in range(1, N):
        lru_fibonacci(lru)
    lrufibend = time()
    lrufibtotal = lrufibend - lrufibstart
    times_lrufib[i] = lrufibtotal

extimes = np.asarray(times_exfib)
lrutimes = np.asarray(times_lrufib)
mean1 = sum(extimes)/its
mean2 = sum(lrutimes)/its
print(mean1, '\n', mean2)
if mean1 < mean2:
    print("Explicit method is faster")
else:
    ratio = abs((mean2-mean1)/mean1)
    print("lru method is faster by a factor of ", ratio)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(iteration, extimes)
ax1.set_title('Times for explicit Fibonacci')
ax2.plot(iteration, lrutimes)
ax2.set_title('Times for lru Fibonacci')
plt.show()
