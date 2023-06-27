import unittest
import unit_test

class UnitTestTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(unit_test.add(4,5),9)
        self.assertEqual(unit_test.add(-1,5),4)

    
    def test_subtract(self):
        self.assertEqual(unit_test.subtract(7,5),2)
        self.assertEqual(unit_test.subtract(7,0),7)
        self.assertEqual(unit_test.subtract(0,9),-9)
        self.assertEqual(unit_test.subtract(4,5),-1)
        self.assertEqual(unit_test.subtract(-1,5),-6)

    def test_multiply(self):
        self.assertEqual(unit_test.multiply(4,5),20)
        self.assertEqual(unit_test.multiply(-1,5),-5)
        self.assertEqual(unit_test.multiply(0,5),0)

    def test_division(self):        
        self.assertEqual(unit_test.division(10,2),5)
        self.assertEqual(unit_test.division(-1,5),-0.2)
        self.assertEqual(unit_test.division(4,5),0.8)

        self.assertRaises(ZeroDivisionError,unit_test.division,4,0)

if __name__=='__main__':
    unittest.main()