"""
Functional test for the add operation
"""
from main import add
def test_index():

    response = add(2, 3)
    assert response == 6
