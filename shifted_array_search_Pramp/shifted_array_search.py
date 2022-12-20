import unittest

# time = O(logn) | space = O(1) where n = len(arr)
# solution: Use binary search. If the middle does have it return index. Otherwise, left is sorted. If num is in left, shift the right pointer. Otherwise, move the left pointer.
# If left is not sorted, check if num is in the right array (which is sorted). If so, move left pointer accordingly. Otherwise, move right pointer to appropriately.
class Solution:

	def shifted_binary_search(self, arr, num):
		'''
		arr has been shifted left by a certain amount. Find out if num is in the rotated arr and return the corresponding index. If 
		it doesn't exist, return -1

		parameters:
			arr: List[int]
			num: int
		return:
			output: int
		'''
		left, right = 0, len(arr) - 1

		while left <= right:

			mid = (left + right) // 2

			if arr[mid] == num:
				return mid

			if arr[left] <= arr[mid]:

				if arr[left] <= num <= arr[mid]:
					right = mid - 1
				else:
					left = mid + 1
			else:

				if arr[mid] <= num <= arr[right]:
					left = mid + 1
				else:
					right = mid - 1

		return -1

class_obj = Solution()


class test(unittest.TestCase):
	
	def test_1(self):
		self.assertEqual(class_obj.shifted_binary_search([9, 12, 17, 2, 4, 5], 2), 3)

	def test_2(self):
		self.assertEqual(class_obj.shifted_binary_search([7], 2), -1)

	def test_3(self):
		self.assertEqual(class_obj.shifted_binary_search([5], 5), 0)


if __name__ == '__main__':
	unittest.main()
