from read_data import read_create

""" Solution to lab 6 """

N, M, C, P = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))  # read input





# Create the graph

# Have a method for finding the source (s)? just get node with value 0?

# Iterate FF alg. while removing some edges through P
# and stop when the flow is below C.

# Print the number of edges/routes we could remove + maximal flow



'''
FRÅGOR
- plocka inte bort kant! lägg till kant istället, börja bakifrån!
-> eftersom vi gör detta kommer s och t ändras? ska vi då ha koll på vad de aktuella s och t är?
'''
