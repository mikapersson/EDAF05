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
    tot_gain, res1, res2 = align_words_rec(string1, string2, res1, res2, init_gain)

    # result1 = ''.join(result1_list)
    # result2 = ''.join(result2_list)
    print(res1, res2)  # print resulting alignment


def align_words_rec(string1, string2, result1, result2, total_gain):
    """
    Recursive help function for 'align_words' function (can be shortened + use help functions)

    Parameters
    ----------
    string1 : str
        First string as in 'align_words'
    string2 : str
        Second string as in 'align_words'
    result1 : str
        Result of the first word in the current query
    result2 : str
        Result of the second word in the current query
    total_gain : int
        Current total gain (from before, not 'string1' and 'string2'

    Returns
    -------
    (int, string, string)
        (total gain between 'string1' and 'string2', aligned first string, aligned second string)
    """

    # if we've already computed the value for (string1, string2, result1, result2, total_gain)
    if (string1, string2, result1, result2) in align_cache:
        return align_cache[(string1, string2, result1, result2)]  # BEHÖVS result1 och result2??
    else:

        length1 = len(string1)
        length2 = len(string2)

        if length1 == 0 and length2 == 0:   # base case 1
            total_gain = 0
            string1_result = ''
            string2_result = ''
        elif length1 > 0 and length2 == 0:  # base case 2
            total_gain = -4 * length1

            string1_result = string1
            string2_result = '*' * length1
        elif length1 == 0 and length2 > 0:  # base case 3
            total_gain = -4 * length2

            string1_result = '*' * length2
            string2_result = string2
        else:
            letter1 = string1[-1]
            letter2 = string2[-1]

            # no '*' added
            gain1, res11, res12 = align_words_rec(string1[:-1], string2[:-1], result1, result2, total_gain)
            gain1 += gain(letter1, letter2)

            # '*' added after letter1
            gain2, res21, res22 = align_words_rec(string1, string2[:-1], result1, result2, total_gain)
            gain2 -= 4

            # '*' added after letter2
            gain3, res31, res32 = align_words_rec(string1[:-1], string2, result1, result2, total_gain)
            gain3 -= 4

            max_gain = max(gain1, gain2, gain3)

            if max_gain == gain1:
                max_res1 = res11 + letter1
                max_res2 = res12 + letter2
            else:
                if max_gain == gain2:
                    max_res1 = res21 + '*'
                    max_res2 = res22 + letter2
                elif max_gain == gain3:
                    max_res1 = res31 + letter1
                    max_res2 = res32 + '*'

            string1_result = max_res1
            string2_result = max_res2

        align_cache[(string1, string2, result1, result2)] = total_gain, string1_result, string2_result
        return total_gain, string1_result, string2_result


gain_matrix, let_to_ind, queries = setup()  # read input, set up cost_matrix and queries
align_cache = {}


for query in queries:
    word1 = query[0]
    word2 = query[1]
    align_words(word1, word2)




