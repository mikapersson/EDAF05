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
    init_gain = 0
    align_words_rec(string1, string2, init_gain)

    result1 = ''.join(result1_list)
    result2 = ''.join(result2_list)
    print(result1, result2)  # print resulting alignment


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
    if length1 == 0 and length2 == 0:    # base cases 1
        return total_gain
    elif length1 > 1 and length2 == 0:   # base case 2
        temp_gain = align_words_rec(string1[:-1], '', total_gain) - 4
        result1_list.append(string1[-1])
        result2_list.append('*')
        return total_gain + temp_gain
    elif length1 == 0 and length2 > 1:  # base case 3:
        temp_gain = align_words_rec('', string2[:-1], total_gain) - 4
        result1_list.append('*')
        result2_list.append(string2[:-1])
        return total_gain + temp_gain
    else:                                 # if both strings have length > 1
        letter1 = string1[-1]
        letter2 = string2[-1]

        if (string1, string2) in align_cache:
            return align_cache[(string1, string2)]
        else:
            value1 = align_words_rec(string1[:-1], string2[:-1], total_gain) + gain(letter1, letter2)
            value2 = align_words_rec(string1, string2[:-1], total_gain) - 4
            value3 = align_words_rec(string1[:-1], string2, total_gain) - 4
            max_value = max(value1, value2, value3)  # choosing the alternative with highest gain

            if max_value == value1:
                result1_list.append(letter1)
                result2_list.append(letter2)
            elif max_value == value2:
                result1_list.append('*')
            else:
                result2_list.append('*')

            align_cache[(string1, string2)] = max_value

            return total_gain + max_value


letters, gain_matrix, let_to_ind, queries = setup()  # read input, set up cost_matrix and queries
align_cache = {}


for query in queries:
    result1_list = []  # list of chars representing aligned 'word1'
    result2_list = []  # list of chars representing aligned 'word2'
    word1 = query[0]
    word2 = query[1]
    align_words(word1, word2)




