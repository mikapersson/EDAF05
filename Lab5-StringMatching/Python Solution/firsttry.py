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
            string1_result = letter1
            string2_result = letter2
        elif length1 > 1 and length2 == 1:   # base case 2
            total_gain = -4*(length1-1) + gain(letter1, letter2)

            string1_result = string1
            string2_result = '*'*(length1-1) + letter2  # check if we add the star before of after
        elif length1 == 1 and length2 > 1:   # base case 3:
            total_gain = -4 * (length2 - 1) + gain(letter1, letter2)
            string1_result = '*' * (length2 - 1) + letter1
            string2_result = string2
        else:                                # if both strings have length > 1

            gain1, res11, res12 = align_words_rec(string1[:-1], string2[:-1], result1, result2, total_gain)
            gain1 += gain(letter1, letter2)

            right = True  # for determining if we add the '*' on the right or left side of letter1 (or letter2)
            gain2 = -inf

            if length1 > length2:  # if string1 is longer than string2

                # ADDING TO THE RIGHT SIDE OF letter2
                substring1_right = string1[:-1]
                substring2_right = string2  # just from clarification
                gain2_right, res21_right, res22_right = align_words_rec(substring1_right, substring2_right, result1,
                                                                        result2, total_gain)
                gain2_right -= 4

                # ADDING TO THE LEFT OF letter2
                substring1_left = string1[:-2]
                substring2_left = string2[:-1]
                gain2_left, res21_left, res22_left = align_words_rec(substring1_left, substring2_left, result1,
                                                                     result2, total_gain)
                gain2_left += gain(letter1, letter2) - 4

                if gain2_right > gain2_left:
                    gain2 = gain2_right
                    res21 = res21_right
                    res22 = res22_right
                else:
                    gain2 = gain2_left
                    res21 = res21_left
                    res22 = res22_left
                    right = False
            elif length1 < length2:  # if string1 is shorter than string2
                substring1_right = string1  # just from clarification
                substring2_right = string2[:-1]

                # ADDING TO THE RIGHT SIDE OF letter1
                gain2_right, res21_right, res22_right = align_words_rec(substring1_right, substring2_right, result1,
                                                                        result2, total_gain)
                gain2_right -= 4

                # ADDING TO THE LEFT OF letter1
                substring1_left = string1[:-1]
                substring2_left = string2[:-2]
                gain2_left, res21_left, res22_left = align_words_rec(substring1_left, substring2_left, result1,
                                                                     result2, total_gain)
                gain2_left += gain(letter1, letter2) - 4

                if gain2_right > gain2_left:
                    gain2 = gain2_right
                    res21 = res21_right
                    res22 = res22_right
                else:
                    gain2 = gain2_left
                    res21 = res21_left
                    res22 = res22_left
                    right = False

            max_value = max(gain1, gain2)  # choosing the alternative with highest gain

            if max_value == gain1:
                max_res1 = res11 + letter1
                max_res2 = res12 + letter2
            else:
                if length1 > length2:
                    if right:  # if the '*' is appended to the right of letter2
                        max_res1 = res21 + letter1
                        max_res2 = res22 + '*'
                    else:      # if the '*' is appended to the left of letter2
                        max_res1 = res21 + string1[-2:]
                        max_res2 = res22 + '*' + letter2
                else:
                    if right:  # if the '*' is appended to the right of letter1
                        max_res1 = res21 + '*'
                        max_res2 = res22 + letter2
                    else:      # if the '*' is appended to the left of letter1
                        max_res1 = res21 + '*' + letter1
                        max_res2 = res22 + string2[-2:]

            string1_result = max_res1
            string2_result = max_res2

            total_gain += max_value

        align_cache[(string1, string2, result1, result2)] = total_gain, string1_result, string2_result
        return total_gain, string1_result, string2_result


gain_matrix, let_to_ind, queries = setup()  # read input, set up cost_matrix and queries
align_cache = {}


for query in queries:
    word1 = query[0]
    word2 = query[1]
    align_words(word1, word2)




