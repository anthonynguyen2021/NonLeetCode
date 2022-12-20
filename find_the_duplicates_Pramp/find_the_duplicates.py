import unittest


class Solution:
	# time = O(n + m) | space = O(min(m, n)) where m, n = len(arr1), len(arr2).
	# solution: We can hash all the elements in the shorter array and see if elements in arr2 are in the hashmap. An alternate solution 
	# uses binary search but is slower. If m, n are approximately the same magnitude.

	def find_duplicates(self, arr1, arr2):
		'''
		Given two sorted arrays arr1 and arr2 of numbers, return all numbers that are in both arr1 and arr2.
		Output should be sorted in ascending order.

		parameters:
			arr1: List[int]
			arr2: List[int]
		return:
			output: List[int]
		'''
		if len(arr2) < len(arr1):
			return self.find_duplicates(arr2, arr1)

		recall = set()
		result = []

		for val_1 in arr1:
			recall.add(val_1)

		for val_2 in arr2:
			if val_2 in recall:
				result.append(val_2)

		return result

class_obj = Solution()


class test(unittest.TestCase):
	
	def test_1(self):
		self.assertEqual(class_obj.find_duplicates(

			[1, 2, 3, 5, 6, 7],
			[3, 6, 7, 8, 20]),
			[3, 6, 7]
						)


if __name__ == '__main__':
	unittest.main()
