from setup import setup
from math import inf


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
    return int(gain_matrix[let_to_ind[let1]][let_to_ind[let2]])


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
    init_gain = 0
    res1 = ''
    res2 = ''
    tot_gain, res1, res2 = align_words_rec(string1, string2, res1, res2, init_gain)  # BEHÖVER VI VERKLIGEN res1, res2?

    # result1 = ''.join(result1_list)
    # result2 = ''.join(result2_list)
    print(res1, res2)  # print resulting alignment


def align_words_rec(string1, string2, result1, result2, total_gain):
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

    # if we've already computed the value for (string1, string2, result1, result2, total_gain)
    if (string1, string2, result1, result2) in align_cache:
        return align_cache[(string1, string2, result1, result2)]
    else:

        length1 = len(string1)  # length of 'string1'
        length2 = len(string2)  # length of 'string2'
        letter1 = string1[-1]   # last letter in 'string1'
        letter2 = string2[-1]   # last letter in 'string2'
        if length1 == 1 and length2 == 1:    # base cases 1
            total_gain = gain(letter1, letter2)
            max_res1 = letter1
            max_res2 = letter2
        elif length1 > 1 and length2 == 1:   # base case 2
            total_gain = -4*(length1-1) + gain(letter1, letter2)
            max_res1 = string1
            max_res2 = '*'*(length1-1) + letter2
        elif length1 == 1 and length2 > 1:   # base case 3:
            total_gain = -4 * (length2 - 1) + gain(letter1, string2[-1])
            max_res1 = '*' * (length2 - 1) + letter1
            max_res2 = string2
        else:                                # if both strings have length > 1

            gain1, res11, res12 = align_words_rec(string1[:-1], string2[:-1], result1, result2, total_gain)
            gain1 += gain(letter1, letter2)

            substring1 = ''
            substring2 = ''
            gain2 = -inf

            if length1 > length2:
                substring1 = string1[:-2]
                substring2 = string2[:-1]
                gain2, res21, res22 = align_words_rec(substring1, substring2, result1, result2, total_gain)
                gain2 += gain(letter1, letter2) - 4
            elif length1 < length2:
                substring1 = string1[:-1]
                substring2 = string2[:-2]
                gain2, res21, res22 = align_words_rec(substring1, substring2, result1, result2, total_gain)
                gain2 += gain(letter1, letter2) - 4

            max_value = max(gain1, gain2)  # choosing the alternative with highest gain

            if max_value == gain1:
                max_res1 = res11 + letter1
                max_res2 = res12 + letter2
            # elif max_value == gain2:
            #    max_res1 = res21 + string1[-2:]
            #    max_res2 = res22 + '*' + letter2
            else:
                if length1 > length2:
                    max_res1 = res21 + string1[-2:]
                    max_res2 = res22 + '*' + letter2
                else:
                    max_res1 = res21 + '*' + letter1
                    max_res2 = res22 + string2[-2:]

            total_gain += max_value

        align_cache[(string1, string2, result1, result2)] = total_gain, max_res1, max_res2
        return total_gain, max_res1, max_res2


gain_matrix, let_to_ind, queries = setup()  # read input, set up cost_matrix and queries
align_cache = {}


for query in queries:
    # result1_list = []  # list of chars representing aligned 'word1'
    # result2_list = []  # list of chars representing aligned 'word2'
    word1 = query[0]
    word2 = query[1]
    align_words(word1, word2)




