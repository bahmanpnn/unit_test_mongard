import unittest
from pytestt import Person
import pytestt 

# #ep3
class PersonTest(unittest.TestCase):

    def setUp(self):
        self.p1=Person('bahman','pournazari')
        self.p2=Person('behzad','pournazari')

    def tearDown(self):
        print('Done!!')
    
    def test_fullname(self):

        self.assertEqual(self.p1.fullname(),'bahman pournazari')
        self.assertEqual(self.p2.fullname(),'behzad pournazari')

    def test_email(self):

        self.assertEqual(self.p1.email(),'bahmanpournazari@gmail.com')
        self.assertEqual(self.p2.email(),'behzadpournazari@gmail.com')


# #ep2
class UnitTestTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(pytestt.add(4,5),9)
        self.assertEqual(pytestt.add(-1,5),4)

    
    def test_subtract(self):
        self.assertEqual(pytestt.subtract(7,5),2)
        self.assertEqual(pytestt.subtract(7,0),7)
        self.assertEqual(pytestt.subtract(0,9),-9)
        self.assertEqual(pytestt.subtract(4,5),-1)
        self.assertEqual(pytestt.subtract(-1,5),-6)

    def test_multiply(self):
        self.assertEqual(pytestt.multiply(4,5),20)
        self.assertEqual(pytestt.multiply(-1,5),-5)
        self.assertEqual(pytestt.multiply(0,5),0)

    def test_division(self):        
        self.assertEqual(pytestt.division(10,2),5)
        self.assertEqual(pytestt.division(-1,5),-0.2)
        self.assertEqual(pytestt.division(4,5),0.8)

        self.assertRaises(ZeroDivisionError,pytestt.division,4,0)

# #ep4
class UnitTestTest(unittest.TestCase):

    def test_add(self):
        assert pytestt.add(4,5)==9
        assert pytestt.add(-1,5)==4
        assert pytestt.add(0,8)==8

    def test_subtract(self):
        assert pytestt.subtract(7,5)==2
        assert pytestt.subtract(7,0)==7
        assert pytestt.subtract(0,9)==-9
        assert pytestt.subtract(4,5)==-1
        assert pytestt.subtract(-1,5)==-6


    def test_multiply(self):
        assert pytestt.multiply(4,5)==20
        assert pytestt.multiply(-1,5)==-5
        assert pytestt.multiply(0,5)==0
        assert pytestt.multiply(3,4)!=11

    def test_division(self):
        assert pytestt.division(10,2)==5
        assert pytestt.division(-1,5)==-0.2
        assert pytestt.division(4,5)==0.8




#main test pattern for pytest
#every class and method can worked with pytest but for writing test woth pytest must do like this pattern
class TestPytest:

    def test_add(self):
        assert pytestt.add(4,5)==9
        assert pytestt.add(-1,5)==4
        assert pytestt.add(0,8)==8

    def test_subtract(self):
        assert pytestt.subtract(7,5)==2
        assert pytestt.subtract(7,0)==7
        assert pytestt.subtract(0,9)==-9
        assert pytestt.subtract(4,5)==-1
        assert pytestt.subtract(-1,5)==-6


    def test_multiply(self):
        assert pytestt.multiply(4,5)==20
        assert pytestt.multiply(-1,5)==-5
        assert pytestt.multiply(0,5)==0
        assert pytestt.multiply(3,4)!=11

    def test_division(self):
        assert pytestt.division(10,2)==5
        assert pytestt.division(-1,5)==-0.2
        assert pytestt.division(4,5)==0.8