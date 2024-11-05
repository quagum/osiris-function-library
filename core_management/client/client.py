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

        # Create a request to publish a function
        publish_function_request = core_management_pb2.PublishFunctionRequest(
            function_name=function_name
        )

        # Create a request to update a function
        update_function_request = core_management_pb2.UpdateFunctionRequest(
            function_name=function_name,
            code=code,
            version=version,
        )

        # Create a request to remove a function
        remove_function_request = core_management_pb2.RemoveFunctionRequest(
            function_name=function_name,
        )

        # Create a request to archive a function
        archive_function_request = core_management_pb2.ArchiveFunctionRequest(
            function_name=function_name
        )

        
   
        # Call the AddFunction method on the stub
        add_function_response = stub.AddFunction(add_function_request)
        update_function_response = stub.UpdateFunction(update_function_request)
        remove_function_response = stub.RemoveFunction(remove_function_request)
        publish_function_response = stub.PublishFunction(publish_function_request)
        unpublish_function_response = stub.UnpublishFunction(publish_function_request)
        archive_function_response = stub.ArchiveFunction(archive_function_request)

        # Print the response from the server
        print(f"AddFunction response: success={add_function_response.success}, message='{add_function_response.message}'")
        print(f"UpdateFunction response: success={update_function_response.success}, message='{add_function_response.message}'")
        print(f"RemoveFunction response: success={remove_function_response.success}, message='{remove_function_response.message}'")
        print(f"PublishFunction response: success={publish_function_response.success}, message='{publish_function_response.message}'")
        print(f"UnpublishFunction response: success={publish_function_response.success}, message='{unpublish_function_response.message}'")
        print(f"ArchiveFunction response: success={archive_function_response.success}, message='{archive_function_response.message}'")

if __name__ == '__main__':
    run()
