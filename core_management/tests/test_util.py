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

# listFunctionsInLibrary tests
def test_list_functions_empty():
    util.listFunctionsInLibrary = MagicMock(return_value=[])
    functions = util.listFunctionsInLibrary()
    assert functions == []

def test_list_functions_non_empty():
    mock_functions = [
        {"name": "function1", "code": "code1", "runtime_env": "Python", "version": "1.0"},
        {"name": "function2", "code": "code2", "runtime_env": "JavaScript", "version": "1.0"}
    ]
    util.listFunctionsInLibrary = MagicMock(return_value=mock_functions)
    functions = util.listFunctionsInLibrary()
    assert len(functions) == 2
    assert functions[0]["name"] == "function1"
    assert functions[1]["name"] == "function2"

# getFunctionDetails tests
def test_get_function_details_found():
    mock_function = {
        "name": "function1",
        "code": "def function1(): pass",
        "runtime_env": "Python",
        "version": "1.0"
    }
    util.getFunctionDetails = MagicMock(return_value=mock_function)
    function_details = util.getFunctionDetails("function1")
    assert function_details["name"] == "function1"
    assert function_details["runtime_env"] == "Python"

def test_get_function_details_not_found():
    util.getFunctionDetails = MagicMock(return_value=None)
    function_details = util.getFunctionDetails("non_existent_function")
    assert function_details is None