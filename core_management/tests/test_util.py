from unittest.mock import MagicMock
from core_management.server import util

# addFunctionToLibrary tests
def test_fail_add_function():
    util.addFunctionToLibrary = MagicMock(return_value=False)
    assert util.addFunctionToLibrary("function_name") == False

def test_success_add_function():
    util.addFunctionToLibrary = MagicMock(return_value=True)
    assert util.addFunctionToLibrary("function_name") == True    

#archive_function tests
def test_fail_archive_function():
    util.archiveFunction = MagicMock(return_value=False)
    assert util.archiveFunction("function_name") == False 

def test_success_archive_function():
    util.archiveFunction = MagicMock(return_value=True)
    assert util.archiveFunction("function_name") == True
