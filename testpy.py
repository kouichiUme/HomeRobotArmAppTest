import pytest



# @pytest.fixture(autouse=True)
def test_FirstMode():
    assert (1, 2, 3) == (1, 2, 3)

