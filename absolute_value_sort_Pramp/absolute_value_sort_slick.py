import unittest

# time = O(nlogn) | space = O(n) where n = len(arr)
# solution: sort array.
class Solution:

	def absolute_value_sort(self, arr):
		'''
		given an array of integers arr, write a function absSort(arr), that sorts the array according to the absolute values of the numbers in arr.
		If two numbers have the same absolute value, sort them according to sign, where the negative numbers come before the positive numbers.

		parameters:
			arr: List[int]
		return:
			result: List[int]
		'''
		return sorted(arr, key=lambda x: (abs(x), x))


class_obj = Solution()

class test(unittest.TestCase):
	
	def test_1(self):
		self.assertEqual(class_obj.absolute_value_sort([2, -7, -2, -2, 0]), [0, -2, -2, 2, -7])

if __name__ == '__main__':
	unittest.main()