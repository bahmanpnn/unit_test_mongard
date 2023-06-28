import unittest
from person import Person

# class PersonTest(unittest.TestCase):

#     def test_fullname(self):
#         p1=Person('bahman','pournazari')
#         p2=Person('behzad','pournazari')

#         self.assertEqual(p1.fullname(),'bahman pournazari')
#         self.assertEqual(p2.fullname(),'behzad pournazari')

#     def test_email(self):
#         p1=Person('bahman','pournazari')
#         p2=Person('behzad','pournazari')

#         self.assertEqual(p1.email(),'bahmanpournazari@gmail.com')
#         self.assertEqual(p2.email(),'behzadpournazari@gmail.com')


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

if __name__=='__main__':
    unittest.main()