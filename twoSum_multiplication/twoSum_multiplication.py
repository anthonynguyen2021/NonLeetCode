'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they multiply to target.
If there's no solution, return inf
Return solution in any order
'''
import unittest


class Solution:
	# time = O(n) where n = len(nums)
	# space = O(n) 
	# solution: similar to two sum. Handle when entries are 0, target % val != 0
	def two_sum_mult(self, nums, target):
		
		if len(nums) < 2:
			return float('inf')
		elif target == 0 and nums.count(0) == 0:
			return float('inf')

		seen = dict()

		for idx, val in enumerate(nums):

			if val == 0:
				continue
			elif target % val != 0:
				continue

			if (target // val) * val == target and (target // val) in seen:
				return sorted([idx, seen[target // val]])

			seen[val] = idx

		return float('inf')

class_obj = Solution()


class test(unittest.TestCase):

	def test_1(self):
		self.assertEqual(class_obj.two_sum_mult([1], 2), float('inf'))

	def test_2(self):
		self.assertEqual(class_obj.two_sum_mult([1, 2, 3, 4], 12), [2, 3])

	def test_3(self):
		self.assertEqual(class_obj.two_sum_mult([], 3), float('inf'))

	def test_4(self):
		self.assertEqual(class_obj.two_sum_mult([2, -3], -6), [0, 1])


if __name__ == '__main__':
	unittest.main()
