import unittest
from ..models_prototypes import  DataType

DataType = DataType()

class TestDataType(unittest.TestCase):
	def test_dataType_Usually(self):
		test_dataType_Usually = ['Boolean', 'Integer', 'String' ]
		self.assertEqual(DataType.dataType_Usually, test_dataType_Usually)

	def test_dataType_Usually(self):
		test_dataType_Usually = ['Boolean', 'Integer', 'String' ]
		self.assertEqual(DataType.dataType_Usually, test_dataType_Usually)


if __name__ == '__main__':
	unittest.main()


# assertTrue(expr, msg=None)
# assertFalse(expr, msg=None)
# assertEqual(first, second, msg=None)
# assertNotEqual(first, second, msg=None)
