class Datatype:
    dataType_Usually = ['Boolean', 'Integer', 'String' ]
    dataType_NonUsaul = ['Integer', 'Array', 'BIGINT',
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
        'VARBINARY', 'VARCHAR']


class Patameter(object):
    def __init__(self):
        self.ParameterName = ''
        self.DataType = ''
        self.NotNull = True
        self.CheckCondition = ''
        self.PrimaryKey = True
        self.ForiegnKey = ''



class Prototype(object):
    def __init__(self):
        self.Name = ''
        self.Parameter = ''
        self.Parameter1Setti
        ng = {'DataType':'int', 'Not Null':True, }
