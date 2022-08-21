import pytest


@pytest.mark.smoke

def test_secondProgram():
    msg="Hello skip"
    assert msg =='Hi',"Test case failed because strings don not match"
#@pytest.skip
def test_firstProgram():
    print('Good evening')
def test_second1():
    print("This is smoke test")