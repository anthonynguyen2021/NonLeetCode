import unittest


# time = O(1) = space
# solution: simulation.
class Solution:

	def validate_ip_address(self, ip):
		'''
		return if a string is a valid ip address. Validate an IP address (IPv4). An address is valid iff it is in the form of X.X.X.X where each X is a number from 0 to 255

		parameters:
			ip: str

		return:
			output: bool
		'''
		if len(ip) == 0: return False

		result = ip.split('.')

		if len(result) != 4: return False

		for item in result:

			if not item.isdigit(): return False
			elif not 0 <= int(item) <= 255: return False

		return True

class_obj = Solution()


class test(unittest.TestCase):
	
	def test_1(self):
		self.assertEqual(class_obj.validate_ip_address('192.168.0.1'), True)

	def test_2(self):
		self.assertEqual(class_obj.validate_ip_address('0.0.0.0'), True)

	def test_3(self):
		self.assertEqual(class_obj.validate_ip_address('123.24.59.99'), True)

	def test_4(self):
		self.assertEqual(class_obj.validate_ip_address('192.168.123.456'), False)

	def test_5(self):
		self.assertEqual(class_obj.validate_ip_address('12.34.56.oops'), False)


if __name__ == '__main__':
	unittest.main()
