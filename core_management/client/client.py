import grpc
from core_management import core_management_pb2
from core_management import core_management_pb2_grpc
def run():
    # Connect to the gRPC server
    with grpc.insecure_channel('localhost:1500') as channel:
        stub = core_management_pb2_grpc.CoreManagementStub(channel)

        # Define your function details
        function_name = "myFunction"
        code = "def myFunction(): pass"
        runtime_env = "Python"
        version = "1.0"

        # Create a request to add a function
        add_function_request = core_management_pb2.AddFunctionRequest(
            function_name=function_name,
            code=code,
            runtime_env=runtime_env,
            version=version
        )

        # Create a request to archive a function
        archive_function_request = core_management_pb2.ArchiveFunctionRequest(
            function_name=function_name
        )

        # Call the AddFunction method on the stub
        add_function_response = stub.AddFunction(add_function_request)
        archive_function_response = stub.ArchiveFunction(archive_function_request)

        # Print the response from the server
        print(f"AddFunction response: success={add_function_response.success}, message='{add_function_response.message}'")
        print(f"ArchiveFunction response: success={archive_function_response.success}, message='{archive_function_response.message}'")
        
        publish_function_request = core_management_pb2.PublishFunctionRequest(function_name=function_name)
        publish_function_response = stub.PublishFunction(publish_function_request)

        # API 4: ListFunctions
        # Call the ListFunctions method on the stub
        list_functions_request = core_management_pb2.ListFunctionsRequest()
        list_functions_response = stub.ListFunctions(list_functions_request)
        
        # Print the response from ListFunctions
        print("ListFunctions response:")
        for function in list_functions_response.functions:
            print(f" - Name: {function.name}, Runtime: {function.runtime_env}, Version: {function.version}")

        # API 5: GetFunctionDetails
        # Call the GetFunctionDetails method on the stub
        get_function_details_request = core_management_pb2.GetFunctionDetailsRequest(
            function_name=function_name
        )
        get_function_details_response = stub.GetFunctionDetails(get_function_details_request)

        # Print the response from GetFunctionDetails
        if get_function_details_response.function.name:
            func = get_function_details_response.function
            print("GetFunctionDetails response:")
            print(f" - Name: {func.name}")
            print(f" - Code: {func.code}")
            print(f" - Runtime Environment: {func.runtime_env}")
            print(f" - Version: {func.version}")
        else:
            print("GetFunctionDetails response: Function not found")

        if publish_function_response.success:
            print(f"The function '{function_name}' was published successfully.")

        unpublish_function_response = stub.UnpublishFunction(publish_function_request)

        if unpublish_function_response.success:
            print(f"The function '{function_name}' was unpublished successfully.")
 

if __name__ == '__main__':
    run()
