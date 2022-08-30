import unittest
from __future__ import annotations

class Solution:
	# time = O(n) | space = O(1) where n = len(arr)
	def move_zeros(self, arr):
		'''
		return the array where all the zeros are at the end of the array and the relative order is preserved
		
		parameters:
			arr: List[int]
		return:
			output: List[int]
		'''
		zero_ct = arr.count(0)
		insertIdx = 0

		for idx, val in enumerate(arr):

			if val != 0:
				arr[insertIdx] = val
				insertIdx += 1

		for idx in reversed(range(zero_ct)):
			arr[-(idx+1)] = 0 

		return arr

obj = Solution()

class Test(unittest.TestCase):
	
	def test_1(self):
		self.assertEqual(obj.move_zeros([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]), [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0])
# 										                          i                
if __name__ == '__main__':
	unittest.main()