from setup import setup
from math import inf


"""First try of solving lab 5, dynamic programming"""


def gain(let1, let2):
    """
    Calculates the gain of the two letters 'let1' and 'let2'

    Parameters
    ----------
    let1 : str
        First letter
    let2 : str
        Second Letter
    Returns
    -------
    int
        The gain of 'let1' and 'let2' according to the gain matrix
    """
    return int(gain_matrix[let_to_ind[let1]][let_to_ind[let2]])


def backtrack():
    """
    Finds the optimal alignment of 'word1' and 'word2' with respect to 'align_cache'.

    Returns
    -------
    str : aligned1
        'word1' aligned
    str : aligned2
        'word2' aligned
    """


def align_words():
    """
    Find optimal alignment, given 'string1' and 'string2',
    such that the total gain of aligning the strings in maximized

    Parameters
    ----------
    string1 : str
        First string in query
    string2 : str
        Second string in query
    """

    global word1
    global word2

    align_words_rec(len(word1)-1, len(word2)-1)
    aligned1, aligned2 = backtrack()
    print(aligned1, aligned2)


def align_words_rec(pos1, pos2):
    """
    Recursive help function for 'align_words' function,
    actually fills out 'align_cache'

    Parameters
    ----------
    int : pos1
        Last position in string1
    int : pos2
        Last position in string2

    Returns
    -------
    (int, string, string)
        (total gain between 'string1' and 'string2', aligned first string, aligned second string)
    """

    # if we've already computed the value for (pos1, pos2)
    if (pos1, pos2) in align_cache:
        return align_cache[(pos1, pos2)]
    else:
        letter1 = word1[pos1]
        letter2 = word2[pos2]

        if pos1 == 0 and pos2 == 0:   # base case 1
            max_gain = gain(letter1, letter2)
        elif pos1 > 0 and pos2 == 0:  # base case 2
            temp_gain = align_words_rec(pos1-1, pos2)
            max_gain = temp_gain - 4
        elif pos1 == 0 and pos2 > 0:  # base case 3
            temp_gain = align_words_rec(pos1, pos2-1)
            max_gain = temp_gain - 4
        else:


            # no '*' added
            gain1 = align_words_rec(pos1-1, pos2-1)
            gain1 += gain(letter1, letter2)

            # '*' added after letter1
            gain2 = align_words_rec(pos1, pos2-1)
            gain2 -= 4

            # '*' added after letter2
            gain3 = align_words_rec(pos1-1, pos2)
            gain3 -= 4

            max_gain = max(gain1, gain2, gain3)

        align_cache[(pos1, pos2)] = max_gain
        return max_gain


gain_matrix, let_to_ind, queries = setup()  # read input, set up cost_matrix and queries
align_cache = {}


for query in queries:
    word1 = query[0]
    word2 = query[1]
    align_words()
    align_cache.clear()




