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
        rollback_function_request = core_management_pb2.RollbackFunctionVersionRequest(
            function_name=function_name,
            target_version="1.0"
        )
        # Publish to archive a function
        publish_function_request = core_management_pb2.PublishFunctionRequest(
            function_name=function_name
        )

        # Create a request to archive a function
        archive_function_request = core_management_pb2.ArchiveFunctionRequest(
            function_name=function_name
        )

        search_function_by_runtime_request = core_management_pb2.SearchFunctionByRuntimeRequest(
            runtime=runtime_env 
        )
   
        # Call the AddFunction method on the stub
        add_function_response = stub.AddFunction(add_function_request)
        archive_function_response = stub.ArchiveFunction(archive_function_request)
        publish_function_response = stub.PublishFunction(publish_function_request)
        unpublish_function_response = stub.UnpublishFunction(publish_function_request)
        rollback_function_response = stub.RollbackFunctionVersion(rollback_function_request)
        search_function_by_runtime_response = stub.SearchFunctionByRuntime(search_function_by_runtime_request)

        # Print the response from the server
        print(f"AddFunction response: success={add_function_response.success}, message='{add_function_response.message}'")
        print(f"PublishFunction response: success={publish_function_response.success}, message='{publish_function_response.message}'")
        print(f"UnpublishFunction response: success={publish_function_response.success}, message='{unpublish_function_response.message}'")
        print(f"ArchiveFunction response: success={archive_function_response.success}, message='{archive_function_response.message}'")
        print(f"RollbackFunctionVersion response: success={rollback_function_response.success}, message='{rollback_function_response.message}'")
        print("SearchFunctionByRuntime response:")
        for func in search_function_by_runtime_response.functions:
            print(f"Function Name: {func.function_name}, Version: {func.version}")

if __name__ == '__main__':
    run()
