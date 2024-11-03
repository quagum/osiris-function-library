import grpc
from concurrent import futures
import core_management_pb2
import core_management_pb2_grpc

# Placeholder database
function_library = {}

def addFunctionToLibrary(function_name: str, code: str, runtime: str, version: str = "1.0") -> (bool):
    key = function_name + '_' + version
    if key in function_library:
        return False, f"Function {function_name} version {version} already exists."
    function_library[key] = {
        'name': function_name,
        'code': code,
        'runtime_env': runtime,
        'version': version
    }
    return True, f"Function {function_name} version {version} added successfully."

class CoreManagementServicer(core_management_pb2_grpc.CoreManagementServicer):
    def AddFunction(self, request, context):
        success, message = addFunctionToLibrary(request.function_name, request.code, request.runtime_env, request.version)
        return core_management_pb2.AddFunctionResponse(success=success, message=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    core_management_pb2_grpc.add_CoreManagementServicer_to_server(CoreManagementServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
