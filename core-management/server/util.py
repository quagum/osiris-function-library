# Placeholder database
function_library = {}

def addFunctionToLibrary(function_name: str, code: str, runtime: str, version: str = "1.0") -> bool:
    # Create a key for the database entry
    key = function_name + '_' + version

    # Check if function already exists
    if key in function_library:
        return False

    # If it doesn't exist, create the database entry
    function_library[key] = {
        'name': function_name,
        'code': code,
        'runtime_env': runtime,
        'version': version
        }
    return True

def updateFunctionInLibrary(function_name: str, code: str, version: str) -> bool:
    pass

def removeFunctionFromLibrary(function_name: str) -> bool:
    pass

def listFunctionsInLibrary() -> list:
    pass

def getFunctionDetails(function_name: str) -> dict:
    pass

def rollbackFunctionVersion(function_name: str, target_version: str) -> bool:
    pass

def searchFunctionByRuntime(runtime: str) -> list:
    pass

def publishFunction(function_name: str) -> bool:
    pass

def unpublishFunction(function_name: str) -> bool:
    pass

def archiveFunction(function_name: str) -> bool:
    '''Description:
        The archiveFunction API archives a function, which removes it from active usage but retains its information and code in the library for future reference.
        Archived functions can be restored later if needed.

        Input:
        function_name: The name of the function to archive. (string)
        
        Output:
        True if the function is successfully archived, False otherwise.
    '''
    try:
        return unpublishFunction(function_name)
    except:
        return False 
