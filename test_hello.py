
from hello import add, subtract, greet


def test_add():
    x = 10
    y = 6
    print("Addition Test:\n")
    assert add(x, y) == 16

def test_subtract():
    x = 8
    y = 4
    print("Subtraction Test:\n")
    assert subtract(x, y) == 4

#setup_function()
#runTests()
#teardown_function()
