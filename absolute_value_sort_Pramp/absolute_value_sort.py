import unittest

# time = O(nlogn) | space = O(n) where n = len(arr)
# solution: sort array. then use two pointers from beginning and end of the sorted array and compare. Then we insert from the rear.
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
		arr.sort()
		left, right = 0, len(arr) - 1
		result = [0] * len(arr)
		insertIdx = len(arr)-1

		while left <= right:

			if abs(arr[left]) < abs(arr[right]):
				result[insertIdx] = arr[right]
				right -= 1
			elif abs(arr[left]) > abs(arr[right]):
				result[insertIdx] = arr[left]
				left += 1
			else:
				result[insertIdx] = arr[right]
				right -= 1
			insertIdx -= 1

		return result


class_obj = Solution()

class test(unittest.TestCase):
	
	def test_1(self):
		self.assertEqual(class_obj.absolute_value_sort([2, -7, -2, -2, 0]), [0, -2, -2, 2, -7])

if __name__ == '__main__':
	unittest.main()