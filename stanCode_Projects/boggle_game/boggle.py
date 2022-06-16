"""
File: boggle.py
Name: 李汝民
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This function prompts the user to provide the 4x4 'board' of the boggle, which will be used in the other
	functions to locate all words that can be found in the board.  This function also times the total time
	spent on locating all the words in the board.
	"""

	####################
	#                  #
	#       TODO:      #
	#                  #
	####################
	while True:
		# board = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]

		# Prompts the user to enter the 4x4 board
		board = []
		first_row = input('1 row of letters: ')
		if len(first_row) != 7:
			print('Illegal input')
			break
		board.append(first_row.lower().split(' '))

		second_row = input('2 row of letters: ')
		if len(second_row) != 7:
			print('Illegal input')
			break
		board.append(second_row.lower().split(' '))

		third_row = input('3 row of letters: ')
		if len(third_row) != 7:
			print('Illegal input')
			break
		board.append(third_row.lower().split(' '))

		fourth_row = input('4 row of letters: ')
		if len(fourth_row) != 7:
			print('Illegal input')
			break
		board.append(fourth_row.lower().split(' '))

		# Record the start time of the searching function
		start = time.time()

		# Runs the searching function
		ans = find_all_boggle(board, [])
		print(f'There are {len(ans)} words in total.')

		# Record the end time of the searching function
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')
		break


def find_all_boggle(board, eng_dict):
	"""
	This function receives the board, runs the dictionary preparation function, and uses a double for loop
	to scan through all the blocks in the board.
	:param board: (nested list) The board provided by user
	:param eng_dict: (list) An empty list
	:return: (list) A list of the words found in the board
	"""
	read_dictionary(FILE, eng_dict)

	rows, cols = len(board), len(board[0])		# Sets the range of the double for loop
	ans = []

	for r in range(rows):
		for c in range(cols):
			find_all_boggle_helper(r, c, '', board, rows, cols, ans, eng_dict)

	return ans


def find_all_boggle_helper(r, c, word, board, rows, cols, ans, eng_dict):
	"""
	This function recursively try possible routes on the board to construct words and find any match
	in the prepared English dictionary.
	:param r: (int) The row where the end of the current route sits
	:param c: (int) The column where the end of the current route sits
	:param word: (str) The current combination of word comprised of each letter on the route visited
	:param board: (list) The user provided board
	:param rows: (int) The total rows of the board
	:param cols: (int) The total columns of the board
	:param ans: (list) The words found on the board
	:param eng_dict: (list) The prepared English dictionary
	:return: The function does not return anything
	"""
	# Setting the edge of recursion, namely the base case
	if r < 0 \
		or c < 0 \
		or r == rows \
		or c == cols \
		or not has_prefix(word, eng_dict) \
		or board[r][c] == '#':
		return

	# When current combination of word has a match in the English dictionary
	if len(word) >= 4 and word in eng_dict and word not in ans:
		print(f'Found: {word}')
		ans.append(word)

	# String the letter of the current block to the word
	word += board[r][c]

	# Mark the current block as visited, while maintaining the letter for later un-mark the visited block
	temp = board[r][c]
	board[r][c] = '#'

	# Below the recursion that tries all routes on the board
	# ↑ ↓
	find_all_boggle_helper(r - 1, c, word, board, rows, cols, ans, eng_dict)
	find_all_boggle_helper(r + 1, c, word, board, rows, cols, ans, eng_dict)

	# ← →
	find_all_boggle_helper(r, c - 1, word, board, rows, cols, ans, eng_dict)
	find_all_boggle_helper(r, c + 1, word, board, rows, cols, ans, eng_dict)

	# ↖ ↙
	find_all_boggle_helper(r - 1, c - 1, word, board, rows, cols, ans, eng_dict)
	find_all_boggle_helper(r + 1, c - 1, word, board, rows, cols, ans, eng_dict)

	# ↗ ↘
	find_all_boggle_helper(r - 1, c + 1, word, board, rows, cols, ans, eng_dict)
	find_all_boggle_helper(r + 1, c + 1, word, board, rows, cols, ans, eng_dict)

	# Un-mark the visited block
	board[r][c] = temp


def read_dictionary(file, eng_dict):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	target = ['firm', 'form', 'foil', 'coif', 'coir', 'corm', 'coil',
			  'moor', 'moil', 'miri', 'giro', 'glim', 'roil', 'roof',
		      'room', 'roomy', 'rimy', 'iglu', 'limy', 'limo', 'hoof']

	with open(file, 'r') as f:
		for line in f:
			if line.strip() in target:
				eng_dict.append(line.strip())
	return eng_dict


def has_prefix(sub_s, eng_dict):
	"""
	:param eng_dict: (list) A prepared English dictionary containing the target words
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in eng_dict:
		if not word.startswith(str(sub_s)):
			pass
		elif word.startswith(str(sub_s)):
			return True
	return False


if __name__ == '__main__':
	main()
