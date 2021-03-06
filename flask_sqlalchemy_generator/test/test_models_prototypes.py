import unittest
from ..models_prototypes import  DataType, Parameter

class TestDataType(unittest.TestCase):
	DataType = DataType()
	def test_dataType_Usually(self):
		test_dataType_Usually = ['Boolean', 'Integer', 'String' ]
		self.assertEqual(DataType.dataType_Usually, test_dataType_Usually)

	def test_dataType_NonUsual(self):
		test_dataType_NonUsaul = ['Integer', 'Array', 'BIGINT',
        'BigINterger','BLOG', 'Boolean', 'BOOLEAN',
        'CHAR', 'CLOB', 'Comparator', 'Concatenable',
        'Date', 'DATE', 'Datetime', 'DATETIME', 'DECIMAL',
        'ENUM', 'Float', 'Float', 'Interval', 'JSON', 
        'JSONElementType', 'JSONIndexType', 'JSONPathType',
        'LargeBinary', 'MatchType', 'NCHAR', 'NullType',
        'Numeric', 'NUMBERIC', 'NVARCHAR',  'PickleType',
        'REAL', 'SchemaType', 'SMALLINT', 'SmallInterger',
        'String', 'TEXT', 'Text', 'Time', 'TIMESTAMP', 'TypeDecorator',
        'TypeEngine', 'Unicode', 'UnicodeText' , 'UserDefinedType',
        'VARBINARY','VARCHAR']
		self.assertEqual(DataType.dataType_NonUsaul, test_dataType_NonUsaul)


class TestParamter(unittest.TestCase):
	Parameter = Parameter()
	def test__init__(self):
		self.assertEqual(Parameter.ParameterName, '')
		self.assertEqual(Parameter.DataType, '')
		self.assertEqual(Parameter.NotNull, True)
		self.assertEqual(Parameter.CheckCondition, '')
		self.assertEqual(Parameter.PrimaryKey, True)
		self.assertEqual(Parameter.ForiegnKey, '')



if __name__ == '__main__':
	unittest.main()


# assertTrue(expr, msg=None)
# assertFalse(expr, msg=None)
# assertEqual(first, second, msg=None)
# assertNotEqual(first, second, msg=None)
