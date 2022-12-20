from collections import deque
import string
import unittest


class Solution:

	# time = O(m * (V + E)) | space = O(m * V) where V = # of nodes in graph, E = # of edges (words differ by 1 letter), and m = length of the longest word
	# solution: use bfs. Check if target is in vocabulary first. If not, return -1. Otherwise, adjoin it to vocabulary. See code to see neighbors.
	def shortest_word_edit_path(self, source, target, words):
		'''
		Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.
		Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

		parameters:
			source: str
			target: str
			words: List[str]
		return:
			output: int
		'''
		vocabulary = set(words)

		if target not in vocabulary:
			return -1

		vocabulary.add(target)

		queue = deque([(source, 0)])
		visited = set([source])

		while len(queue) > 0:

			current_word, steps = queue.popleft()

			if current_word == target:
				return steps

			for idx in range(len(current_word)):
				for char in string.ascii_lowercase:

					neighbor_word = current_word[:idx] + char + current_word[idx+1:]

					if neighbor_word not in vocabulary or neighbor_word in visited:
						continue

					visited.add(neighbor_word)
					queue.append((neighbor_word, steps + 1))

		return -1

class_obj = Solution()


class test(unittest.TestCase):

	def test_1(self):
		self.assertEqual(class_obj.shortest_word_edit_path('bit', 'dog', ['but', 'put', 'big', 'pot', 'pog', 'dog', 'lot']), 5)

	def test_2(self):
		self.assertEqual(class_obj.shortest_word_edit_path('no', 'go', ['to']), -1)


if __name__ == '__main__':
	unittest.main()
