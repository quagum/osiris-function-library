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
        'version': version
        }
    return True, f"Function {function_name} version {version} added successfully."

def updateFunctionInLibrary(function_name: str, code: str, version: str) -> bool:
    '''Description:
        The updateFunctionInLibrary API updates the code and version of an existing function in the library.
        It requires the function name, new code, and a new version number.

        Input:
        function_name: The name of the function to update (string)
        code: The updated source code for the function (string)
        version: The new version of the function (string)

        Output:
        True if the function is successfully updated, False otherwise

    '''
    #check if function already exists
    if function_name in function_library:
        #perform update
        function_library[function_name].update({
            'code': code,
            'version': version
            })
        return True
    return False #function does not exist in library, cannot update

def removeFunctionFromLibrary(function_name: str) -> bool:
    '''Description:
        The removeFunctionFromLibrary API removes a function from the library based on its name.
        The function returns True if the function is successfully removes, False otherwise.
        
        Input: 
        function_name: The name of the function to be removed (string)

        Output:
        True if the function if successfully removed, False otherwise
        '''
    #Check if function is in library
    if function_name in function_library:
        #delete entry using del
        del function_library[function_name]
        return True
    return False

def listFunctionsInLibrary() -> list:
    pass

def getFunctionDetails(function_name: str) -> dict:
    pass

def rollbackFunctionVersion(function_name: str, target_version: str) -> bool:
    pass

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
