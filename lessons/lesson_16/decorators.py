import pytest

pythonlist = ["python3.5", "python3.6", "python3.7"]


@pytest.fixture(params=pythonlist)
def python_version(request):
    return request.param


def test_python_version(python_version):
    assert python_version in pythonlist


# addopts = --strict-markers