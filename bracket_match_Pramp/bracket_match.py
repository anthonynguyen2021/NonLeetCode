import unittest

class Solution:

	def bracket_match(self, text):
		
		left_count = 0
		min_add = 0

		for char in text:

			if char == '(':
				left_count += 1
			elif left_count > 0:
				left_count -= 1
			else:
				min_add += 1

		return min_add + left_count

class_obj = Solution()

class test(unittest.TestCase):
	
	def test_1(self):
		self.assertEqual(class_obj.bracket_match('(()'), 1)
	def test_2(self):
		self.assertEqual(class_obj.bracket_match('(())'), 0)
	def test_3(self):
		self.assertEqual(class_obj.bracket_match('())('), 2)

if __name__ == '__main__':
	unittest.main()