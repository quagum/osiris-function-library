from server.data_store import function_library

def addFunctionToLibrary(function_name: str, code: str, runtime: str, version: str = "1.0") -> bool:
    # Check if function already exists
    if function_name in function_library:
        return False, f"Function {function_name} version {version} already exists."

    # If it doesn't exist, create the database entry
    function_library[function_name] = {
        'name': function_name,
        'code': code,
        'runtime_env': runtime,
        'version': version,
        'versions': {version: code}
        }
    return True, f"Function {function_name} version {version} added successfully."

def updateFunctionInLibrary(function_name: str, code: str, version: str) -> bool:
    pass

def removeFunctionFromLibrary(function_name: str) -> bool:
    pass

def listFunctionsInLibrary() -> list:
    pass

def getFunctionDetails(function_name: str) -> dict:
    pass

def rollbackFunctionVersion(function_name: str, target_version: str) -> bool:
    if function_name in function_library:
        # Check if the target version exists in the versions dictionary
        if target_version in function_library[function_name]['versions']:
            # Rollback to the specified version
            function_library[function_name]['code'] = function_library[function_name]['versions'][target_version]
            function_library[function_name]['version'] = target_version
            return True, f"Function {function_name} rolled back to version {target_version}."
        else:
            return False, f"Version {target_version} not found for function {function_name}."
    return False, f"Function {function_name} not found in the library."

def searchFunctionByRuntime(runtime: str) -> list:
    pass

def publishFunction(function_name: str) -> bool:
    if function_name in function_library:
        function_library[function_name]['published'] = True
        return True, f"Function {function_name} published successfully." 
    return False, f"Failed to publish function {function_name}."

def unpublishFunction(function_name: str) -> bool:
    if function_name in function_library:
        function_library[function_name]['published'] = False
        return True, f"Function {function_name} unpublished successfully." 
    return False, f"Failed to unpublish function {function_name}."

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
        if function_name in function_library:
            function_library[function_name]["archive_status"] = True 
            return True, f"Function {function_name} archived."
        else:
            return False, f"Function {function_name} not in function library."
    except:
        return False, f"Unexpected error archiving function {function_name}."
