from unittest import TestCase
import nth_or_last 

class TestNthOrLast(TestCase):
    def test_basic(self):
        self.assertEqual(nth_or_last.nth_or_last(range(3),1),1)
        self.assertEqual(nth_or_last.nth_or_last(range(3),3),2)
    
    def test_default_value(self):
        default='zero'
        self.assertEqual(nth_or_last.nth_or_last(range(0),3,default),default)

    def test_empty_iterable_no_default(self):
        """
            in this method we set empty list without default to check error.
            if dont use lambda test fail and we still have error.
            if use lambda,then assertRaises can compare ValueError with
            output of lambda list

        """
        # self.assertRaises(ValueError,nth_or_last.nth_or_last(range(0),0))
        self.assertRaises(ValueError,lambda:nth_or_last.nth_or_last(range(0),0))
