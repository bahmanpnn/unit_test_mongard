import pytestt
import pytest


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

        with pytest.raises(ZeroDivisionError):
            pytestt.division(3,0)

