import pytest
from fixtures import Person
import time

# class TestPerson:

#     @pytest.fixture
#     def setup_teardown(self):
#         self.p1=Person('bahman','pournazari')
#         self.p2=Person('behzad','pournazari')
#         yield 'SetUpTearDown'
#         print('it does not print in this method!!')
#         time.sleep(1)
    
#     def test_fullname(self,setup_teardown):

#         assert self.p1.fullname(),'bahman pournazari'
#         assert self.p2.fullname(),'behzad pournazari'

#     def test_email(self,setup_teardown):

#         assert self.p1.email(),'bahmanpournazari@gmail.com'
#         assert self.p2.email(),'behzadpournazari@gmail.com'


#main pattern with (==)
class TestPerson:

    @pytest.fixture
    def setup_teardown(self):
        self.p1=Person('bahman','pournazari')
        self.p2=Person('behzad','pournazari')
        yield 'SetUpTearDown'
        print('it does not print in this method!!')
        time.sleep(1)
    
    def test_fullname(self,setup_teardown):

        assert self.p1.fullname() == 'bahman pournazari'
        assert self.p2.fullname() == 'behzad pournazari'

    def test_email(self,setup_teardown):

        assert self.p1.email() == 'bahmanpournazari@gmail.com'
        assert self.p2.email() == 'behzadpournazari@gmail.com'