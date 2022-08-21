import pytest
@pytest.fixture(scope = "class")
def setup():
    print('I will execute first')
    yield
    print("I will be executed  last")
@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return["Rahul","Shetty","rahulshetty/Academy.com"]
@pytest.fixture(params=[('chrome','Rahul','Shetty'),'Firefox','IE'])
def crossBrowser(request):
    return request.param