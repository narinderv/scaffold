
from hello import add, subtract, greet

x = 10
y = 6

def setup_function():
    print("Test Setup...\n")
    x = 10
    y = 6

def teardown_function():
    print("Test Teardown...\n")

def runTests():
    print("Addition Test:\n")
    #print("Add: ", add(x,y))
    assert add(x, y) == 16

    print("Subtraction Test:\n")
    assert subtract(x, y) == 4

setup_function()
runTests()
teardown_function()
