from unittest import TestCase
import firstt
import traceback

class TestFirst(TestCase):
    def test_many(self):
        self.assertEqual(firstt.first(x for x in range(4)),0)

    def test_one(self):
        self.assertEqual(firstt.first(['first']),'first')
        self.assertEqual(firstt.first([77]),77)
        
    def test_default(self):
        self.assertEqual(firstt.first([],'boo!!'),'boo!!')

    def test_empty_stop_iteration(self):
        # self.assertRaises(firstt.first([]),)
        try:
            firstt.first([])
        except ValueError:
            formatted_exec=traceback.format_exc()
            self.assertIn('StopIteration',formatted_exec)
            self.assertIn('The above exception was the direct cause',formatted_exec)
        else:
            self.fail()


