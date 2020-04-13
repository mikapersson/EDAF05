from setup import setup


"""Solution for lab 5, dynamic programming"""


def gain(let1, let2):
    """
    Calculates the gain of the two letters 'let1' and 'let2'

    Parameters
    ----------
    let1 : str
        First letter
    let2 : str

    Returns
    -------
    int
        The gain of 'let1' and 'let2' according to the gain matrix
    """
    return gain_matrix[let_to_ind[let1]][let_to_ind[let2]]


def align_words(string1, string2):
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
    total_gain = 0
    align_words_rec(string1, string2, total_gain)
    print(string1, string2)  # print resulting alignment


def align_words_rec(string1, string2, total_gain):
    """
    Recursive help function for 'align_words' function

    Parameters
    ----------
    string1 : str
        First string as in 'align_words'
    string2 : str
        Second string as in 'align_words'
    total_gain : int
        Current total gain (from before, not 'string1' and 'string2'

    Returns
    -------
    int
        Total gain between 'string1' and 'string2'
    """

    length1 = len(string1)
    length2 = len(string2)
    if length1 == 1 and length2 == 1:    # base cases 1
        return gain(string1, string2)
    elif length1 > 1 and length2 == 1:   # base case 2
        return
    elif length1 == 1 and length2 > 1:  # base case 3:
        return
    else:                                 # if both strings have length > 1
        letter1 = string1[-1]
        letter2 = string2[-1]
        # if parameters in align_cache: do something, else: compute everything and add to cache
        if (string1, string2) in align_cache:
            return align_cache[(string1, string2)]
        else:
            value1 = (gain(letter1, letter2) + align_words_rec(string1[:-1], string2[:-1], total_gain))
            value2 =

            max_value = max(value1, value2)
            if max_value == value1:

            elif max_value == value2:

            else:

            align_cache[(string1, string2)] = max_value


        #print(string1, string2)


letters, gain_matrix, let_to_ind, queries = setup()  # read input, set up cost_matrix and queries
align_cache = {}

for query in queries:
    word1 = query[0]
    word2 = query[1]
    align_words(word1, word2)




