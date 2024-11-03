import grpc
from core_management import core_management_pb2
from core_management import core_management_pb2_grpc

def run():
    # Connect to the gRPC server
    with grpc.insecure_channel('localhost:50051') as channel:
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

        # Call the AddFunction method on the stub
        add_function_response = stub.AddFunction(add_function_request)

        # Print the response from the server
        print(f"AddFunction response: success={add_function_response.success}, message='{add_function_response.message}'")
if __name__ == '__main__':
    run()
