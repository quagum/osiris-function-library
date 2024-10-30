from unittest.mock import MagicMock
from src import util


#archive_function tests
def test_fail_archive_function():
    util.archiveFunction = MagicMock(return_value=False)
    assert util.archiveFunction("function_name") == False 

def test_success_archive_function():
    util.archiveFunction = MagicMock(return_value=True)
    assert util.archiveFunction("function_name") == True 
