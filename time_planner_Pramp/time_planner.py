import unittest

# time = O(m + n) | space = O(1) where m, n = len(arr1), len(arr2)
# solution: use two pointers. Starting with one, if its ending time is less than the starting of the right
# increment. Similarly, do the same with two. At this point, the intersection is non-empty. Then check their 
# intersection and if its length is at least dur, return the solution of length dur. Otherwise, increment index 1.
class Solution:

	def time_planner(self, arr1, arr2, dur):

		idx1, idx2 = 0, 0

		while idx1 < len(arr1) and idx2 < len(arr2):

			while idx1 < len(arr1) and arr1[idx1][1] < arr2[idx2][0]:
				idx1 += 1

			if idx1 == len(arr1):
				break

			while idx2 < len(arr2) and arr2[idx2][1] < arr1[idx1][0]:
				idx2 += 1

			if idx2 == len(arr2):
				break

			left = max(arr1[idx1][0], arr2[idx2][0])
			right = min(arr1[idx1][1], arr2[idx2][1])

			if right - left >= dur:
				return [left, left + dur]

			idx1 += 1

		return []

class_obj = Solution()


class test(unittest.TestCase):

	def test_1(self):

		self.assertEqual(class_obj.time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8), [60, 68])

	def test_2(self):

		self.assertEqual(class_obj.time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12), [])


if __name__ == '__main__':
	unittest.main()
