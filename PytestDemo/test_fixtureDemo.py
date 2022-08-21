import pytest
@pytest.mark.usefixtures("setup")
class testexample:
    def test_fixtureDemo0(self):
        print('I will execute fixturedemo0 method ')
    def test_fixtureDemo1(self):
        print('I will execute fixturedemo1 method')

    def test_fixtureDemo2(self):
        print('I will execute fixturedemo2 method')




