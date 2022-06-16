"""
File: anagram.py
Name: 李汝民
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

dictionary = []


def main():
    """
    1. Prompt the user to input a word for searching anagrams.
    2. Record start time of searching.
    3. Run find_anagrams() function.
    4. Record the end time of searching, print the time user to find all the anagrams.
    5. If input == '-1', end the program.
    """
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        start = time.time()
        if s == '-1':
            break
        else:
            print('Searching...')
            find_anagrams(s)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary(file, s):
    """
    Read the dictionary file and prepare(shrink) it for anagram searching.
    :param file: (str) Filename of the English dictionary
    :param s: (str) User input word
    :return: (list) The prepared(shrunk) dictionary.
    """
    global dictionary

    # Count the times each letter appears in the user input, letter as key and times as value.
    count_s = {}
    for _ in s:
        count_s[_] = count_s.get(_, 0) + 1

    with open(file, 'r') as f:
        for line in f:
            # Only examine the words in the English dictionary with same length as the user input.
            if len(line.strip()) == len(s):
                # Count the times each letter appears in the word, letter as key and times as value.
                count_line = {}
                for _ in line.strip():
                    count_line[_] = count_line.get(_, 0) + 1
                # Compare the two dictionaries, if identical then add the word to the (shrunk) English dictionary.
                if count_line == count_s:
                    dictionary.append(line.strip())


def find_anagrams(s):
    """
    Receives the user input, run the read_dictionary() function,
    :param s: (str) The user input word
    :return: This function does not return anything
    """
    global dictionary
    read_dictionary(FILE, s)

    s_num_list = []
    result_list = []

    # create a numerical list to represent the user input word, for that this simplifies the permutation
    # process where there are duplicate letters in the word (ex. 'contains' got two 'n's).
    for i in range(len(s)):
        s_num_list.append(i)

    find_anagrams_helper(s, s_num_list, [], '', len(s), result_list)

    # When the find_anagrams_helper() function completed, print the number of anagrams and the list thereof.
    print(f'{len(result_list)} anagrams: {result_list}')

    # Empty the English dictionary for next input.
    dictionary = []


def find_anagrams_helper(s, s_num_list, current_lst, current_word, ans_lst, anagrams_list):
    """
    Generate all the permutations of the numerical list from the find_anagrams() function, and
    create the matching 'word' to be searched in the English dictionary. With the help of the
    has_prefix() function, this function will skip those permutations that is unlikely to match
    any word in the (shrunk) English dictionary.
    :param s: (str) The user input word
    :param s_num_list: (list) The created numerical list having same length as the user input word
    :param current_lst: (list) Empty list, to be used in finding permutations
    :param current_word: (str) Empty string, to be user in creating the matching 'word' reflecting the permutation
    :param ans_lst: (int) The length of the user input word
    :param anagrams_list: (list) Empty list, to store the found anagrams
    :return: This function does not return anything
    """
    # When base case reached
    if len(current_lst) == ans_lst:

        # Generate the word reflecting the permutation of numerical list
        for _ in current_lst:
            current_word += s[_]

        # Match the word for anagrams in the (shrunk) dictionary.
        if current_word in dictionary:
            if current_word not in anagrams_list:
                anagrams_list.append(current_word)
                print(f'Found: {current_word}')
                print('Searching...')

    # When base case not reached
    else:
        # Run permutations for the numerical list
        for _ in s_num_list:
            if _ in current_lst:
                pass
            # Skip the (partial) permutation that is unlikely to find anagram in the (shrunk) dictionary.
            elif not has_prefix(s, current_lst, ''):
                pass
            # Choose, explore, un-choose.
            else:
                current_lst.append(_)
                find_anagrams_helper(s, s_num_list, current_lst, current_word, ans_lst, anagrams_list)
                current_lst.pop()


def has_prefix(s, sub_s, current_sub_str):
    """
    Checks if the (partial) permutation is unlikely to have any match in the (shrunk) dictionary.
    :param s: (str) The user input
    :param sub_s: (list) The (partial) permutation to be searched
    :param current_sub_str: (str) Empty str, to create the word reflecting the (partial) permutation
    :return: (boolean) Whether any word in the (shrunk) dictionary starts with the partial word
    """
    # Generate the partial word according to the (partial) permutation
    for _ in sub_s:
        current_sub_str += s[_]

    # check if any word in the (shrunk) dictionary starts with the partial word
    for word in dictionary:
        if not word.startswith(str(current_sub_str)):
            pass
        elif word.startswith(str(current_sub_str)):
            return True
    return False


if __name__ == '__main__':
    main()
