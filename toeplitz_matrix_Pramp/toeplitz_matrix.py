import unittest


class Solution:
	# time = O(m * n) | space = O(1) where m, n = len(matrix), len(matrix[0])
	def is_toeplitz(self, matrix):
		'''
		Given matrix, return True if it is toeplitz. Else, False.

		parameters:
			matrix: List[List[int]]
		return:
			output: bool
		'''
		def diagonal_constant(r, c):

			candidate = matrix[r][c]

			while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):

				if matrix[r][c] != candidate:
					return False
				r += 1
				c += 1

			return True

		for rowIdx in range(len(matrix)):

			if not diagonal_constant(rowIdx, 0):
				return False

		for colIdx in range(1, len(matrix[0])):
			if not diagonal_constant(0, colIdx):
				return False

		return True

class_obj = Solution()


class test(unittest.TestCase):
	
	def test_1(self):
		self.assertEqual(class_obj.is_toeplitz([[1, 2, 3, 4], [5, 1, 2, 3], [6, 5, 1, 2]]), True)

	def test_2(self):
		self.assertEqual(class_obj.is_toeplitz([[1, 2, 3, 4], [5, 1, 9, 3], [6, 5, 1, 2]]), False)


if __name__ == '__main__':
	unittest.main()
