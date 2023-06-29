# import unittest
import main_nose

def test_add():
    assert main_nose.add(4,5)==9
    assert main_nose.add(-1,5)==4
    assert main_nose.add(0,8)==8

def test_subtract():
    assert main_nose.subtract(7,5)==2
    assert main_nose.subtract(7,0)==7
    assert main_nose.subtract(0,9)==-9
    assert main_nose.subtract(4,5)==-1
    assert main_nose.subtract(-1,5)==-6


def test_multiply():
    assert main_nose.multiply(4,5)==20
    assert main_nose.multiply(-1,5)==-5
    assert main_nose.multiply(0,5)==0
    assert main_nose.multiply(3,4)!=11

def test_division():
    assert main_nose.division(10,2)==5
    assert main_nose.division(-1,5)==-0.2
    assert main_nose.division(4,5)==0.8


#nosetest worked on unittest class too!!   
# class Main_NoseTest(unittest.TestCase):

#     def test_add(self):
#         self.assertEqual(unit_test.add(4,5),9)
#         self.assertEqual(unit_test.add(-1,5),4)

    
#     def test_subtract(self):
#         self.assertEqual(unit_test.subtract(7,5),2)
#         self.assertEqual(unit_test.subtract(7,0),7)
#         self.assertEqual(unit_test.subtract(0,9),-9)
#         self.assertEqual(unit_test.subtract(4,5),-1)
#         self.assertEqual(unit_test.subtract(-1,5),-6)

#     def test_multiply(self):
#         self.assertEqual(unit_test.multiply(4,5),20)
#         self.assertEqual(unit_test.multiply(-1,5),-5)
#         self.assertEqual(unit_test.multiply(0,5),0)

#     def test_division(self):        
#         self.assertEqual(unit_test.division(10,2),5)
#         self.assertEqual(unit_test.division(-1,5),-0.2)
#         self.assertEqual(unit_test.division(4,5),0.8)

#         self.assertRaises(ZeroDivisionError,unit_test.division,4,0)

# if __name__=='__main__':
#     unittest.main()


