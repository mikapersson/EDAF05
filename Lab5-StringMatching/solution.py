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

    if (string1, string2, result1, result2, total_gain) in align_cache:
        return align_cache[(string1, string2, result1, result2, total_gain)]
    else:  # if we already haven't computed the value for (string1, string2)

        length1 = len(string1)
        length2 = len(string2)
        max_res1 = ''
        max_res2 = ''
        if length1 == 0 and length2 == 0:    # base cases 1
            pass
        elif length1 > 0 and length2 == 0:   # base case 2
            temp_gain, res1, res2 = align_words_rec(string1[:-1], '', result1, result2, total_gain)
            temp_gain -= 4
            total_gain = temp_gain
            max_res1 = res1 + string1[-1]
            max_res2 = res2 + '*'
        elif length1 == 0 and length2 > 0:  # base case 3:
            temp_gain, res1, res2 = align_words_rec('', string2[:-1], result1, result2, total_gain)
            temp_gain -= 4
            total_gain = temp_gain
            max_res1 = res1 + '*'
            max_res2 = res2 + string2[-1]
        else:                                 # if both strings have length > 1
            letter1 = string1[-1]
            letter2 = string2[-1]

            value1, res11, res12 = align_words_rec(string1[:-1], string2[:-1], result1, result2, total_gain)

            value2, res21, res22 = align_words_rec(string1, string2[:-1], result1, result2, total_gain)

            value3, res31, res32 = align_words_rec(string1[:-1], string2, result1, result2, total_gain)

            max_value = max(value1, value2, value3)  # choosing the alternative with highest gain

            if max_value == value1:
                max_res1 = res11 + letter1
                max_res2 = res12 + letter2
            elif max_value == value2:
                max_res1 = res21 + '*'
                max_res2 = res22 + letter2
            else:
                max_res1 = res31 + letter1
                max_res2 = res32 + '*'

            align_cache[(string1, string2, result1, result2, total_gain)] = max_value + total_gain, max_res1, max_res2

            return total_gain + max_value, max_res1, max_res2

        align_cache[(string1, string2, result1, result2, total_gain)] = total_gain, max_res1, max_res2
        return total_gain, max_res1, max_res2


gain_matrix, let_to_ind, queries = setup()  # read input, set up cost_matrix and queries
align_cache = {}


for query in queries:
    # result1_list = []  # list of chars representing aligned 'word1'
    # result2_list = []  # list of chars representing aligned 'word2'
    word1 = query[0]
    word2 = query[1]
    align_words(word1, word2)




