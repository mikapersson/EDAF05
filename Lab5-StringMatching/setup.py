import sys


def setup():
    """
    Setup everything for solving lab5.
    More specific: read input, list letters, create cost_matrix and list queries. (return these)
    """
    letters = sys.stdin.readline().replace('\n', '').split()  # list containing letters
    nr_letters = len(letters)            # same as number of rows and columns in cost_matrix
    messy_input = sys.stdin.readlines()  # list of strings containing whole input except letters, this we will organize
    list_messy_input = []  # list containing every cost, nr_queries and queries as elements (will be sorted later)
    for element in messy_input:
        for el in element.replace('\n', '').split():
            list_messy_input.append(el)

    letter_to_index = {}  # dictionary for translating letter to its corresponding index
    for index, letter in enumerate(letters):  # filling 'letter_to_index'
        letter_to_index[letter] = index

    gain_matrix = [list_messy_input[n:n + nr_letters] for n in range(0, nr_letters ** 2, nr_letters)]

    # nr_queries = list_messy_input[nr_letters**2 + 1]  # we know that number of queries is given after the costs
    queries = [list_messy_input[n:n+2] for n in range(nr_letters**2+1, len(list_messy_input), 2)]  # queries x 2 matrix

    return gain_matrix, letter_to_index, queries
