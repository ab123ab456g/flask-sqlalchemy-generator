import unittest
from .test_models_prototypes import TestDataType


suite = unittest.TestSuite()

TestsJo1 = unittest.TestLoader().loadTestsFromTestCase(TestDataType)
suite.addTests(TestsJo1)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

# # 直接用addTest方法添加单个TestCase
# suite.addTest(TestMathFunc("test_multi"))

# # 用addTests + TestLoader
# # loadTestsFromName()，传入'模块名.TestCase名'
# suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
# suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))  # loadTestsFromNames()，类似，传入列表

# # loadTestsFromTestCase()，传入TestCase
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))