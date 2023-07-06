from unittest import TestCase
import last



class TestLast(TestCase):
    """
        with loop we can test many cases and with subtest we can see which of them has error when test failed!
        so subtest is not necessary but it is very helpful
        subtest must use with (with) because it is context manager==> with self.subtest():
    """
    def test_basic(self):
        cases=[
            (range(4),3),
            (iter(range(4)),3),
            (range(1),0),
            (iter(range(1)),0),
            ({n:str(n) for n in range(5)},4)
        ]
        for iterable,expected in cases:
            with self.subTest(iterable=iterable):
                self.assertEqual(last.last(iterable),expected)

    def test_default(self):
        for iterable,default,expected in [
            (range(1),None,0),
            ([],None,None),
            ({},None,None),
            (iter([]),None,None)
        ]:
            with self.subTest(args=(iterable,default)):
                self.assertEqual(last.last(iterable,default=default),expected)

    
    def test_empty(self):
        """
            iterable in this method has 2 state:
            1- [] = empty list 
            2- iter(range(0))= empty

            so we want to check this states and errors for testing
        """
        for iterable in ([],iter(range(0))):
            with self.subTest(iterable=iterable):
                with self.assertRaises(ValueError):
                    last.last(iterable)